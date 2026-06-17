from typing import Callable

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox, QLineEdit, QLabel, QPushButton, QComboBox, QRadioButton

from models.entities import Character
from models.handler.character_handler import CharacterHandler
from running.connection.resizing import GridReflowFilter
from services import change_service
from services.change_service import select_image, remove_image
from services.database_service import DBDynamicConnection
from services.grid_service import clear_grid, restore_selection
from services.selection_manager import init_entity, SelectionManager
from ui.generated_ui import Ui_MainWindow


def connect_characters(ui: Ui_MainWindow):
    ui.characters_grid.reflow_filter = GridReflowFilter(ui.characters_grid)

    create = ui.characters_create_confirm_button
    edit = ui.characters_edit_confirm_button

    create_image = ui.characters_create_image_button
    create_image_remove = ui.characters_create_image_remove_button
    create_image_preview = ui.characters_create_image_preview

    edit_image = ui.characters_edit_image_button
    edit_image_remove = ui.characters_edit_image_remove_button
    edit_image_preview = ui.characters_edit_image_preview

    create_image.clicked.connect(
        lambda: select_image(create_image_preview, create_image_remove, width=230, height=100))  # On creation image selection

    edit_image.clicked.connect(lambda: select_image(edit_image_preview, edit_image_remove, width=230, height=100))  # On edit image selection

    create_image_remove.clicked.connect(
        lambda: remove_image(create_image_preview, create_image_remove))  # On creation image removal

    edit_image_remove.clicked.connect(
        lambda: remove_image(edit_image_preview, edit_image_remove))  # On edit image removal

    create.clicked.connect(lambda: create_character(ui))  # On creation

    edit.clicked.connect(lambda: edit_character(ui))  # On edit

    ui.characters_filter_input.textChanged.connect(lambda text: QTimer.singleShot(0, lambda: filter_characters(ui, text)))  # On filter change

    ui.characters_create_universe_selector.activated.connect(
        lambda index: universe_change(ui, index)
    )

def universe_change(ui: Ui_MainWindow, index):
    ui.edit_character.hide()
    SelectionManager.set_selected_universe(
        ui.characters_create_universe_selector.itemData(index))
    QTimer.singleShot(0, lambda: reload_ui(ui))

def create_character(ui: Ui_MainWindow):
    db = get_db()

    character_name = ui.characters_create_name_input.text()

    universe_id = ui.characters_create_universe_selector.currentData().universe_id

    default_style = get_default_style(ui.characters_create_style_regular_option)

    default_font = ui.characters_create_font_selector.currentData().font_id

    default_text_transform = ui.characters_create_transform_selector.currentData().transform_id

    pixmap = ui.characters_create_image_preview.pixmap()

    order_position = db.count_characters(universe_id) + 1


    form_operation(-1, character_name, universe_id, default_style, default_font, default_text_transform, pixmap, order_position, db.insert_character)

    post_operation(
        ui.characters_create_name_input,
        ui.characters_create_image_preview,
        ui.characters_create_image_remove_button,
        lambda: QTimer.singleShot(0, lambda: reload_ui(ui)),
    )

def get_default_style(regular_option: QPushButton):
    return 1 if regular_option.isChecked() else 2

def edit_character(ui: Ui_MainWindow):
    character_id = ui.characters_edit_confirm_button.property("character_id")
    character_name = ui.characters_edit_name_input.text()
    pixmap = ui.characters_edit_image_preview.pixmap()
    universe_id = ui.characters_edit_universe_selector.currentData().universe_id
    style = get_default_style(ui.characters_edit_style_regular_option)
    font = ui.characters_edit_font_selector.currentData().font_id
    transform = ui.characters_edit_transform_selector.currentData().transform_id

    db = get_db()

    exists = db.select_character_by_id(character_id)

    if not exists:
        post_operation(
            ui.characters_edit_name_input,
            ui.characters_edit_image_preview,
            ui.characters_edit_image_remove_button,
            lambda: QTimer.singleShot(0, lambda: reload_ui(ui))
        )
        return

    form_operation(character_id, character_name, universe_id, style, font, transform, pixmap, 42,
                   db.update_character)  # Order position is not changed on update and thus not considered, 42 is the answer to the question of live

    SelectionManager.set_selected_character(db.select_character_by_id(character_id))

    post_operation(
        ui.characters_edit_name_input,
        ui.characters_edit_image_preview,
        ui.characters_edit_image_remove_button,
        lambda: QTimer.singleShot(0, lambda: reload_ui(ui))  # For edit to take effect
    )

