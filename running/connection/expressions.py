from PySide6.QtWidgets import QGroupBox

from models.entities import Expression
from services.database_service import DBDynamicConnection
from ui.generated_ui import Ui_MainWindow


def connect_expressions(ui: Ui_MainWindow):
    pass

def on_move(ui: Ui_MainWindow, character: Expression, direction: int):
    pass

def on_edit(ui: Ui_MainWindow, character: Expression):
    pass

def on_select(ui: Ui_MainWindow, character: Expression, tile: QGroupBox):
    pass

def on_delete(ui: Ui_MainWindow, character: Expression, tile: QGroupBox):
    pass

"""
1. hide edit like initial
2. Wipe characters
3. Wipe universes
4. Load universes into select (sorted)
2. clear filter
"""
def reload_ui(ui: Ui_MainWindow):
    ui.edit_expression.hide()
    ui.expressions_create_character_selector.clear()
    ui.expressions_create_universe_selector.clear()

    universes_list = get_db().select_all_universes()
    universes_list.sort(key=lambda universe: universe.order_position)
    for u in universes_list: # Get universes
        ui.expressions_create_universe_selector.addItem(u.universe_name)

    ui.expressions_filter_input.clear()


def get_db():
    return DBDynamicConnection.get_instance()