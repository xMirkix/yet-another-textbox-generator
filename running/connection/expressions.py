from typing import Callable

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QLineEdit, QLabel, QPushButton, QMessageBox

from models.entities import Expression, Universe
from models.handler.expression_handler import ExpressionHandler
from running.connection.resizing import GridReflowFilter
from services import change_service
from services.change_service import select_image, remove_image
from services.database_service import DBDynamicConnection
from services.grid_service import clear_grid, restore_selection
from services.selection_manager import init_entity, left_manager
from ui.generated_ui import Ui_MainWindow


def connect_expressions(ui: Ui_MainWindow):
    ui.expressions_grid.reflow_filter = GridReflowFilter(ui.expressions_grid)

    create = ui.expressions_create_confirm_button
    edit = ui.expressions_edit_confirm_button

    create_image = ui.expressions_create_image_button
    create_image_remove = ui.expressions_create_image_remove_button
    create_image_preview = ui.expressions_create_image_preview

    edit_image = ui.expressions_edit_image_button
    edit_image_remove = ui.expressions_edit_image_remove_button
    edit_image_preview = ui.expressions_edit_image_preview

    create_image.clicked.connect(
        lambda: select_image(create_image_preview, create_image_remove, width=67,
                             height=70))  # On creation image selection

    edit_image.clicked.connect(
        lambda: select_image(edit_image_preview, edit_image_remove, width=67, height=70))  # On edit image selection

    create_image_remove.clicked.connect(
        lambda: remove_image(create_image_preview, create_image_remove))  # On creation image removal

    edit_image_remove.clicked.connect(
        lambda: remove_image(edit_image_preview, edit_image_remove))  # On edit image removal

    create.clicked.connect(lambda: create_expression(ui))  # On creation

    edit.clicked.connect(lambda: edit_expression(ui))  # On edit

    ui.expressions_filter_input.textChanged.connect(lambda text: QTimer.singleShot(0, lambda: filter_expressions(ui, text)))  # On filter change

    ui.expressions_create_universe_selector.activated.connect(
        lambda: universe_change(ui)
    )

    ui.expressions_create_character_selector.activated.connect(
        lambda index: character_change(ui, index)
    )

def universe_change(ui: Ui_MainWindow):
    ui.edit_expression.hide()
    new_universe : Universe = ui.expressions_create_universe_selector.currentData()
    left_manager.set_selected_universe(new_universe)
    left_manager.try_to_select_first_character_from_current_universe()
    QTimer.singleShot(0, lambda: reload_ui(ui))

def character_change(ui: Ui_MainWindow, index):
    ui.edit_expression.hide()
    left_manager.set_selected_character(
        ui.expressions_create_character_selector.itemData(index))
    QTimer.singleShot(0, lambda: reload_ui(ui))

def create_expression(ui: Ui_MainWindow):
    db = get_db()

    expression_name = ui.expressions_create_name_input.text()

    character = left_manager.get_selected_character()

    if not character:
        QMessageBox.warning(ui.centralwidget, "Invalid Character", "No selected Character")
        return

    character_id = character.character_id

    pixmap = ui.expressions_create_image_preview.pixmap()

    order_position = db.count_expressions(character_id) + 1

    form_operation(ui, -1, expression_name, character_id, pixmap,
                   order_position, db.insert_expression)

    post_operation(
        ui.expressions_create_name_input,
        ui.expressions_create_image_preview,
        ui.expressions_create_image_remove_button,
        lambda: QTimer.singleShot(0, lambda: reload_ui(ui)),
    )

def edit_expression(ui: Ui_MainWindow):
    expression_id = ui.expressions_edit_confirm_button.property("expression_id")
    expression_name = ui.expressions_edit_name_input.text()
    pixmap = ui.expressions_edit_image_preview.pixmap()
    character_id = ui.expressions_edit_character_selector.currentData().character_id

    db = get_db()

    exists = db.select_expression_by_id(expression_id)

    if not exists:
        post_operation(
            ui.expressions_edit_name_input,
            ui.expressions_edit_image_preview,
            ui.expressions_edit_image_remove_button,
            lambda: QTimer.singleShot(0, lambda: reload_ui(ui))
        )
        return

    form_operation(ui, expression_id, expression_name, character_id, pixmap, 42,
                   db.update_expression)  # Order position is not changed on update and thus not considered, 42 is the answer to the question of live

    left_manager.set_selected_expression(db.select_expression_by_id(expression_id))

    post_operation(
        ui.expressions_edit_name_input,
        ui.expressions_edit_image_preview,
        ui.expressions_edit_image_remove_button,
        lambda: QTimer.singleShot(0, lambda: reload_ui(ui))  # For edit to take effect
    )

