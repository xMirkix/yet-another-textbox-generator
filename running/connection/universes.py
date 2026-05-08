from typing import Callable

from models.entities import Universe
from running.connection.tile_service import insert_tile
from services import change_service
from services.change_service import select_image, remove_image
from services.database_service import DBDynamicConnection
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QMessageBox, QGroupBox, QLineEdit, QLabel, QPushButton


def connect_universes(ui: Ui_MainWindow):
    ui.universe_create_image_button.clicked.connect(lambda: select_image(ui.universe_create_image_preview, ui.universe_create_image_remove_button))
    ui.universe_edit_image_button.clicked.connect(lambda: select_image(ui.universe_edit_image_preview, ui.universe_edit_image_remove_button))
    ui.universe_create_image_remove_button.clicked.connect(lambda: remove_image(ui.universe_create_image_preview, ui.universe_create_image_remove_button))
    ui.universe_edit_image_remove_button.clicked.connect(lambda: remove_image(ui.universe_edit_image_preview, ui.universe_edit_image_remove_button))
    ui.universe_create_confirm_button.clicked.connect(lambda: create_universe(ui))
    ui.universe_edit_confirm_button.clicked.connect(lambda: edit_universe(ui))

def create_universe(ui: Ui_MainWindow):
    db = get_db()
    universe_name = ui.universe_create_name_input.text()
    pixmap = ui.universe_create_image_preview.pixmap()
    order_position = db.count_universes() + 1
    form_operation(-1, universe_name, pixmap, order_position, db.insert_universe)

    post_operation(
        ui.universe_create_name_input,
        ui.universe_create_image_preview,
        ui.universe_create_image_remove_button,
        lambda: on_tab_change(ui),
    )

def edit_universe(ui: Ui_MainWindow):
    universe_id = ui.universe_edit_confirm_button.property("universe")
    universe_name = ui.universe_edit_name_input.text()
    pixmap = ui.universe_edit_image_preview.pixmap()
    db = get_db()
    form_operation(universe_id, universe_name, pixmap, 42, db.update_universe) # Order position is not changed on update and thus not considered, 42 is the answer to the question of live

    post_operation(
        ui.universe_edit_name_input,
        ui.universe_edit_image_preview,
        ui.universe_edit_image_remove_button,
        lambda: on_tab_change(ui) # For edit to take effect
    )

def form_operation(universe_id: int, name: str, pixmap, order_position: int, db_function: Callable):
    if not name:
        QMessageBox.warning(None, "Invalid Name", "Name cannot be empty")
        return
    pixmap = change_service.pixmap_to_base64(pixmap) if pixmap else ''
    universe = Universe(universe_id, name, pixmap, order_position)
    db_function(universe)

def post_operation(input_to_clear: QLineEdit, pixmap_to_clear: QLabel, remove_button: QPushButton, post_function: Callable):
    input_to_clear.clear() # Clear input
    remove_image(pixmap_to_clear, remove_button)
    post_function()

def on_move(ui: Ui_MainWindow, universe: Universe, direction: int):
    pass

def on_edit(ui: Ui_MainWindow, universe: Universe):
    ui.universe_edit_name_input.setText(universe.universe_name)
    if universe.preview_image:
        ui.universe_edit_image_preview.setPixmap(change_service.base64_to_pixmap(universe.preview_image))
        ui.universe_edit_image_remove_button.show()
    ui.universe_edit_confirm_button.setProperty("universe", universe.universe_id)
    ui.edit_universe.show()

def on_delete(ui: Ui_MainWindow, universe: Universe, tile: QGroupBox):
    print(f"delete {universe.universe_name}")
    pass


def get_db():
    return DBDynamicConnection.get_instance()

"""
1. hide edit like initial
2. Load universes into grid
3. clear filter
"""
def on_tab_change(ui: Ui_MainWindow):
    ui.edit_universe.hide()
    clear_grid(ui.universe_grid)
    for u in get_db().select_all_universes():
        insert_tile(ui, ui.universe_grid, u)
    ui.universe_filter_input.clear()

def clear_grid(widget):
    layout = widget.layout()
    if layout is None:
        return
    while layout.count():
        item = layout.takeAt(0)
        w = item.widget()
        if w:
            w.deleteLater()