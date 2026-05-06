import PySide6
from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from configs.paths import ICON_LEFT, ICON_RIGHT, ICON_EDIT, ICON_DELETE
from models.entities import Universe, Character, Expression
from static import change_service

_ICONS: dict | None = None

def get_icons() -> dict:
    global _ICONS
    if _ICONS is None:
        _ICONS = {
            'left':   QIcon(str(ICON_LEFT)),
            'right':  QIcon(str(ICON_RIGHT)),
            'edit':   QIcon(str(ICON_EDIT)),
            'delete': QIcon(str(ICON_DELETE)),
        }
    return _ICONS

type Entity = Universe | Character | Expression

def create_tile(parent, entity: Entity) -> QGroupBox:
    tile = QGroupBox(parent)
    tile.setMinimumSize(QSize(250, 200))
    tile.setMaximumSize(QSize(250, 200))
    layout = QVBoxLayout(tile)

    preview = QLabel(tile)
    preview.setMinimumSize(QSize(230, 100))  # volle Breite des Tiles
    preview.setMaximumSize(QSize(230, 100))
    preview.setAlignment(PySide6.QtCore.Qt.AlignmentFlag.AlignCenter)
    if entity.preview_image:
        preview.setPixmap(change_service.base64_to_pixmap(entity.preview_image))
    else:
        preview.setText("Nothing...")
    preview.setAutoFillBackground(True)
    palette = preview.palette()
    palette.setColor(preview.backgroundRole(), PySide6.QtGui.QColor("black"))
    preview.setPalette(palette)

    layout.addWidget(preview)

    name_label = QLabel(_get_name(entity), tile)
    name_label.setAlignment(PySide6.QtCore.Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(name_label)

    button_row = QHBoxLayout()
    icons = get_icons()
    btn_left = QPushButton(icons['left'], "", tile)
    btn_right = QPushButton(icons['right'], "", tile)
    btn_edit = QPushButton(icons['edit'], "", tile)
    btn_delete = QPushButton(icons['delete'], "", tile)
    for btn in [btn_left, btn_right, btn_edit, btn_delete]:
        button_row.addWidget(btn)
    layout.addLayout(button_row)

    btn_left.clicked.connect(lambda: on_move(entity, -1))
    btn_right.clicked.connect(lambda: on_move(entity, +1))
    btn_edit.clicked.connect(lambda: on_edit(entity))
    btn_delete.clicked.connect(lambda: on_delete(entity, tile))

    return tile


def insert_tile(grid_widget, entity: Entity, cols: int = 3):
    tile = create_tile(grid_widget, entity)
    count = grid_widget.layout().count()
    grid_widget.layout().addWidget(tile, count // cols, count % cols)


def _get_name(entity: Entity) -> str:
    if isinstance(entity, Universe):
        return entity.universe_name
    if isinstance(entity, Character):
        return entity.character_name
    if isinstance(entity, Expression):
        return entity.expression_name
    return ""


def on_move(entity: Entity, direction: int):
    pass

def on_edit(entity: Entity):
    pass

def on_delete(entity: Entity, tile: QGroupBox):
    pass