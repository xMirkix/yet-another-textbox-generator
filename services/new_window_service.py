from typing import Callable

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QDialog, QPushButton, QComboBox

from models.tile_config import TileConfig
from running.connection.resizing import GridReflowFilter
from services.database_service import DBDynamicConnection
from services.grid_service import clear_grid, restore_selection
from services.selection_manager import SelectionManager, select_chars, select_expr, select_entity_in_combo, \
    SideSelectors
from services.tile_service import Entity, insert_tile_simple
from ui.generated_ui import Ui_MainWindow
from ui.preview_ui import Ui_Dialog


class EntityPickerDialog(QDialog):
    def __init__(self, entities: list[Entity], parent=None, selected: int | None = None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Entity Picker")

        self.ui.entity_grid.reflow_filter = GridReflowFilter(self.ui.entity_grid)

        self.entities = entities
        self.selected_id: int | None = selected

        self.ui.filter_name_input.textChanged.connect(lambda: QTimer.singleShot(0, lambda: self._populate_grid(selected)))
        self._populate_grid(selected)

    def _populate_grid(self, selected: int | None = None):
        grid = self.ui.entity_grid

        clear_grid(grid)

        filter_text = self.ui.filter_name_input.text().lower()

        for entity in self.entities:
            if filter_text and filter_text not in entity.get_name().lower():
                continue

            config = TileConfig(
                on_select=lambda e=entity: self._select(e),
            )

            tile = insert_tile_simple(grid, entity)

            tile.set_config(config)

        if selected:
            restore_selection(grid, selected)

    def _select(self, entity: Entity):
        self.selected_id = entity.get_id()
        self.accept()



def create_preview_window(ui: Ui_MainWindow, entities: list[Entity], selected: Entity | None) -> Entity | None:
    parent_window = ui.centralwidget.window()

    selected_id = selected.get_id() if selected else None

    dialog = EntityPickerDialog(entities, parent=parent_window, selected=selected_id)
    result = dialog.exec()

    if result == QDialog.DialogCode.Accepted:
        return next(
            (e for e in entities if e.get_id() == dialog.selected_id),
            None
        )

    return None

def connect_universe_create(ui: Ui_MainWindow, button: QPushButton, man: SelectionManager, post_fn: Callable):
    db = get_db()
    def picker():
        universe = create_preview_window(
            ui,
            db.select_all_universes(),
            man.get_selected_universe(),
        )

        if universe is not None:
            post_fn(universe, man)

    button.clicked.connect(picker)

def connect_character_create(ui: Ui_MainWindow, button: QPushButton, man: SelectionManager, post_fn: Callable):
    def picker():
        character = create_preview_window(
            ui,
            select_chars(man.get_selected_universe()),
            man.get_selected_character()
        )

        if character is not None:
            post_fn(character, man)

    button.clicked.connect(picker)

def connect_expression_create(ui: Ui_MainWindow, button: QPushButton, man: SelectionManager, post_fn: Callable):
    def picker():
        expression = create_preview_window(
            ui,
            select_expr(man.get_selected_character()),
            man.get_selected_expression()
        )

        if expression is not None:
            post_fn(expression, man)

    button.clicked.connect(picker)

def connect_alt_expression(ui: Ui_MainWindow, button: QPushButton, man: SelectionManager, post_fn: Callable, sel_side: SideSelectors, selector: QComboBox):
    def picker():
        expression = create_preview_window(
            ui,
            select_expr(man.get_selected_character()),
            man.get_alternating_expression()
        )
        if expression is not None:
            post_fn(expression, man, sel_side, selector)
    button.clicked.connect(picker)

def connect_universe_edit(ui: Ui_MainWindow, button: QPushButton, selector: QComboBox, post_fn: Callable):
    db = get_db()
    def picker():
        universe = create_preview_window(
            ui,
            db.select_all_universes(),
            None
        )

        if universe is not None:
            select_entity_in_combo(selector, universe)
            post_fn()
    button.clicked.connect(picker)

def connect_character_edit(ui: Ui_MainWindow, button: QPushButton, selector: QComboBox):
    def picker():
        universe = ui.expressions_edit_universe_selector.currentData()
        character = create_preview_window(
            ui,
            select_chars(universe),
            None
        )

        if character is not None:
            select_entity_in_combo(selector, character)
    button.clicked.connect(picker)


def get_db():
    return DBDynamicConnection.get_instance()
