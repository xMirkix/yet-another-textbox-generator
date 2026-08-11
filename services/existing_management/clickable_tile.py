from PySide6.QtWidgets import QGroupBox
from PySide6.QtCore import Signal

from models.tile_config import TileConfig


class ClickableTile(QGroupBox):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.btn_left   = None
        self.btn_right  = None
        self.btn_edit   = None
        self.btn_delete = None

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

    def set_config(self, config: TileConfig):
        self.btn_left.clicked.connect(lambda: config.on_move(-1))
        self.btn_right.clicked.connect(lambda: config.on_move(+1))
        self.btn_edit.clicked.connect(config.on_edit)
        self.btn_delete.clicked.connect(config.on_delete)
        self.clicked.connect(config.on_select)


class ClickableTileSimple(QGroupBox):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

    def set_config(self, config: TileConfig):
        self.clicked.connect(config.on_select)