def form_operation(ui: Ui_MainWindow, expression_id: int, name: str, character_id: int, pixmap, order_position: int, db_function: Callable):
    if not name:
        QMessageBox.warning(ui.centralwidget, "Invalid Name", "Name cannot be empty")
        return

    if character_id is None:
        QMessageBox.warning(ui.centralwidget, "Invalid Character", "Expression must belong to a character")
        return

    if pixmap is None or pixmap.isNull():
        QMessageBox.warning(ui.centralwidget, "Invalid Image", "Expression must have an image")
        return

    pixmap = change_service.pixmap_to_blob(pixmap)

    expression = Expression(expression_id=expression_id,
                          expression_name=name,
                          character_id=character_id,
                          preview_image=pixmap,
                          order_position=order_position)
    db_function(expression)

def post_operation(input_to_clear: QLineEdit, pixmap_to_clear: QLabel, remove_button: QPushButton, post_function: Callable):
    input_to_clear.clear() # Clear input
    remove_image(pixmap_to_clear, remove_button)
    post_function()

def filter_expressions(ui: Ui_MainWindow, filter_text: str):
    clear_grid(ui.expressions_grid)
    character = left_manager.get_selected_character()

    if character is None:
        return

    for expression in get_db().select_filtered_expressions(character.character_id, filter_text):
        insert_expression_tile(ui, expression)

    selected = left_manager.get_selected_expression()

    if selected:
        restore_selection(ui.expressions_grid, selected.get_id())

def on_edit(ui: Ui_MainWindow, expression: Expression):
    ui.expressions_edit_name_input.setText(expression.expression_name)

    ui.expressions_edit_universe_selector.setCurrentIndex(ui.expressions_create_universe_selector.currentIndex())

    ui.expressions_edit_character_selector.setCurrentIndex(ui.expressions_create_character_selector.currentIndex())

    ui.expressions_edit_image_preview.setPixmap(change_service.blob_to_pixmap(expression.preview_image))
    ui.expressions_edit_image_remove_button.show()

    ui.expressions_edit_confirm_button.setProperty("expression_id", expression.expression_id)
    ui.edit_expression.show()

"""
1. hide edit like initial
2. Wipe characters
3. Wipe universes
4. Load universes into select (sorted)
2. clear filter
"""
def reload_ui(ui: Ui_MainWindow):
    ui.edit_expression.hide()
    ui.expressions_create_character_selector.clear()
    ui.expressions_create_universe_selector.clear()
    ui.expressions_edit_character_selector.clear()
    ui.expressions_edit_universe_selector.clear()
    ui.expressions_filter_input.clear()
    clear_grid(ui.expressions_grid)

    universe = left_manager.get_selected_universe()
    if universe is None:
        return

    init_entity(get_db().select_all_universes, ui.expressions_create_universe_selector, None, universe)
    init_entity(get_db().select_all_universes, ui.expressions_edit_universe_selector, None, universe)

    character = left_manager.get_selected_character()
    if character is None:
        return

    init_entity(lambda: get_db().select_all_characters_from_universe(universe.universe_id), ui.expressions_create_character_selector, None, character)
    init_entity(lambda: get_db().select_all_characters_from_universe(universe.universe_id), ui.expressions_edit_character_selector, None, character)

    for expression in get_db().select_all_expressions_from_character(character.character_id):
        insert_expression_tile(ui, expression)

    selected = left_manager.get_selected_expression()

    restore_selection(ui.expressions_grid, selected.get_id() if selected else None) or ExpressionHandler(
        ui).select_first_or_none()

def insert_expression_tile(ui: Ui_MainWindow, expression: Expression):
    ExpressionHandler(ui).insert_entity_tile(expression)

def get_db():
    return DBDynamicConnection.get_instance()