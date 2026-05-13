from typing import Callable

from PySide6.QtWidgets import QLabel, QComboBox

from models.entities import Universe, Character, Expression
from services import change_service
from services.database_service import DBDynamicConnection
from services.selection_manager import SelectionManager
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

    is_universe_selected = load_entities(db.select_all_universes, SelectionManager.get_selected_universe(), ui.universe_selector, ui.universe_preview)

    if not is_universe_selected:
        return

    universe = ui.universe_selector.currentData()

    is_character_selected = load_entities(lambda: db.select_all_characters_from_universe(universe.universe_id), universe, ui.character_selector, ui.character_preview)

    if not is_character_selected:
        return

    character = ui.character_selector.currentData()

    load_entities(lambda: db.select_all_expressions_from_character(character.character_id), character, ui.expression_selector, ui.expression_preview)


def load_entities(db_list_function: Callable, selected: Universe | Character | Expression | None, selector: QComboBox, preview: QLabel) -> bool:
    entity_list = db_list_function()
    if len(entity_list) == 0:
        return False

    for entity in entity_list:  # Sets entity in selector
       selector.addItem(entity.get_name(), userData=entity)

    if not selected:
        set_preview(entity_list[0].preview_image, preview)
        return True

    index = find_by_id(selector, selected.get_id())

    if index == -1:  # Should never be reached, but just in case
        set_preview(entity_list[0].preview_image, preview)
        return True

    selector.setCurrentIndex(index)  # Set selected entity

    set_preview(entity_list[index].preview_image, preview)  # Set preview of selected entity
    return True

def set_preview(preview_object: str | None, preview_ui: QLabel): # Sets universe preview image to first universe
    if not preview_object:
        preview_ui.setText("Nothing...")
        return
    preview_ui.setPixmap(change_service.base64_to_pixmap(preview_object))

def find_by_id(combo_box, search_id):
    for i in range(combo_box.count()):
        obj: Universe | Character | Expression = combo_box.itemData(i)
        if obj.get_id() == search_id:
            return i
    return -1

def get_db():
    return DBDynamicConnection.get_instance()