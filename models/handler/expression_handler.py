from models.handler.entity_handler import EntityHandler
from services.selection_manager import SelectionManager

class ExpressionHandler(EntityHandler):

    def grid_widget(self):
        return self.ui.expressions_grid

    def db_delete(self, expression):
        self.get_db().delete_universe(expression.expression_id, expression.order_position) # TODO

    def db_select_by_order(self, pos):
        return self.get_db().select_universe_by_order_position(pos) # TODO

    def db_update_order(self, expression, new_pos):
        self.get_db().update_universe_order_position(expression.expression_id, new_pos) # TODO

    def handle_edit(self, expression):
        from running.connection.expressions import on_edit
        on_edit(self.ui, expression)

    def delete_message(self, expression) -> str:
        return (f"Delete expression '{expression.expression_name}'?\n\n"
                f"This action cannot be undone.")

    def update_selection_manager(self, expression):
        SelectionManager.set_selected_expression(expression)

    def clear_selection_manager(self):
        SelectionManager.set_selected_expression(None)

    #def on_before_delete(self, character): Not overridden because no cascading type and deletion already covered
        #pass

    def filter_text(self) -> str:
        return self.ui.expressions_filter_input.text()

    def reload_filtered(self):
        from running.connection.expressions import filter_expressions
        filter_expressions(self.ui, self.filter_text())