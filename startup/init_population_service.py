from PySide6.QtWidgets import QComboBox

from models.form_bindings import ColorType
from running.connection.generator.generator import hide_alternating, make_sides
from running.connection.stacker.stacker import hide_initial
from services.database_service import DBStaticConnection, DBDynamicConnection
from services.font_service import check_with_system_fonts
from startup.in_memory.static_classes import Color
from ui.generated_ui import Ui_MainWindow
from PySide6.QtGui import QFontDatabase
import PySide6.QtGui
from configs.paths import UNDERTALE_PREVIEW, STATIC_DB, ICON_EYE

def populate_selector(items, selector, preview=None, preview_path=None, filter_fn=None):
    for item in items:
        if filter_fn is None or filter_fn(item):
            selector.addItem(str(item), userData=item)
    if preview and preview_path:
        preview.setPixmap(PySide6.QtGui.QPixmap(str(preview_path)))

def populate_color_selector(items: list[Color], selector, preview=None, set_preview: bool = True):
    for item in items:
        selector.addItem(str(item), userData=item)
    if preview and set_preview:
        first = items[0]
        border = darken(first.r, first.g, first.b)
        preview.setStyleSheet(
            f"background-color: rgb({first.r}, {first.g}, {first.b});"
            f"border: 2px solid rgb({border[0]}, {border[1]}, {border[2]});"
        )

def fill_coloring_types(selector: QComboBox):
    selector.addItem("Simple", userData=ColorType.SIMPLE)
    selector.addItem("Everything", userData=ColorType.EVERYTHING)
    selector.addItem("Custom", userData=ColorType.CUSTOM)

def darken(r: int, g: int, b: int, factor: float = 0.3) -> tuple[int, int, int]:
    return int(r * factor), int(g * factor), int(b * factor)

def set_preview_button_images(ui: Ui_MainWindow):
    icon = PySide6.QtGui.QIcon(str(ICON_EYE))

    everything = [
        ui.all_universes,
        ui.all_universes_2,
        ui.all_universes_3,
        ui.all_universes_4,
        ui.all_universes_5,
        ui.all_universes_6,
        ui.all_universes_7,
        ui.all_characters,
        ui.all_characters_2,
        ui.all_characters_3,
        ui.all_characters_4,
        ui.all_expressions,
        ui.all_expressions_2,
        ui.all_expressions_alt,
        ui.all_expressions_alt_2
    ]


    for button in everything:
        button.setText("")
        button.setIcon(icon)


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

def hide_color_type(ui: Ui_MainWindow):
    hide_color_type_left(ui)
    hide_color_type_right(ui)


def hide_color_type_left(ui: Ui_MainWindow):
    ui.expression_color_type_selector.hide()
    ui.expression_color_type_label.hide()
    ui.expression_color_type_button.hide()
    ui.line_79.hide()
    ui.line_80.hide()
    ui.label_left.hide()
    ui.label_right.hide()

def show_color_type_left(ui: Ui_MainWindow):
    ui.expression_color_type_selector.show()
    ui.expression_color_type_label.show()
    ui.expression_color_type_button.show()
    ui.line_79.show()
    ui.line_80.show()
    ui.label_left.show()
    ui.label_right.show()

def hide_color_type_right(ui: Ui_MainWindow):
    ui.expression_color_type_selector_2.hide()
    ui.expression_color_type_label_2.hide()
    ui.expression_color_type_button_2.hide()
    ui.line_37.hide()
    ui.line_82.hide()
    ui.label_left_2.hide()
    ui.label_right_2.hide()

def show_color_type_right(ui: Ui_MainWindow):
    ui.expression_color_type_selector_2.show()
    ui.expression_color_type_label_2.show()
    ui.expression_color_type_button_2.show()
    ui.line_37.show()
    ui.line_82.show()
    ui.label_left_2.show()
    ui.label_right_2.show()

class InitPopulationService:

    def __init__(self):
        self.connection = DBStaticConnection(STATIC_DB)
        self.colors = self.connection.select_all_colors()
        self.styles = self.connection.select_all_border_styles()
        self.fonts = self.connection.select_all_text_fonts()
        self.transforms = self.connection.select_all_text_transforms()
        self.dynamic_connection = DBDynamicConnection()

    def init_populate(self, ui: Ui_MainWindow):
        set_preview_button_images(ui)
        self.populate_border_settings(ui)  # Original/Deltarune/... and Color
        self.populate_sprite_settings(ui)  # Color
        ui.expression_color_selector_2.addItem("No changes", userData=None)
        populate_color_selector(self.colors, ui.expression_color_selector_2, ui.expression_color_preview_2, set_preview=False)
        hide_color_type(ui)
        self.populate_font_settings(ui)  # Determination Mono/Comic Sans/..., Asterisk Colors, Uppercase/Lowercase/...
        self.populate_universe_page(ui)
        self.populate_character_page(ui)
        self.populate_default_text_color(ui)
        hide_edits(ui)  # Hide edit blocks
        hide_removes(ui)
        sides = make_sides(ui)
        hide_alternating(sides[0])
        hide_alternating(sides[1])
        ui.download.hide()
        ui.import_load.hide()
        ui.import_progress.hide()
        ui.add_to_stack.hide()
        ui.copy_to_clipboard.hide()
        hide_initial(ui)
        self.create_temporary_data_tables()

    def populate_border_settings(self, ui: Ui_MainWindow):
        populate_selector(self.styles, ui.border_style_selector, ui.border_style_preview, UNDERTALE_PREVIEW)
        populate_color_selector(self.colors, ui.border_color_selector, ui.border_color_preview)

    def populate_sprite_settings(self, ui: Ui_MainWindow):
        ui.expression_color_selector.addItem("No changes", userData=None)
        fill_coloring_types(ui.expression_color_type_selector)
        fill_coloring_types(ui.expression_color_type_selector_2)
        ui.expression_color_type_button.setEnabled(False)
        ui.expression_color_type_button_2.setEnabled(False)
        populate_color_selector(self.colors, ui.expression_color_selector, ui.expression_color_preview, set_preview=False)

    def populate_font_settings(self, ui: Ui_MainWindow):
        check_with_system_fonts(self.fonts, ui.font_selector)
        populate_color_selector(self.colors, ui.asterisk_color_selector_1, ui.asterisk_color_preview_1)
        populate_color_selector(self.colors, ui.asterisk_color_selector_2, ui.asterisk_color_preview_2)
        populate_color_selector(self.colors, ui.asterisk_color_selector_3, ui.asterisk_color_preview_3)
        populate_selector(self.transforms, ui.text_transform_selector)

    def populate_universe_page(self, ui: Ui_MainWindow):
        populate_selector(self.styles, ui.universe_create_border_style_selector)
        populate_selector(self.styles, ui.universe_edit_border_style_selector)

    def populate_character_page(self, ui: Ui_MainWindow):
        check_with_system_fonts(self.fonts, ui.characters_create_font_selector)
        check_with_system_fonts(self.fonts, ui.characters_edit_font_selector)
        populate_selector(self.transforms, ui.characters_create_transform_selector)
        populate_selector(self.transforms, ui.characters_edit_transform_selector)

    def populate_default_text_color(self, ui: Ui_MainWindow):
        populate_color_selector(self.colors, ui.default_color_selector, ui.default_color_preview)

    def create_temporary_data_tables(self):
        self.dynamic_connection.create_all_tables()
