from PySide6.QtWidgets import QGroupBox
from PySide6.QtCore import Signal

class ClickableTile(QGroupBox):
    clicked = Signal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)