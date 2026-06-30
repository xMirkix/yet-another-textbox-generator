import io
import struct
from pathlib import Path

from PIL import Image

TRANSPARENT_IDX = 255


def _encode_single_frame(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, format='GIF')
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
            if ext_type == 0xF9:  # Graphic Control Extension gefunden
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

        gce_packed = 0x05 if has_trans else 0x04

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