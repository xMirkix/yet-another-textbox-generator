from dataclasses import dataclass

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QDialog, QFrame, QSizePolicy, QHBoxLayout, QCheckBox, QVBoxLayout, QLabel

from running.connection.resizing import GridReflowFilter2
from services.grid_service import clear_grid
from startup.in_memory.static_classes import Color
from ui.color_ui import Ui_Dialog
from ui.generated_ui import Ui_MainWindow


@dataclass
class ColorEntry:
    position: int
    color: Color
    included: bool = True

TILES_PER_ROW = 5

class ColorPickerDialog(QDialog):
    def __init__(self, selected_colors: tuple[Color], excluded: tuple[Color], simple_recoloring: bool, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.simple_recoloring.setChecked(simple_recoloring)
        self.simple = simple_recoloring
        self.colors: list[ColorEntry] = []
        self.tiles: list[QFrame] = []

        self.ui.scrollAreaWidgetContents.reflow_filter = GridReflowFilter2(self.ui.scrollAreaWidgetContents)

        i = 0
        for c in selected_colors:
            self.colors.append(ColorEntry(i, c))
            i += 1

        i = 0
        for c in excluded:
            self.colors.append(ColorEntry(i, c, False))
            i += 1

        self.setWindowTitle("Configure Colors")

        self.ui.select_all.clicked.connect(self._select_all)
        self.ui.invert_selection.clicked.connect(self._invert_selection)

        def set_simple():
            self.simple = not self.simple

        self.ui.simple_recoloring.clicked.connect(lambda: set_simple())

        self.ui.ok_button.clicked.connect(lambda: self.accept())
        self.ui.cancel_button.clicked.connect(lambda: self.reject())

        self._populate_grid(self.colors)

    def _populate_grid(self, colors: list[ColorEntry]):
        grid = self.ui.scrollAreaWidgetContents
        clear_grid(grid)
        self.tiles.clear()

        layout = self.ui.gridLayout_2
        for idx, entry in enumerate(colors):
            tile = create_tile(entry)
            row, col = divmod(idx, TILES_PER_ROW)
            layout.addWidget(tile, row, col)
            self.tiles.append(tile)

    def _select_all(self):
        for tile in self.tiles:
            tile.checkbox.setChecked(True)

    def _invert_selection(self):
        for tile in self.tiles:
            tile.checkbox.setChecked(not tile.checkbox.isChecked())


def create_color_window(ui: Ui_MainWindow, included: tuple[Color], excluded: tuple[Color], simple_recoloring: bool) -> tuple[list[Color], list[Color], bool]:
    parent_window = ui.centralwidget.window()

    dialog = ColorPickerDialog(included, excluded, simple_recoloring, parent=parent_window)
    result = dialog.exec()

    if result == QDialog.DialogCode.Accepted:
        included_ret, excluded_ret = [], []
        for c in dialog.colors:
            if c.included:
                included_ret.append(c.color)
            else:
                excluded_ret.append(c.color)
        return included_ret, excluded_ret, dialog.simple

    return list(included), list(excluded), simple_recoloring



def create_tile(
    entry: ColorEntry,
) -> QFrame:
    tile = QFrame()
    tile.setObjectName(f"color_{entry.position}_tile")

    size_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    size_policy.setHeightForWidth(tile.sizePolicy().hasHeightForWidth())
    tile.setSizePolicy(size_policy)
    tile.setMinimumSize(QSize(130, 0))
    tile.setFrameShape(QFrame.Shape.Box)
    tile.setFrameShadow(QFrame.Shadow.Raised)
    tile.setLineWidth(1)

    layout = QHBoxLayout(tile)

    checkbox = QCheckBox(tile)
    checkbox.setObjectName(f"color_{entry.position}_checkbox")
    checkbox.setChecked(entry.included)
    layout.addWidget(checkbox)

    labels_layout = QVBoxLayout()
    r_label = QLabel(f"R: {entry.color.r}", tile)
    g_label = QLabel(f"G: {entry.color.g}", tile)
    b_label = QLabel(f"B: {entry.color.b}", tile)
    labels_layout.addWidget(r_label)
    labels_layout.addWidget(g_label)
    labels_layout.addWidget(b_label)
    layout.addLayout(labels_layout)

    preview = QLabel(tile)
    preview.setStyleSheet(
        f"background-color: rgb({entry.color.r}, {entry.color.g}, {entry.color.b})"
    )
    layout.addWidget(preview)

    def _on_toggled(checked: bool):
        entry.included = checked

    checkbox.toggled.connect(_on_toggled)

    tile.checkbox = checkbox
    tile.r_label = r_label
    tile.g_label = g_label
    tile.b_label = b_label
    tile.preview = preview
    tile.entry = entry

    return tile

