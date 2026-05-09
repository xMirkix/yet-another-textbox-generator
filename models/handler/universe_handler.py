from models.handler.entity_handler import EntityHandler
from services.selection_manager import SelectionManager

class UniverseHandler(EntityHandler):

    def grid_widget(self):
        return self.ui.universe_grid

    def db_delete(self, universe):
        self.get_db().delete_universe(universe.universe_id, universe.order_position)

    def db_select_by_order(self, pos):
        return self.get_db().select_universe_by_order_position(pos)

    def db_update_order(self, universe, new_pos):
        self.get_db().update_universe_order_position(universe.universe_id, new_pos)

    def handle_edit(self, universe):
        from running.connection.universes import on_edit
        on_edit(self.ui, universe)

    def delete_message(self, universe) -> str:
        return (f"Delete universe '{universe.universe_name}'?\n\n"
                f"This will delete all characters and expressions in this universe.")

    def update_selection_manager(self, universe):
        SelectionManager.set_selected_universe(universe)

    def clear_selection_manager(self):
        SelectionManager.set_selected_universe(None)
        SelectionManager.set_selected_character(None)
        SelectionManager.set_selected_expression(None)

    def on_before_delete(self, universe):
        # Cascade: selected character/expression belonged to universe
        char = SelectionManager.get_selected_character()
        if char and char.universe_id == universe.universe_id:
            SelectionManager.set_selected_character(None)
            SelectionManager.set_selected_expression(None)

    def filter_text(self) -> str:
        return self.ui.universe_filter_input.text()

    def reload_filtered(self):
        from running.connection.universes import filter_universe
        filter_universe(self.ui, self.filter_text())