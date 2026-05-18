import shutil
from typing import Callable

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QTextEdit, QFileDialog
from PySide6.QtGui import QMovie

from configs.paths import PREVIEWS_DIR, TEMP_PNG, TEMP_GIF
from generation import generation_service
from models.entities import Universe, Character
from models.form_bindings import SpriteSettings, FontSettings, TextStyle, BorderSettings, ExportSettings, ExportFormat, \
    ExportSize
from services.database_service import DBDynamicConnection
from services.selection_manager import SelectionManager, init_entity
from startup.in_memory.static_classes import Color, BorderStyle
from ui.generated_ui import Ui_MainWindow


def connect_generator(ui: Ui_MainWindow):
    # Colors
    ui.border_color_selector.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: set_border_color(ui.input, ui.border_color_selector.currentData(), ui.border_color_preview)))
    ui.expression_color_selector.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: set_color(ui.expression_color_selector.currentData(), ui.expression_color_preview)))
    ui.asterisk_color_selector_1.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: set_color(ui.asterisk_color_selector_1.currentData(), ui.asterisk_color_preview_1)))
    ui.asterisk_color_selector_2.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: set_color(ui.asterisk_color_selector_2.currentData(), ui.asterisk_color_preview_2)))
    ui.asterisk_color_selector_3.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: set_color(ui.asterisk_color_selector_3.currentData(), ui.asterisk_color_preview_3)))

    # Border Style
    ui.border_style_selector.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: set_border_style(ui.border_style_selector.currentData(), ui.border_style_preview)))

    # Universe/Character/Expression
    ui.universe_selector.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: universe_change(ui)))
    ui.character_selector.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: character_change(ui)))
    ui.expression_selector.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: expression_change(ui)))

    # Asterisk
    ui.asterisk_checkbox.clicked.connect(lambda: update_with_function_then_regenerate(ui, lambda: hide_or_show(ui)))

    # Miscellaneous
    ui.font_selector.activated.connect(lambda: try_generate(ui))
    ui.text_style_regular_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.text_style_dark_world_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.text_transform_selector.activated.connect(lambda: try_generate(ui))
    ui.format_png_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.format_gif_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.margin_checkbox.clicked.connect(lambda: try_generate(ui))
    ui.size_small_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.size_medium_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.size_small_option.toggled.connect(lambda: try_generate(ui))
    ui.include_checkbox.clicked.connect(lambda: try_generate(ui))

    ui.input.textChanged.connect(lambda: try_generate(ui))
    ui.download.clicked.connect(download)

def try_generate(ui: Ui_MainWindow):
    text_input = ui.input.toPlainText()
    sprite_settings = SpriteSettings(universe=SelectionManager.get_selected_universe(),
                                     character=SelectionManager.get_selected_character(),
                                     expression=SelectionManager.get_selected_expression(),
                                     expression_color=ui.expression_color_selector.currentData())

    asterisk_colors: list[Color] = []

    if ui.asterisk_checkbox.isChecked():
        asterisk_colors.append(ui.asterisk_color_selector_1.currentData())
        asterisk_colors.append(ui.asterisk_color_selector_2.currentData())
        asterisk_colors.append(ui.asterisk_color_selector_3.currentData())

    text_style = TextStyle(TextStyle.REGULAR)
    if ui.text_style_dark_world_option.isChecked():
        text_style = TextStyle(TextStyle.DARK_WORLD)

    font_settings = FontSettings(font=ui.font_selector.currentData(),
                                 asterisk_color=asterisk_colors,
                                 text_style=text_style,
                                 transform=ui.text_transform_selector.currentData())

    if not generation_service.is_valid_configuration_ui(text_input, sprite_settings, ui.include_checkbox.isChecked(), font_settings):
        ui.download.hide()
        ui.output.setText("Nothing...")
        return

    border_settings = BorderSettings(style=ui.border_style_selector.currentData(), color=ui.border_color_selector.currentData())

    output_format = ExportFormat.PNG

    if ui.format_gif_option.isChecked():
        output_format = ExportFormat.GIF

    output_size = ExportSize.SMALL

    if ui.size_medium_option.isChecked():
        output_size = ExportSize.MEDIUM
    if ui.size_big_option.isChecked():
        output_size = ExportSize.LARGE

    export_settings = ExportSettings(export_format=output_format, margin=ui.margin_checkbox.isChecked(), size=output_size)

    result_path = generation_service.generate(text_input, border_settings, sprite_settings, font_settings, export_settings)

    if result_path.suffix == ".gif":
        movie = QMovie(str(result_path))
        ui.output.setMovie(movie)
        movie.start()
    else:
        ui.output.setPixmap(QPixmap(str(result_path)))

    ui.download.show()


