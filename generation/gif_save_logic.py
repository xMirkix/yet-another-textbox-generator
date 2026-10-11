import io
import math
import struct
import subprocess
import re
from pathlib import Path
import random

from PIL import Image

from generation.ffmpeg_locator import FfmpegNotFoundError, get_ffmpeg_path

TRANSPARENT_IDX = 255


def _encode_single_frame(img: Image.Image, dither: bool = True) -> bytes:
    has_alpha = img.mode in ('RGBA', 'LA') or 'transparency' in img.info

    if img.mode != 'P':
        rgba = img.convert('RGBA')
        rgb = rgba.convert('RGB')

        quantized = rgb.quantize(
            colors=255,
            method=Image.Quantize.MEDIANCUT,
            dither=Image.Dither.FLOYDSTEINBERG if dither else Image.Dither.NONE
        )

        if has_alpha:
            alpha = rgba.split()[-1]
            mask = alpha.point(lambda a: 255 if a < 128 else 0).convert('1')
            if mask.getbbox() is not None:
                quantized.paste(255, mask)
                quantized.info['transparency'] = 255

        img = quantized

    buf = io.BytesIO()
    save_kwargs = {'format': 'GIF'}
    if 'transparency' in img.info:
        save_kwargs['transparency'] = img.info['transparency']
    img.save(buf, **save_kwargs)
    return buf.getvalue()


def _extract_image_block(gif_bytes: bytes) -> tuple[bytes, bool, int]:
    raw = bytearray(gif_bytes)
    pos = 6

    packed_lsd = raw[pos + 4]
    pos += 7

    gct_bytes = b''
    if packed_lsd & 0x80:
        gct_size = 3 * (2 ** ((packed_lsd & 0x07) + 1))
        gct_bytes = bytes(raw[pos: pos + gct_size])
        pos += gct_size

    has_transparency = False
    trans_idx = 0
    image_block = b''

    while pos < len(raw):
        b = raw[pos]
        if b == 0x2C:  # Image Descriptor
            start = pos
            packed_img = raw[start + 9]

            gct_size_bitmask = packed_lsd & 0x07
            raw[start + 9] = packed_img | 0x80 | gct_size_bitmask

            pos += 10

            if packed_img & 0x80:
                pos += 3 * (2 ** ((packed_img & 0x07) + 1))

            pos += 1
            while raw[pos]:
                pos += raw[pos] + 1
            pos += 1

            descriptor_header = bytes(raw[start: start + 10])
            lzw_and_terminator = bytes(raw[start + 10: pos])

            image_block = descriptor_header + gct_bytes + lzw_and_terminator
            break

        elif b == 0x21:  # Extension Block
            ext_type = raw[pos + 1]
            if ext_type == 0xF9:  # Graphic Control Extension found
                packed_gce = raw[pos + 3]
                has_transparency = bool(packed_gce & 0x01)
                trans_idx = raw[pos + 6]

            pos += 2
            while raw[pos]:
                pos += raw[pos] + 1
            pos += 1
        else:
            break

    if not image_block:
        raise ValueError("No image descriptor found")

    return image_block, has_transparency, trans_idx


