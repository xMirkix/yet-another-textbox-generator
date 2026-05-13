import PySide6
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from configs.paths import ICON_LEFT, ICON_RIGHT, ICON_EDIT, ICON_DELETE
from models.entities import Universe, Character, Expression
from services.existing_management.clickable_tile import ClickableTile
from services import change_service
from models.tile_config import TileConfig

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

def create_tile(parent, entity: Entity, config: TileConfig) -> ClickableTile:
    tile = ClickableTile(parent)
    tile.setProperty("entity_id", entity.get_id())
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
        preview.setText(entity.get_name())
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
    tile.btn_left = QPushButton(icons['left'], "", tile)
    tile.btn_right = QPushButton(icons['right'], "", tile)
    tile.btn_edit = QPushButton(icons['edit'], "", tile)
    tile.btn_delete = QPushButton(icons['delete'], "", tile)
    for btn in [tile.btn_left, tile.btn_right, tile.btn_edit, tile.btn_delete]:
        button_row.addWidget(btn)
    layout.addLayout(button_row)

    return tile


def insert_tile(grid_widget, entity: Entity, config: TileConfig, tile_width: int = 250, spacing: int = 10):
    tile = create_tile(grid_widget, entity, config)
    cols = max(1, grid_widget.width() // (tile_width + spacing))
    count = grid_widget.layout().count()
    grid_widget.layout().addWidget(tile, count // cols, count % cols)
    return tile


def _get_name(entity: Entity) -> str:
    if isinstance(entity, Universe):
        return entity.universe_name
    if isinstance(entity, Character):
        return entity.character_name
    if isinstance(entity, Expression):
        return entity.expression_name
    return ""