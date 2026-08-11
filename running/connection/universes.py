from typing import Callable

from PySide6.QtCore import QTimer

from models.entities import Universe
from models.handler.universe_handler import UniverseHandler
from running.connection.resizing import GridReflowFilter
from services import change_service
from services.exporting_service import export_all_universes, export_selected_universe
from services.grid_service import clear_grid, restore_selection
from services.change_service import select_image, remove_image
from services.database_service import DBDynamicConnection
from services.selection_manager import left_manager
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QMessageBox, QLineEdit, QLabel, QPushButton


def connect_universes(ui: Ui_MainWindow):
    ui.universe_grid.reflow_filter = GridReflowFilter(ui.universe_grid)

    create = ui.universe_create_confirm_button
    edit = ui.universe_edit_confirm_button

    create_image = ui.universe_create_image_button
    create_image_remove = ui.universe_create_image_remove_button
    create_image_preview = ui.universe_create_image_preview

    edit_image = ui.universe_edit_image_button
    edit_image_remove = ui.universe_edit_image_remove_button
    edit_image_preview = ui.universe_edit_image_preview


    create_image.clicked.connect(lambda: select_image(create_image_preview, create_image_remove, width=230, height=100)) # On creation image selection

    edit_image.clicked.connect(lambda: select_image(edit_image_preview, edit_image_remove, width=230, height=100)) # On edit image selection

    create_image_remove.clicked.connect(lambda: remove_image(create_image_preview, create_image_remove)) # On creation image removal

    edit_image_remove.clicked.connect(lambda: remove_image(edit_image_preview, edit_image_remove)) # On edit image removal

    create.clicked.connect(lambda: create_universe(ui)) # On creation

    edit.clicked.connect(lambda: edit_universe(ui)) # On edit

    ui.universe_filter_input.textChanged.connect(lambda text: QTimer.singleShot(0, lambda: filter_universes(ui, text))) # On filter change

    ui.export_all_universe.clicked.connect(lambda: export_all_universes())
    ui.export_selected_universe.clicked.connect(lambda: export_selected_universe())

def create_universe(ui: Ui_MainWindow):
    db = get_db()
    universe_name = ui.universe_create_name_input.text()
    pixmap = ui.universe_create_image_preview.pixmap()
    default_border_style = ui.universe_create_border_style_selector.currentData().border_id
    order_position = db.count_universes() + 1
    form_operation(-1, universe_name, pixmap, default_border_style, order_position, db.insert_universe)

    post_operation(
        ui.universe_create_name_input,
        ui.universe_create_image_preview,
        ui.universe_create_image_remove_button,
        lambda: QTimer.singleShot(0, lambda: reload_ui(ui)),
    )

def edit_universe(ui: Ui_MainWindow):
    universe_id = ui.universe_edit_confirm_button.property("universe_id")
    universe_name = ui.universe_edit_name_input.text()
    pixmap = ui.universe_edit_image_preview.pixmap()
    default_border_style = ui.universe_edit_border_style_selector.currentData().border_id
    db = get_db()

    exists = db.select_universe_by_id(universe_id)

    if not exists:
        post_operation(
            ui.universe_edit_name_input,
            ui.universe_edit_image_preview,
            ui.universe_edit_image_remove_button,
            lambda: QTimer.singleShot(0, lambda: reload_ui(ui))
        )
        return

    form_operation(universe_id, universe_name, pixmap, default_border_style, 42, db.update_universe) # Order position is not changed on update and thus not considered, 42 is the answer to the question of live

    left_manager.set_selected_universe(db.select_universe_by_id(universe_id))

    post_operation(
        ui.universe_edit_name_input,
        ui.universe_edit_image_preview,
        ui.universe_edit_image_remove_button,
        lambda: QTimer.singleShot(0, lambda: reload_ui(ui)) # For edit to take effect
    )

def form_operation(universe_id: int, name: str, pixmap, border_style: int, order_position: int, db_function: Callable):
    if not name:
        QMessageBox.warning(None, "Invalid Name", "Name cannot be empty")
        return
    pixmap = change_service.pixmap_to_blob(pixmap) if pixmap else None
    universe = Universe(universe_id, name, pixmap, border_style, order_position)
    db_function(universe)

def post_operation(input_to_clear: QLineEdit, pixmap_to_clear: QLabel, remove_button: QPushButton, post_function: Callable):
    input_to_clear.clear() # Clear input
    remove_image(pixmap_to_clear, remove_button)
    post_function()

def filter_universes(ui: Ui_MainWindow, name: str):
    clear_grid(ui.universe_grid)
    for universe in get_db().select_filtered_universes(name):
        insert_universe_tile(ui, universe)

    selected = left_manager.get_selected_universe()

    if selected:
        restore_selection(ui.universe_grid, selected.get_id())

def on_edit(ui: Ui_MainWindow, universe: Universe):
    ui.universe_edit_name_input.setText(universe.universe_name)
    ui.universe_edit_border_style_selector.setCurrentIndex(universe.default_border_style - 1)
    if universe.preview_image is not None:
        ui.universe_edit_image_preview.setPixmap(change_service.blob_to_pixmap(universe.preview_image))
        ui.universe_edit_image_remove_button.show()
    else:
        ui.universe_edit_image_preview.clear()
        ui.universe_edit_image_preview.setText("Nothing...")
        ui.universe_edit_image_remove_button.hide()
    ui.universe_edit_confirm_button.setProperty("universe_id", universe.universe_id)
    ui.edit_universe.show()


def get_db():
    return DBDynamicConnection.get_instance()

def reload_ui(ui: Ui_MainWindow):
    db = get_db()
    if db.count_universes() > 0:
        ui.export_all_universe.setEnabled(True)
        ui.export_selected_universe.setEnabled(True)
    else:
        ui.export_all_universe.setEnabled(False)
        ui.export_selected_universe.setEnabled(False)
    ui.edit_universe.hide()
    clear_grid(ui.universe_grid)
    for universe in db.select_all_universes():
        insert_universe_tile(ui, universe)
    ui.universe_filter_input.clear()

    selected = left_manager.get_selected_universe()
    restore_selection(ui.universe_grid, selected.get_id() if selected else None) or UniverseHandler(
        ui).select_first_or_none()

def insert_universe_tile(ui: Ui_MainWindow, universe: Universe):
    UniverseHandler(ui).insert_entity_tile(universe)