def save_gif(frames: list[Image.Image], durations: list[int], path: Path):
    w, h = frames[0].size
    out = io.BytesIO()

    out.write(b'GIF89a')
    out.write(struct.pack('<HH', w, h))
    out.write(bytes([0x00, 0x00, 0x00]))

    out.write(bytes([0x21, 0xFF, 0x0B]) + b'NETSCAPE2.0' +
              bytes([0x03, 0x01, 0x00, 0x00, 0x00]))

    for frame, duration in zip(frames, durations):
        gif_bytes = _encode_single_frame(frame)
        image_block, has_trans, trans_idx = _extract_image_block(gif_bytes)

        delay_cs = max(1, duration // 10)

        gce_packed = 0x09 if has_trans else 0x08

        out.write(bytes([
            0x21, 0xF9, 0x04,
            gce_packed,
            delay_cs & 0xFF, (delay_cs >> 8) & 0xFF,
            trans_idx if has_trans else 0x00,
            0x00,
        ]))

        out.write(image_block)

    out.write(bytes([0x3B]))
    path.write_bytes(out.getvalue())



class Mp4EncodingError(Exception):
    pass


def clip_duration_ms(ffmpeg_path, sound: Path) -> int:
    result = subprocess.run(
        [str(ffmpeg_path), "-hide_banner", "-i", str(sound)],
        capture_output=True, text=True, errors="ignore",
    )
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", result.stderr)
    if not m:
        raise Mp4EncodingError(f"Could not read duration of {sound}")
    h, mnt, s = int(m[1]), int(m[2]), float(m[3])
    return int((h * 3600 + mnt * 60 + s) * 1000)


def _picker(rng: random.Random, indices: list[int]):
    last = None

    def pick() -> int:
        nonlocal last
        pool = [i for i in indices if i != last] or indices
        last = rng.choice(pool)
        return last

    return pick


def build_events(letter_frames, n_left, n_right, mono, rng):
    speakers = []  # (picker, pan)
    if n_left:
        speakers.append((_picker(rng, list(range(n_left))), -1))
    if n_right:
        speakers.append((_picker(rng, list(range(n_left, n_left + n_right))), 1))

    events = []
    for frame in letter_frames:
        for ch, (pick, side) in enumerate(speakers):  # one channel per speaker
            events.append((frame, pick(), ch, 0 if mono else side))
    return events


def plan_events(events, durations, frame_ms, overlap_clips: bool):
    planned = []
    for n, (frame, inp, ch, pan) in enumerate(events):
        start = frame * frame_ms
        play, cut = durations[inp], False
        if not overlap_clips:
            for later in events[n + 1:]:
                if later[2] == ch:
                    gap = later[0] * frame_ms - start
                    if gap < play:
                        play, cut = gap, True
                    break
        planned.append((start, inp, play, cut, pan))
    return planned


_PAN = {
    -1: "pan=stereo|c0=c0|c1=0*c0",
    0: "pan=stereo|c0=c0|c1=c0",
    1: "pan=stereo|c0=0*c0|c1=c0",
}


def audio_filter(planned, total_ms: float, volume: float = 1.0) -> str:
    by_input: dict[int, list] = {}
    for e in planned:
        by_input.setdefault(e[1], []).append(e)

    parts, labels = [], []
    for inp, evs in by_input.items():
        n = len(evs)
        outs = [f"[s{inp}_{j}]" for j in range(n)]
        head = f"[{inp + 1}:a]aformat=sample_rates=44100:channel_layouts=mono"
        parts.append(head + (f",asplit={n}{''.join(outs)}" if n > 1 else outs[0]))
        for j, (start, _, play, cut, pan) in enumerate(evs):
            chain = [f"atrim=end={play / 1000:.4f}", "asetpts=PTS-STARTPTS"]
            if cut:
                chain.append(f"afade=t=out:st={max(0, play - 5) / 1000:.4f}:d=0.005")
            chain += [_PAN[pan], f"adelay={int(start)}:all=1"]
            parts.append(f"{outs[j]}{','.join(chain)}[d{inp}_{j}]")
            labels.append(f"[d{inp}_{j}]")

    parts.append(
        f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:duration=longest,"
        f"volume={volume:.3f},"
        f"alimiter=limit=0.9:level=disabled,"
        f"apad=whole_dur={total_ms / 1000:.3f},atrim=end={total_ms / 1000:.3f}[aout]"
    )
    return ";".join(parts)


def save_mp4(
    frames: list[Image.Image],
    frame_duration_ms: float,
    letter_frames: list[int],
    sounds_left: list[Path],
    sounds_right: list[Path],
    advanced_options: tuple[bool, bool, float],
    path: Path,
    min_tail_seconds: float = 1.75,
) -> None:
    if not frames:
        return

    try:
        ffmpeg_path = get_ffmpeg_path()
        sounds = list(sounds_left) + list(sounds_right)
        has_audio = bool(sounds and letter_frames)

        tail_ms = int(min_tail_seconds * 1000)
        base_ms = len(frames) * frame_duration_ms
        audio_filter_str = None

        if has_audio:
            mono = advanced_options[0]
            rng = random.Random(hash(tuple(letter_frames)))
            events = build_events(letter_frames, len(sounds_left), len(sounds_right),
                                  mono, rng)
            durations = {i: clip_duration_ms(ffmpeg_path, s) for i, s in enumerate(sounds)}
            planned = plan_events(events, durations, frame_duration_ms, advanced_options[1])
            audio_end = max(start + play for start, _, play, _, _ in planned)
            tail_ms = max(tail_ms, int(max(0, audio_end - base_ms)) + 250)

        extra_tail_frames = math.ceil(tail_ms / frame_duration_ms)
        full_frames = frames + [frames[-1]] * extra_tail_frames
        total_ms = len(full_frames) * frame_duration_ms

        if has_audio:
            audio_filter_str = audio_filter(planned, total_ms, advanced_options[2])

        _encode_via_pipe(
            full_frames, 1000.0 / frame_duration_ms, path, ffmpeg_path,
            sounds if has_audio else [], audio_filter_str,
        )

    except (FfmpegNotFoundError, Mp4EncodingError):
        raise
    except Exception as e:
        raise Mp4EncodingError(str(e)) from e


def _encode_via_pipe(
    frames: list[Image.Image],
    fps: float,
    path: Path,
    ffmpeg_path,
    sounds: list[Path],
    audio_filter: str | None,
) -> None:
    width, height = frames[0].size
    path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        str(ffmpeg_path), "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{width}x{height}", "-r", str(fps),
        "-i", "pipe:0",
    ]
    for s in sounds:
        cmd += ["-i", str(s)]

    if audio_filter:
        cmd += [
            "-filter_complex", audio_filter,
            "-map", "0:v", "-map", "[aout]",
            "-c:a", "aac", "-b:a", "160k",
        ]

    cmd += [
        "-vf", "crop=trunc(iw/2)*2:trunc(ih/2)*2",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(path),
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        for frame in frames:
            proc.stdin.write(frame.convert("RGB").tobytes())
        proc.stdin.close()
    except BrokenPipeError:
        pass  # ffmpeg exited early; its stderr is reported below
    finally:
        try:
            proc.stdin.close()
        except BrokenPipeError:
            pass
        stderr = proc.stderr.read().decode(errors="ignore")
        proc.wait()

    if proc.returncode != 0:
        raise Mp4EncodingError(f"ffmpeg failed (code {proc.returncode}): {stderr}")
