from static.database_service import DBDynamicConnection
from ui.generated_ui import Ui_MainWindow


def connect_characters(ui: Ui_MainWindow):
    pass

"""
1. hide edit like initial
2. Wipe universes
3. Load universes into select (sorted)
4. clear filter
"""
def on_tab_change(ui: Ui_MainWindow):
    ui.edit_character.hide()
    ui.characters_create_universe_selector.clear() # Wipe universes

    universes_list = get_db().select_all_universes()
    universes_list.sort(key=lambda universe: universe.order_position)
    for u in universes_list: # Get universes
        ui.characters_create_universe_selector.addItem(u.universe_name)

    ui.characters_filter_input.clear()

def get_db():
    return DBDynamicConnection.get_instance()