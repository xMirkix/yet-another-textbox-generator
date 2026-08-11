from models.handler.entity_handler import EntityHandler
from services.selection_manager import left_manager


class ExpressionHandler(EntityHandler):

    def grid_widget(self):
        return self.ui.expressions_grid

    def db_delete(self, expression):
        self.get_db().delete_expression(expression.expression_id, expression.character_id, expression.order_position)

    def on_before_delete(self, entity):
        # Would normally do nothing since nothing depends on it, but the check for exporting is convenient here
        db = self.get_db()

        universe = left_manager.get_selected_universe()
        character = left_manager.get_selected_character()

        if universe is None or character is None: # Safety check, should never happen
            self.ui.export_selected_expression.setEnabled(False)
            self.ui.export_all_expression.setEnabled(False)
            return

        if db.count_expressions(character.character_id) == 1: # No expression left after deletion, disable downloads
            self.ui.export_selected_expression.setEnabled(False)
            self.ui.export_all_expression.setEnabled(False)

    def db_select_by_order(self, entity, new_pos: int):
        return self.get_db().select_expression_by_order_position(entity.character_id, new_pos)

    def db_update_order(self, expression, new_pos):
        self.get_db().update_expression_order_position(expression.expression_id, new_pos)

    def handle_edit(self, expression):
        from running.connection.expressions import on_edit
        on_edit(self.ui, expression)

    def delete_message(self, expression) -> str:
        return (f"Delete expression '{expression.expression_name}'?\n\n"
                f"This action cannot be undone.")

    def update_selection_manager(self, expression):
        left_manager.set_selected_expression(expression)

    def clear_selection_manager(self):
        left_manager.set_selected_expression(None)

    def filter_text(self) -> str:
        return self.ui.expressions_filter_input.text()

    def reload_filtered(self):
        from running.connection.expressions import filter_expressions
        filter_expressions(self.ui, self.filter_text())

    def get_selected_entity(self):
        return left_manager.get_selected_expression()