def form_operation(character_id: int, name: str, universe_id: int, default_style: int, default_font: int, default_text_transform: int, pixmap, order_position: int, db_function: Callable):
    if not name:
        QMessageBox.warning(None, "Invalid Name", "Name cannot be empty")
        return

    if universe_id is None:
        QMessageBox.warning(None, "Invalid Universe", "Character must belong to a universe")
        return

    pixmap = change_service.pixmap_to_blob(pixmap) if pixmap else None
    character = Character(character_id=character_id,
                          character_name=name,
                          universe_id=universe_id,
                          default_style=default_style,
                          default_font=default_font,
                          default_text_transform=default_text_transform,
                          preview_image=pixmap,
                          order_position=order_position)
    db_function(character)

def post_operation(input_to_clear: QLineEdit, pixmap_to_clear: QLabel, remove_button: QPushButton, post_function: Callable):
    input_to_clear.clear() # Clear input
    remove_image(pixmap_to_clear, remove_button)
    post_function()

def filter_characters(ui: Ui_MainWindow, filter_text: str):
    clear_grid(ui.characters_grid)
    universe = SelectionManager.get_selected_universe()

    if universe is None:
        return

    for character in get_db().select_filtered_characters(universe.universe_id, filter_text):
        insert_character_tile(ui, character)

    selected = SelectionManager.get_selected_character()

    if selected:
        restore_selection(ui.characters_grid, selected.get_id())

def on_edit(ui: Ui_MainWindow, character: Character):
    ui.characters_edit_name_input.setText(character.character_name)

    ui.characters_edit_universe_selector.setCurrentIndex(ui.characters_create_universe_selector.currentIndex())

    selected_font_index = get_character_font_index(character, ui.characters_create_font_selector)

    if selected_font_index == -1:
        selected_font_index = 0 # fallback to "Determination Mono", should always exist

    ui.characters_edit_font_selector.setCurrentIndex(selected_font_index)

    selected_transform_index = get_text_transform_index(character, ui.characters_create_transform_selector)

    if selected_transform_index == -1:
        selected_transform_index = 0 # fallback to "no changes"

    ui.characters_edit_transform_selector.setCurrentIndex(selected_transform_index)

    selected_default_style_index = get_default_style_index(character)

    if selected_default_style_index != -1:
        ui.characters_edit_style_regular_option.setChecked(selected_default_style_index == 1)
        ui.characters_edit_style_dark_world_option.setChecked(selected_default_style_index == 2)
    else: # no option selected, should not happen, just for null values
        uncheck_radio_group(
            ui.characters_edit_style_regular_option,
            ui.characters_edit_style_dark_world_option
        )


    if character.preview_image is not None:
        ui.characters_edit_image_preview.setPixmap(change_service.blob_to_pixmap(character.preview_image))
        ui.characters_edit_image_remove_button.show()
    else:
        ui.characters_edit_image_preview.clear()
        ui.characters_edit_image_preview.setText("Nothing...")
        ui.characters_edit_image_remove_button.hide()

    ui.characters_edit_confirm_button.setProperty("character_id", character.character_id)
    ui.edit_character.show()

def uncheck_radio_group(*buttons: QRadioButton):
    for btn in buttons:
        btn.setAutoExclusive(False)
        btn.setChecked(False)
        btn.setAutoExclusive(True)

def get_character_font_index(character: Character, edit_selector: QComboBox) -> int:
    for i in range(edit_selector.count()):
        if edit_selector.itemData(i).font_id == character.default_font:
            return i
    return -1

def get_text_transform_index(character: Character, edit_selector: QComboBox) -> int:
    for i in range(edit_selector.count()):
        if edit_selector.itemData(i).transform_id == character.default_text_transform:
            return i
    return -1

def get_default_style_index(character: Character) -> int:
    if character.default_style == 1:
        return 1
    if character.default_style == 2:
        return 2
    return -1

def reload_ui(ui: Ui_MainWindow):
    ui.edit_character.hide()
    ui.characters_create_universe_selector.clear() # Wipe universes
    ui.characters_edit_universe_selector.clear()
    ui.characters_filter_input.clear()

    universe = SelectionManager.get_selected_universe()

    if universe is None:
        return

    init_entity(get_db().select_all_universes, ui.characters_create_universe_selector, None, universe)
    init_entity(get_db().select_all_universes, ui.characters_edit_universe_selector, None, universe)

    clear_grid(ui.characters_grid)

    for character in get_db().select_all_characters_from_universe(universe.universe_id):
        insert_character_tile(ui, character)

    selected = SelectionManager.get_selected_character()
    restore_selection(ui.characters_grid, selected.get_id() if selected else None) or CharacterHandler(
        ui).select_first_or_none()

def insert_character_tile(ui: Ui_MainWindow, character: Character):
    CharacterHandler(ui).insert_entity_tile(character)

def get_db():
    return DBDynamicConnection.get_instance()