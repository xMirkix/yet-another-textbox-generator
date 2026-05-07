from services.database_service import DBDynamicConnection
from ui.generated_ui import Ui_MainWindow


def connect_expressions(ui: Ui_MainWindow):
    pass

"""
1. hide edit like initial
2. Wipe characters
3. Wipe universes
4. Load universes into select (sorted)
2. clear filter
"""
def on_tab_change(ui: Ui_MainWindow):
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