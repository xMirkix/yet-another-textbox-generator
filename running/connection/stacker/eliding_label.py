from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFontMetrics
from PySide6.QtWidgets import QLabel, QSizePolicy


class ElidingLabel(QLabel):
    def __init__(self, text: str = "", parent=None):
        super().__init__(parent)
        self._full_text = text
        self.setWordWrap(False)
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        self.setMinimumWidth(0)
        self._update_elided_text()

    def setFullText(self, text: str):
        self._full_text = text
        self._update_elided_text()

    def _update_elided_text(self):
        metrics = QFontMetrics(self.font())
        lines = self._full_text.split("\n")
        elided_lines = [
            metrics.elidedText(line, Qt.TextElideMode.ElideRight, self.width())
            for line in lines
        ]
        super().setText("\n".join(elided_lines))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_elided_text()

    def setFont(self, font):
        super().setFont(font)
        self._update_elided_text()