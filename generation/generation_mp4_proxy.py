from pathlib import Path
from collections import OrderedDict

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QMessageBox

from generation.generation_gif_proxy import generate_gif
from generation.generation_request import GenerationRequest
from configs.paths import TEMP_DATA_DIR
from generation.gif_save_logic import save_mp4


CACHE_SIZE = 10

def show_ffmpeg_missing_dialog():
    box = QMessageBox()
    box.setIcon(QMessageBox.Icon.Warning)
    box.setWindowTitle("ffmpeg not found")
    box.setText(
        "In order to generate videos, ffmpeg must be installed on this system."
    )
    box.setInformativeText(
        "Please install ffmpeg and restart the app afterwards."
    )

    open_button = box.addButton(
        "Direct download link",
        QMessageBox.ButtonRole.ActionRole,
    )
    box.addButton(QMessageBox.StandardButton.Close)

    box.exec()

    if box.clickedButton() is open_button:
        QDesktopServices.openUrl(
            QUrl("https://ffmpeg.org/download.html")
        )

class GenerationMp4Proxy:
    cache: OrderedDict[GenerationRequest, Path] = OrderedDict()
    slot: int = 0

    def generate(self, request: GenerationRequest) -> Path | None:
        if request in self.cache:
            return self.cache[request]

        frames, positions = generate_gif(request)

        if not frames:
            return None

        path = TEMP_DATA_DIR / f"output_{self.slot}.mp4"
        audio_settings = request.export_settings.audio_settings
        save_mp4(frames, 1000 / 30, positions, audio_settings, path)

        self.slot = (self.slot + 1) % CACHE_SIZE
        self.cache[request] = path
        if len(self.cache) > CACHE_SIZE:
            self.cache.popitem(last=False)

        return path
