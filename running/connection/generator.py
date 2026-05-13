from services.database_service import DBDynamicConnection
from services.selection_manager import SelectionManager, init_entity
from ui.generated_ui import Ui_MainWindow

def connect_generator(ui: Ui_MainWindow):
    pass

"""
1. Wipe universe/character/expression selector
2. Load universes into select (sorted)
Universes, characters and expressions are added dynamically
"""
def reload_ui(ui: Ui_MainWindow):
    ui.expression_selector.clear()
    ui.expression_preview.clear()
    ui.character_selector.clear()
    ui.character_preview.clear()
    ui.universe_selector.clear()
    ui.universe_preview.clear() # Wipe existing items in case of changes

    db = get_db()

    empty = init_entity(db.select_all_universes, ui.universe_selector, ui.universe_preview, SelectionManager.get_selected_universe())

    if empty:
        return

    empty = init_entity(lambda: db.select_all_characters_from_universe(ui.universe_selector.currentData()), ui.character_selector, ui.character_preview, SelectionManager.get_selected_character())

    if empty:
        return

    init_entity(lambda: db.select_all_expressions_from_character(ui.character_selector.currentData()), ui.expression_selector, ui.expression_preview, SelectionManager.get_selected_expression())

def get_db():
    return DBDynamicConnection.get_instance()