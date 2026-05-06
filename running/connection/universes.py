from models.entities import Universe
from running.connection.tile_service import insert_tile
from static import change_service
from static.database_service import DBDynamicConnection
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtGui import QImage, QPixmap


def connect_universes(ui: Ui_MainWindow):
    ui.universe_create_image_button.clicked.connect(lambda: select_image(ui))
    ui.universe_create_image_remove_button.clicked.connect(lambda: remove_image(ui))
    ui.universe_create_confirm_button.clicked.connect(lambda: create_universe(ui))

def select_image(ui: Ui_MainWindow):
    path, _ = QFileDialog.getOpenFileName(
        caption="Choose Image",
        filter="PNG Pictures (*.png)"
    )
    if not path:
        return  # Nothing selected

    image = QImage(path)
    if image.width() > 69 or image.height() > 70:
        QMessageBox.warning(None, "Invalid Picture", f"Picture size cannot exceed the resolution 69x70 (current: {image.width()}x{image.height()})")
        return

    ui.universe_create_image_preview.setPixmap(QPixmap(image))
    ui.universe_create_image_remove_button.show()

def remove_image(ui: Ui_MainWindow):
    ui.universe_create_image_preview.clear()
    ui.universe_create_image_preview.setText("Nothing...")
    ui.universe_create_image_remove_button.hide()

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
    remove_image(ui)

    insert_tile(ui.universe_grid, universe)

def get_db():
    return DBDynamicConnection.get_instance()

"""
1. hide edit like initial
2. clear filter
"""
def on_tab_change(ui: Ui_MainWindow):
    ui.edit_universe.hide()
    ui.universe_filter_input.clear()