from typing import Callable

import PySide6
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QTextEdit

from configs.paths import PREVIEWS_DIR
from models.entities import Universe
from services.database_service import DBDynamicConnection
from services.selection_manager import SelectionManager, init_entity
from startup.in_memory.static_classes import Color, BorderStyle
from ui.generated_ui import Ui_MainWindow


def connect_generator(ui: Ui_MainWindow):
    # Colors
    ui.border_color_selector.activated.connect(lambda: update_with_function_then_regenerate(lambda: set_border_color(ui.input, ui.border_color_selector.currentData(), ui.border_color_preview)))
    ui.expression_color_selector.activated.connect(lambda: update_with_function_then_regenerate(lambda: set_color(ui.expression_color_selector.currentData(), ui.expression_color_preview)))
    ui.asterisk_color_selector_1.activated.connect(lambda: update_with_function_then_regenerate(lambda: set_color(ui.asterisk_color_selector_1.currentData(), ui.asterisk_color_preview_1)))
    ui.asterisk_color_selector_2.activated.connect(lambda: update_with_function_then_regenerate(lambda: set_color(ui.asterisk_color_selector_2.currentData(), ui.asterisk_color_preview_2)))
    ui.asterisk_color_selector_3.activated.connect(lambda: update_with_function_then_regenerate(lambda: set_color(ui.asterisk_color_selector_3.currentData(), ui.asterisk_color_preview_3)))

    # Border Style
    ui.border_style_selector.activated.connect(lambda: update_with_function_then_regenerate(lambda: set_border_style(ui.border_style_selector.currentData(), ui.border_style_preview)))

    # Universe/Character/Expression
    ui.universe_selector.activated.connect(lambda: update_with_function_then_regenerate(lambda: universe_change(ui)))
    ui.character_selector.activated.connect(lambda: update_with_function_then_regenerate(lambda: character_change(ui)))
    ui.expression_selector.activated.connect(lambda: update_with_function_then_regenerate(lambda: expression_change(ui)))

    # Asterisk
    ui.asterisk_checkbox.clicked.connect(lambda: update_with_function_then_regenerate(lambda: hide_or_show(ui)))

    # Miscellaneous
    ui.font_selector.activated.connect(lambda: update_with_function_then_regenerate(lambda: ()))
    ui.text_style_regular_option.toggled.connect(on_radio_changed)
    ui.text_style_dark_world_option.toggled.connect(on_radio_changed)
    ui.text_transform_selector.activated.connect(lambda: update_with_function_then_regenerate(lambda: ()))
    ui.format_png_option.toggled.connect(on_radio_changed)
    ui.format_gif_option.toggled.connect(on_radio_changed)
    ui.margin_checkbox.clicked.connect(lambda: update_with_function_then_regenerate(lambda: ()))
    ui.size_small_option.toggled.connect(on_radio_changed)
    ui.size_medium_option.toggled.connect(on_radio_changed)
    ui.size_small_option.toggled.connect(lambda: update_with_function_then_regenerate(lambda: ()))

def update_with_function_then_regenerate(function: Callable):
    function()
    # TODO add generate Function here

def set_color(color: Color, preview: QLabel):
    preview.setAutoFillBackground(True)
    palette = preview.palette()
    palette.setColor(preview.backgroundRole(), PySide6.QtGui.QColor(color.r, color.g, color.b, 255))
    preview.setPalette(palette)

def set_border_color(text_input: QTextEdit, color: Color, preview: QLabel):
    text_input.setStyleSheet("")
    text_input.setStyleSheet(f"border: 2px solid rgb({color.r}, {color.g}, {color.b});")
    set_color(color, preview)

def set_border_style(style: BorderStyle, border_style_preview):
    with_extension = "".join([style.preview_file_name, ".png"])
    path = PREVIEWS_DIR / with_extension
    border_style_preview.setPixmap(QPixmap(path))

def universe_change(ui: Ui_MainWindow):
    new_universe : Universe = ui.universe_selector.currentData()
    SelectionManager.set_selected_universe(new_universe)
    SelectionManager.try_to_select_first_character_from_current_universe()
    reload_ui(ui)

def character_change(ui: Ui_MainWindow):
    SelectionManager.set_selected_character(
        ui.character_selector.currentData())
    SelectionManager.try_to_select_first_expression_from_current_character()
    reload_ui(ui)

def expression_change(ui: Ui_MainWindow):
    SelectionManager.set_selected_expression(ui.expression_selector.currentData())
    reload_ui(ui)

def hide_asterisk(ui: Ui_MainWindow):
    ui.asterisk_color_everything.hide()
    ui.asterisk_color_values_everything.hide()

    ui.line_51.hide()
    ui.line_56.hide()

    ui.line_50.hide()
    ui.line_55.hide()

def show_asterisk(ui: Ui_MainWindow):
    ui.asterisk_color_everything.show()
    ui.asterisk_color_values_everything.show()

    ui.line_51.show()
    ui.line_56.show()

    ui.line_50.show()
    ui.line_55.show()

def hide_or_show(ui: Ui_MainWindow):
    if ui.asterisk_checkbox.isChecked():
        show_asterisk(ui)
    else:
        hide_asterisk(ui)

def on_radio_changed(checked: bool):
    if checked:
        update_with_function_then_regenerate(lambda: ())

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

    db = get_db()

    has_any_entity = init_entity(db.select_all_universes, ui.universe_selector, ui.universe_preview, SelectionManager.get_selected_universe())

    if not has_any_entity:
        return

    has_any_entity = init_entity(lambda: db.select_all_characters_from_universe(ui.universe_selector.currentData().universe_id), ui.character_selector, ui.character_preview, SelectionManager.get_selected_character())

    if not has_any_entity:
        return

    init_entity(lambda: db.select_all_expressions_from_character(ui.character_selector.currentData().character_id), ui.expression_selector, ui.expression_preview, SelectionManager.get_selected_expression())

def get_db():
    return DBDynamicConnection.get_instance()