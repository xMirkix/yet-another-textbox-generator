from pathlib import Path

from PySide6.QtCore import QObject, QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer, QVideoFrame, QVideoSink
from PySide6.QtWidgets import QLabel


class OutputVideoPlayer(QObject):
    def __init__(self, label: QLabel):
        super().__init__(label)
        self.label = label
        self.player = QMediaPlayer(self)
        self.available = self.player.isAvailable()
        if not self.available:
            return
        self.audio = QAudioOutput(self)
        self.sink = QVideoSink(self)
        self.player.setAudioOutput(self.audio)
        self.player.setVideoSink(self.sink)
        self.player.setLoops(QMediaPlayer.Loops.Infinite)
        self.sink.videoFrameChanged.connect(self._on_frame)

    def _on_frame(self, frame: QVideoFrame):
        if frame.isValid():
            image = frame.toImage()
            if not image.isNull():
                self.label.setPixmap(QPixmap.fromImage(image))

    def play_file(self, path: Path) -> bool:
        if not self.available:
            return False
        self.player.stop()
        self.player.setSource(QUrl.fromLocalFile(str(path)))
        self.player.play()
        return True

    def stop(self):
        self.player.stop()
        self.player.setSource(QUrl())
