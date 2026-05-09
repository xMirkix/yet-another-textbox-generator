from models.handler.entity_handler import EntityHandler
from services.selection_manager import SelectionManager

class CharacterHandler(EntityHandler):

    def grid_widget(self):
        return self.ui.characters_grid

    def db_delete(self, character):
        self.get_db().delete_universe(character.character_id, character.order_position) # TODO

    def db_select_by_order(self, pos):
        return self.get_db().select_universe_by_order_position(pos) # TODO

    def db_update_order(self, character, new_pos):
        self.get_db().update_universe_order_position(character.character_id, new_pos)  # TODO

    def handle_edit(self, character):
        from running.connection.characters import on_edit
        on_edit(self.ui, character)

    def delete_message(self, character) -> str:
        return (f"Delete character '{character.character_name}'?\n\n"
                f"This will delete all associated expressions.")

    def update_selection_manager(self, character):
        SelectionManager.set_selected_character(character)

    def clear_selection_manager(self):
        SelectionManager.set_selected_character(None)
        SelectionManager.set_selected_expression(None)

    def on_before_delete(self, character):
        # Cascade: selected expressions belonged to character
        char = SelectionManager.get_selected_character()
        if char and char.character_id == character.character_id:
            SelectionManager.set_selected_expression(None)

    def filter_text(self) -> str:
        return self.ui.characters_filter_input.text()

    def reload_filtered(self):
        from running.connection.characters import filter_characters
        filter_characters(self.ui, self.filter_text())