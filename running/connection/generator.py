from PySide6.QtGui import QPixmap

from services import change_service
from services.database_service import DBDynamicConnection
from ui.generated_ui import Ui_MainWindow
from models.form_bindings import BorderSettings, SpriteSettings, FontSettings, ExportSettings
from PySide6.QtCore import QByteArray

def connect_generator(ui: Ui_MainWindow):
    pass

"""
1. Wipe universe/character/expression selector
2. Load universes into select (sorted)
Universes, characters and expressions are added dynamically
"""
def reload_ui(ui: Ui_MainWindow):
    ui.expression_selector.clear()
    ui.expression_preview.clear()
    ui.character_selector.clear()
    ui.character_preview.clear()
    ui.universe_selector.clear()
    ui.universe_preview.clear() # Wipe existing items in case of changes

    universes_list = get_db().select_all_universes()
    universes_list.sort(key=lambda universe: universe.order_position)
    for u in universes_list: # Get universes, characters and expressions are added dynamically
        ui.universe_selector.addItem(u.universe_name)

    if len(universes_list) > 0: # Sets universe preview image to first universe
        preview = universes_list[0].preview_image
        if preview:
            ui.universe_preview.setPixmap(change_service.base64_to_pixmap(preview))
        else:
            ui.universe_preview.clear()

def get_db():
    return DBDynamicConnection.get_instance()