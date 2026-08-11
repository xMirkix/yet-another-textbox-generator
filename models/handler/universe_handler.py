from models.handler.entity_handler import EntityHandler
from services.selection_manager import left_manager

class UniverseHandler(EntityHandler):

    def grid_widget(self):
        return self.ui.universe_grid

    def db_delete(self, universe):
        self.get_db().delete_universe(universe.universe_id, universe.order_position)

    def db_select_by_order(self, entity, new_pos: int):
        return self.get_db().select_universe_by_order_position(new_pos)

    def db_update_order(self, universe, new_pos):
        self.get_db().update_universe_order_position(universe.universe_id, new_pos)

    def handle_edit(self, universe):
        from running.connection.universes import on_edit
        on_edit(self.ui, universe)

    def delete_message(self, universe) -> str:
        return (f"Delete universe '{universe.universe_name}'?\n\n"
                f"This will delete all characters and expressions in this universe.")

    def update_selection_manager(self, universe):
        left_manager.set_selected_universe(universe)
        left_manager.try_to_select_first_character_from_current_universe()

    def clear_selection_manager(self):
        left_manager.set_selected_universe(None)
        left_manager.set_selected_character(None)
        left_manager.set_selected_expression(None)

    def on_before_delete(self, universe):
        # Cascade: selected character/expression belonged to universe
        char = left_manager.get_selected_character()
        if char and char.universe_id == universe.universe_id:
            left_manager.set_selected_character(None)
            left_manager.set_selected_expression(None)

        # Disable Export All/Selected buttons if necessary
        db = self.get_db()

        if db.count_universes() == 1: # No universe left after deletion, disable downloads
            self.ui.export_selected_universe.setEnabled(False)
            self.ui.export_all_universe.setEnabled(False)

    def filter_text(self) -> str:
        return self.ui.universe_filter_input.text()

    def reload_filtered(self):
        from running.connection.universes import filter_universes
        filter_universes(self.ui, self.filter_text())

    def get_selected_entity(self):
        return left_manager.get_selected_universe()