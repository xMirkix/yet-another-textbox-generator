from PySide6.QtWidgets import QComboBox

from services.database_service import DBStaticConnection, DBDynamicConnection
from startup.in_memory.static_classes import TextFont, Color
from ui.generated_ui import Ui_MainWindow
from PySide6.QtGui import QFontDatabase
import PySide6.QtGui
from configs.paths import UNDERTALE_PREVIEW

def populate_selector(items, selector, preview=None, preview_path=None, filter_fn=None):
    for item in items:
        if filter_fn is None or filter_fn(item):
            selector.addItem(str(item), userData=item)
    if preview and preview_path:
        preview.setPixmap(PySide6.QtGui.QPixmap(str(preview_path)))

def populate_color_selector(items: list[Color], selector, preview=None):
    for item in items:
        selector.addItem(str(item), userData=item)
    if preview:
        first = items[0]
        border = darken(first.r, first.g, first.b)
        preview.setStyleSheet(
            f"background-color: rgb({first.r}, {first.g}, {first.b});"
            f"border: 2px solid rgb({border[0]}, {border[1]}, {border[2]});"
        )

def darken(r: int, g: int, b: int, factor: float = 0.3) -> tuple[int, int, int]:
    return int(r * factor), int(g * factor), int(b * factor)

def check_with_system_fonts(fonts: list[TextFont], element: QComboBox):
    for f in fonts:
        if is_font_installed(f.font_name):
            element.addItem(f.font_name, userData=f)

def is_font_installed(font_name: str) -> bool:
    return font_name in QFontDatabase.families()

def hide_edits(ui: Ui_MainWindow):
    ui.edit_universe.hide()
    ui.edit_character.hide()
    ui.edit_expression.hide()

def hide_removes(ui: Ui_MainWindow):
    ui.universe_create_image_remove_button.hide()
    ui.universe_edit_image_remove_button.hide()
    ui.characters_create_image_remove_button.hide()
    ui.characters_edit_image_remove_button.hide()
    ui.expressions_create_image_remove_button.hide()
    ui.expressions_edit_image_remove_button.hide()

class InitPopulationService:

    def __init__(self):
        self.connection = DBStaticConnection()
        self.colors = self.connection.select_all_colors()
        self.styles = self.connection.select_all_border_styles()
        self.fonts = self.connection.select_all_text_fonts()
        self.transforms = self.connection.select_all_text_transforms()
        self.dynamic_connection = DBDynamicConnection()

    def init_populate(self, ui: Ui_MainWindow):
        self.populate_border_settings(ui)  # Original/Deltarune/... and Color
        self.populate_sprite_settings(ui)  # Color
        self.populate_font_settings(ui)  # Determination Mono/Comic Sans/..., Asterisk Colors, Uppercase/Lowercase/...
        self.populate_character_page(ui)
        hide_edits(ui)  # Hide edit blocks
        hide_removes(ui)
        ui.download.hide()
        self.create_temporary_data_tables()

    def populate_border_settings(self, ui: Ui_MainWindow):
        populate_selector(self.styles, ui.border_style_selector, ui.border_style_preview, UNDERTALE_PREVIEW)
        populate_color_selector(self.colors, ui.border_color_selector, ui.border_color_preview)

    def populate_sprite_settings(self, ui: Ui_MainWindow):
        populate_color_selector(self.colors, ui.expression_color_selector, ui.expression_color_preview)

    def populate_font_settings(self, ui: Ui_MainWindow):
        populate_selector(self.fonts, ui.font_selector, filter_fn=lambda f: is_font_installed(str(f)))
        populate_color_selector(self.colors, ui.asterisk_color_selector_1, ui.asterisk_color_preview_1)
        populate_color_selector(self.colors, ui.asterisk_color_selector_2, ui.asterisk_color_preview_2)
        populate_color_selector(self.colors, ui.asterisk_color_selector_3, ui.asterisk_color_preview_3)
        populate_selector(self.transforms, ui.text_transform_selector)

    def populate_character_page(self, ui: Ui_MainWindow):
        populate_selector(self.fonts, ui.characters_create_font_selector, filter_fn=lambda f: is_font_installed(str(f)))
        populate_selector(self.fonts, ui.characters_edit_font_selector, filter_fn=lambda f: is_font_installed(str(f)))
        populate_selector(self.transforms, ui.characters_create_transform_selector)
        populate_selector(self.transforms, ui.characters_edit_transform_selector)

    def create_temporary_data_tables(self):
        self.dynamic_connection.create_all_tables()
