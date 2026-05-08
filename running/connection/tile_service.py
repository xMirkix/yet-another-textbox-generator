import PySide6
from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from configs.paths import ICON_LEFT, ICON_RIGHT, ICON_EDIT, ICON_DELETE
from models.entities import Universe, Character, Expression
from running.connection import universes, characters, expressions
from services import change_service
from ui.generated_ui import Ui_MainWindow

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


def _get_id(entity: Entity) -> int:
    if isinstance(entity, Universe): return entity.universe_id
    if isinstance(entity, Character): return entity.character_id
    if isinstance(entity, Expression): return entity.expression_id
    return -1

def create_tile(ui: Ui_MainWindow, parent, entity: Entity) -> QGroupBox:
    tile = QGroupBox(parent)
    tile.setProperty("entity_id", _get_id(entity))
    tile.setProperty("entity", entity)
    tile.setMinimumSize(QSize(250, 200))
    tile.setMaximumSize(QSize(250, 200))
    layout = QVBoxLayout(tile)

    preview = QLabel(tile)
    preview.setMinimumSize(QSize(230, 100))  # entire with of tile
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

    btn_left.clicked.connect(lambda: on_move(ui, entity, -1))
    btn_right.clicked.connect(lambda: on_move(ui, entity, +1))
    btn_edit.clicked.connect(lambda: on_edit(ui, entity))
    btn_delete.clicked.connect(lambda: on_delete(entity, tile))

    return tile


def insert_tile(ui: Ui_MainWindow, grid_widget, entity: Entity, tile_width: int = 250, spacing: int = 10):
    tile = create_tile(ui, grid_widget, entity)
    cols = max(1, grid_widget.width() // (tile_width + spacing))
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


def on_move(ui: Ui_MainWindow, entity: Entity, direction: int):
    if isinstance(entity, Universe):
        universes.on_move(ui, entity, direction)
    if isinstance(entity, Character):
        characters.on_move(ui, entity, direction)
    if isinstance(entity, Expression):
        expressions.on_move(ui, entity, direction)

def on_edit(ui: Ui_MainWindow, entity: Entity):
    if isinstance(entity, Universe):
        universes.on_edit(ui, entity)
    if isinstance(entity, Character):
        characters.on_edit(ui, entity)
    if isinstance(entity, Expression):
        expressions.on_edit(ui, entity)

def on_delete(entity: Entity, tile: QGroupBox):
    if isinstance(entity, Universe):
        universes.on_delete(entity, tile)
    if isinstance(entity, Character):
        characters.on_delete(entity, tile)
    if isinstance(entity, Expression):
        expressions.on_delete(entity, tile)