from models.entities import Universe
from running.connection.tile_service import insert_tile
from services import change_service
from services.change_service import select_image, remove_image
from services.database_service import DBDynamicConnection
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QMessageBox, QGroupBox

def connect_universes(ui: Ui_MainWindow):
    ui.universe_create_image_button.clicked.connect(lambda: select_image(ui.universe_create_image_preview, ui.universe_create_image_remove_button))
    ui.universe_edit_image_button.clicked.connect(lambda: select_image(ui.universe_edit_image_preview, ui.universe_edit_image_remove_button))
    ui.universe_create_image_remove_button.clicked.connect(lambda: remove_image(ui.universe_create_image_preview, ui.universe_create_image_remove_button))
    ui.universe_edit_image_remove_button.clicked.connect(lambda: remove_image(ui.universe_edit_image_preview, ui.universe_edit_image_remove_button))
    ui.universe_create_confirm_button.clicked.connect(lambda: create_universe(ui))
    ui.universe_edit_confirm_button.clicked.connect(lambda: edit_universe(ui))

def create_universe(ui: Ui_MainWindow):
    db = get_db()
    if not ui.universe_create_name_input.text():
        QMessageBox.warning(None, "Invalid Name", "Name cannot be empty")
        return

    pixmap = ui.universe_create_image_preview.pixmap()
    image_data = change_service.pixmap_to_base64(pixmap) if pixmap else ''
    universe = Universe(-1, ui.universe_create_name_input.text(), image_data, db.count_universes() + 1)
    db.insert_universe(universe)

    ui.universe_create_name_input.clear()
    remove_image(ui.universe_create_image_preview, ui.universe_create_image_remove_button)
    insert_tile(ui, ui.universe_grid, universe)

def edit_universe(ui: Ui_MainWindow):
    db = get_db()
    if not ui.universe_edit_name_input.text():
        QMessageBox.warning(None, "Invalid Name", "Name cannot be empty")
        return

    pixmap = ui.universe_edit_image_preview.pixmap()
    image_data = change_service.pixmap_to_base64(pixmap) if pixmap else ''
    universe = Universe(ui.universe_edit_confirm_button.property("universe"), ui.universe_edit_name_input.text(), image_data, 42) # Order position is not changed and not considered
    db.update_universe(universe) # Update

    ui.universe_edit_name_input.clear() # Clear input
    remove_image(ui.universe_edit_image_preview, ui.universe_edit_image_remove_button)

    on_tab_change(ui) # Edit takes effect

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