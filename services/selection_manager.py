from dataclasses import dataclass, field
from typing import Callable

from PySide6.QtWidgets import QComboBox, QLabel, QCheckBox, QWidget

from models.entities import Universe, Character, Expression
from services import change_service
from services.database_service import DBDynamicConnection


class SelectionManager:
    def __init__(self):
        self.selected_universe: Universe | None = None
        self.selected_character: Character | None = None
        self.selected_expression: Expression | None = None
        self.selected_alternating: Expression | None = None

    def reset(self):
        self.selected_universe = None
        self.selected_character = None
        self.selected_expression = None
        self.selected_alternating = None

    def set_selected_universe(self, universe: Universe | None):
        self.selected_universe = universe

    def set_selected_character(self, character: Character | None):
        self.selected_character = character

    def set_selected_expression(self, expression: Expression | None):
        self.selected_expression = expression

    def get_selected_universe(self) -> Universe | None:
        return self.selected_universe

    def get_selected_character(self) -> Character | None:
        return self.selected_character

    def get_selected_expression(self) -> Expression | None:
        return self.selected_expression

    def get_alternating_expression(self) -> Expression | None:
        return self.selected_alternating

    def set_alternating_expression(self, expression: Expression | None):
        self.selected_alternating = expression

    def try_to_init_alternating_expression(self):
        if self.selected_expression:
            self.selected_alternating = self.selected_expression

    def try_to_select_first_universe_character_expression(self):
        db = get_db()
        universes = db.select_all_universes()
        if not universes:
            return
        self.set_selected_universe(universes[0])
        characters = db.select_all_characters_from_universe(universes[0].universe_id)
        if not characters:
            return
        self.set_selected_character(characters[0])
        expressions = db.select_all_expressions_from_character(characters[0].character_id)
        if not expressions:
            return
        self.set_selected_expression(expressions[0])

    def try_to_select_first_character_from_current_universe(self):
        db = get_db()
        universe = self.get_selected_universe()
        if universe is None:
            return
        characters = db.select_all_characters_from_universe(universe.universe_id)
        if not characters:
            self.set_selected_character(None)
            self.set_selected_expression(None)
            return
        self.set_selected_character(characters[0])

    def try_to_select_first_expression_from_current_character(self):
        db = get_db()
        character = self.get_selected_character()
        if character is None:
            return
        expressions = db.select_all_expressions_from_character(character.character_id)
        if not expressions:
            return
        self.set_selected_expression(expressions[0])

    def check_if_selected_exist(self):
        db = get_db()
        if None in (self.selected_universe, self.selected_character,
                    self.selected_expression, self.selected_alternating):
            return

        if not db.universe_exists(self.selected_universe.universe_id):
            self.reset()
            return

        if not db.character_exists(self.selected_character.character_id):
            self.selected_character = None
            self.selected_expression = None
            self.selected_alternating = None
            self.try_to_select_first_character_from_current_universe()
            self.try_to_select_first_expression_from_current_character()
            return

        if not db.expression_exists(self.selected_expression.expression_id):
            self.selected_expression = None
            self.selected_alternating = None
            self.try_to_select_first_expression_from_current_character()
            self.try_to_init_alternating_expression()


@dataclass
class SideSelectors:
    universe_selector:         QComboBox
    universe_preview:          QLabel
    character_selector:        QComboBox
    character_preview:         QLabel
    expression_selector:       QComboBox
    expression_preview:        QLabel
    alternating_selector:      QComboBox
    alternating_preview:       QLabel
    include_checkbox:          QCheckBox
    expression_color_selector: QComboBox
    expression_color_preview:  QLabel
    alternating_container:     QWidget
    alternating_lines:         list[QWidget]


left_manager  = SelectionManager()
right_manager = SelectionManager()


def init_entity(db_function: Callable, selector: QComboBox, preview: QLabel | None, selected: Universe | Character | Expression | None) -> bool:
    any_entity_exists = load_entities(db_function, selector)

    if not any_entity_exists:
        return False

    override_with_selected_if_exists(selector, selected)

    entity = selector.currentData()

    if preview is not None:
        set_preview(entity.preview_image, preview, entity)

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

def set_preview(preview_object: bytes | None, preview_ui: QLabel, entity: Universe | Character | Expression): # Sets universe preview image to first universe
    if not preview_object:
        preview_ui.setText(entity.get_name())
        return
    preview_ui.setPixmap(change_service.blob_to_pixmap(preview_object))

def find_by_id(combo_box, search_id):
    for i in range(combo_box.count()):
        obj: Universe | Character | Expression = combo_box.itemData(i)
        if obj.get_id() == search_id:
            return i
    return -1

def get_db():
    return DBDynamicConnection.get_instance()