from typing import Callable

from PySide6.QtWidgets import QComboBox, QLabel

from models.entities import Universe, Character, Expression
from services import change_service


class SelectionManager:
    selected_universe: Universe | None = None
    selected_character: Character | None = None
    selected_expression: Expression | None = None

    @classmethod
    def reset(cls):
        cls.selected_universe = None
        cls.selected_character = None
        cls.selected_expression = None

    @classmethod
    def set_selected_universe(cls, universe: Universe | None):
        cls.selected_universe = universe

    @classmethod
    def set_selected_character(cls, character: Character | None):
        cls.selected_character = character

    @classmethod
    def set_selected_expression(cls, expression: Expression | None):
        cls.selected_expression = expression

    @classmethod
    def get_selected_universe(cls) -> Universe | None:
        return cls.selected_universe

    @classmethod
    def get_selected_character(cls) -> Character | None:
        return cls.selected_character

    @classmethod
    def get_selected_expression(cls) -> Expression | None:
        return cls.selected_expression

def init_entity(db_function: Callable, selector: QComboBox, preview: QLabel | None, selected: Universe | Character | Expression | None) -> bool:
    any_entity_exists = load_entities(db_function, selector)

    if not any_entity_exists:
        return False

    override_with_selected_if_exists(selector, selected)

    entity = selector.currentData()

    if preview is not None:
        set_preview(entity.preview_image, preview)

    return True

def load_entities(db_list_function: Callable, selector: QComboBox) -> bool:
    entity_list = db_list_function()
    if len(entity_list) == 0:
        return False

    for entity in entity_list:  # Sets entity in selector
       selector.addItem(entity.get_name(), userData=entity)

    return True

def override_with_selected_if_exists(selector: QComboBox, selected: Universe | Character | Expression | None):
    if not selected:
        return

    index = find_by_id(selector, selected.get_id())

    if index == -1:  # Should never be reached, but just in case
        return

    selector.setCurrentIndex(index)  # Set selected entity

def set_preview(preview_object: bytes | None, preview_ui: QLabel): # Sets universe preview image to first universe
    if not preview_object:
        preview_ui.setText("Nothing...")
        return
    preview_ui.setPixmap(change_service.blob_to_pixmap(preview_object))

def find_by_id(combo_box, search_id):
    for i in range(combo_box.count()):
        obj: Universe | Character | Expression = combo_box.itemData(i)
        if obj.get_id() == search_id:
            return i
    return -1