def update_with_function_then_regenerate(ui: Ui_MainWindow, function: Callable):
    function()
    try_generate(ui)

def set_color(color: Color, preview: QLabel):
    border = darken(color.r, color.g, color.b)
    preview.setStyleSheet(
        f"background-color: rgb({color.r}, {color.g}, {color.b});"
        f"border: 2px solid rgb({border[0]}, {border[1]}, {border[2]});"
    )

def set_border_color(text_input: QTextEdit, color: Color, preview: QLabel):
    text_input.setStyleSheet("")
    text_input.setStyleSheet(f"border: 2px solid rgb({color.r}, {color.g}, {color.b});")
    set_color(color, preview)

def darken(r: int, g: int, b: int, factor: float = 0.3) -> tuple[int, int, int]:
    return int(r * factor), int(g * factor), int(b * factor)

def set_border_style(style: BorderStyle, border_style_preview):
    with_extension = "".join([style.preview_file_name, ".png"])
    path = PREVIEWS_DIR / with_extension
    border_style_preview.setPixmap(QPixmap(path))

def universe_change(ui: Ui_MainWindow):
    new_universe : Universe = ui.universe_selector.currentData()
    SelectionManager.set_selected_universe(new_universe)
    SelectionManager.try_to_select_first_character_from_current_universe()
    SelectionManager.try_to_select_first_expression_from_current_character()
    reset_selectors(ui)

def character_change(ui: Ui_MainWindow):
    character = ui.character_selector.currentData()
    SelectionManager.set_selected_character(character)
    set_defaults(character, ui)
    SelectionManager.try_to_select_first_expression_from_current_character()
    reset_selectors(ui)

def expression_change(ui: Ui_MainWindow):
    SelectionManager.set_selected_expression(ui.expression_selector.currentData())
    reset_selectors(ui)

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

def on_radio_changed(ui: Ui_MainWindow, checked: bool):
    if checked:
        try_generate(ui)

def set_defaults(character: Character, ui: Ui_MainWindow):
    style = character.default_style
    transform = character.default_text_transform
    font = character.default_font
    ui.text_style_regular_option.setChecked(style == 1)
    ui.text_style_dark_world_option.setChecked(style == 2)
    ui.text_transform_selector.setCurrentIndex(transform - 1)
    ui.font_selector.setCurrentIndex(font - 1)

def download():
    source = generation_service.get_last_output()
    if source is None:
        return

    suffix = source.suffix
    path, _ = QFileDialog.getSaveFileName(
        caption="Save",
        filter="PNG (*.png)" if suffix == ".png" else "GIF (*.gif)"
    )
    if path:
        shutil.copyfile(source, path)
"""
1. Wipe universe/character/expression selector
2. Load universes into select (sorted)
Universes, characters and expressions are added dynamically
"""
def reload_ui(ui: Ui_MainWindow):
    reset_selectors(ui)
    try_generate(ui)


def reset_selectors(ui: Ui_MainWindow):
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

    set_defaults(SelectionManager.get_selected_character(), ui)

    init_entity(lambda: db.select_all_expressions_from_character(ui.character_selector.currentData().character_id), ui.expression_selector, ui.expression_preview, SelectionManager.get_selected_expression())

def get_db():
    return DBDynamicConnection.get_instance()