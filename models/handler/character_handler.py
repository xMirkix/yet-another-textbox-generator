from models.handler.entity_handler import EntityHandler
from services.selection_manager import left_manager


class CharacterHandler(EntityHandler):

    def grid_widget(self):
        return self.ui.characters_grid

    def db_delete(self, character):
        self.get_db().delete_character(character.character_id, character.universe_id, character.order_position)

    def db_select_by_order(self, entity, new_pos: int):
        return self.get_db().select_character_by_order_position(entity.universe_id, new_pos)

    def db_update_order(self, character, new_pos):
        self.get_db().update_character_order_position(character.character_id, new_pos)

    def handle_edit(self, character):
        from running.connection.characters import on_edit
        on_edit(self.ui, character)

    def delete_message(self, character) -> str:
        return (f"Delete character '{character.character_name}'?\n\n"
                f"This will delete all associated expressions.")

    def update_selection_manager(self, character):
        left_manager.set_selected_character(character)
        left_manager.try_to_select_first_expression_from_current_character()

    def clear_selection_manager(self):
        left_manager.set_selected_character(None)
        left_manager.set_selected_expression(None)

    def on_before_delete(self, character):
        # Cascade: selected expressions belonged to character
        char = left_manager.get_selected_character()
        universe = left_manager.get_selected_universe()
        if char and char.character_id == character.character_id:
            left_manager.set_selected_expression(None)

        db = self.get_db()

        if universe is None: # Safety check, should never happen
            self.ui.export_selected_character.setEnabled(False)
            self.ui.export_all_character.setEnabled(False)
            return

        if db.count_characters(universe.universe_id) == 1: # No character left after deletion, disable downloads
            self.ui.export_selected_character.setEnabled(False)
            self.ui.export_all_character.setEnabled(False)

    def filter_text(self) -> str:
        return self.ui.characters_filter_input.text()

    def reload_filtered(self):
        from running.connection.characters import filter_characters
        filter_characters(self.ui, self.filter_text())

    def get_selected_entity(self):
        return left_manager.get_selected_character()