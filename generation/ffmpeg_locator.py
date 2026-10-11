import shutil


class FfmpegNotFoundError(Exception):
    pass


def get_ffmpeg_path() -> str:
    path = shutil.which("ffmpeg")
    if path is None:
        raise FfmpegNotFoundError(
            "ffmpeg isn't installed on this system."
            "Please install it from ffmpeg.org/download.html and make sure, that the output of: 'which ffmpeg' in the terminal application doesn't produce an error."
        )
    return path
