import shutil
from pathlib import Path
from typing import Callable

from PySide6.QtCore import QThreadPool, QRunnable, QObject, Signal, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QTextEdit, QFileDialog, QMessageBox
from PySide6.QtGui import QMovie

from configs.paths import PREVIEWS_DIR
from generation.generation_gif_proxy import GenerationGifProxy
from generation.generation_png_proxy import GenerationPngProxy, is_valid_configuration_ui
from generation.generation_request import GenerationRequest
from models.entities import Universe, Character, Expression
from models.form_bindings import SpriteSettings, FontSettings, TextStyle, BorderSettings, ExportSettings, ExportFormat, \
    ExportSize
from services.database_service import DBDynamicConnection
from services.selection_manager import SelectionManager, init_entity, set_preview
from startup.in_memory.static_classes import Color, BorderStyle
from ui.generated_ui import Ui_MainWindow

png_proxy = GenerationPngProxy()

gif_proxy = GenerationGifProxy()

_pool = QThreadPool.globalInstance()
_pool.setMaxThreadCount(1)
_current_token = [0]
_active_signals: set = set()

class _WorkerSignals(QObject):
    done = Signal(object, object, int)  # path, format, token

class _GenerationRunnable(QRunnable):
    def __init__(self, signals: _WorkerSignals, request, fmt, token):
        super().__init__()
        self._signals = signals
        self._request = request
        self._fmt = fmt
        self._token = token
        self.setAutoDelete(True)

    def run(self):
        if self._fmt == ExportFormat.GIF:
            path = gif_proxy.generate(self._request)
        else:
            path = png_proxy.generate(self._request)
        self._signals.done.emit(path, self._fmt, self._token)

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
    ui.alternating_selector.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: alternate_change(ui)))

    ui.expression_selector.setMaxVisibleItems(10)

    ui.expression_selector.setStyleSheet("""
        QComboBox {
            combobox-popup: 0;
        }
        QComboBox QAbstractItemView {
            max-height: 320px;
            min-height: 100px;
        }
        QComboBox QAbstractItemView::item {
            min-height: 30px;
            padding: 4px;
        }
    """)

    ui.alternating_selector.setStyleSheet("""
        QComboBox {
            combobox-popup: 0;
        }
        QComboBox QAbstractItemView {
            max-height: 320px;
            min-height: 100px;
        }
        QComboBox QAbstractItemView::item {
            min-height: 30px;
            padding: 4px;
        }
    """)

    # Asterisk
    ui.asterisk_checkbox.clicked.connect(lambda: update_with_function_then_regenerate(ui, lambda: hide_or_show(ui)))

    # Miscellaneous
    ui.font_selector.activated.connect(lambda: try_generate(ui))
    ui.default_color_selector.activated.connect(lambda: update_with_function_then_regenerate(ui, lambda: set_color(ui.default_color_selector.currentData(), ui.default_color_preview)))
    ui.text_style_regular_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.text_style_dark_world_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.text_transform_selector.activated.connect(lambda: try_generate(ui))
    ui.format_png_option.toggled.connect(lambda change: png_checked(ui, change))
    ui.format_gif_option.toggled.connect(lambda change: gif_checked(ui, change))
    ui.margin_checkbox.clicked.connect(lambda: try_generate(ui))
    ui.size_small_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.size_medium_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.size_big_option.toggled.connect(lambda change: on_radio_changed(ui, change))
    ui.include_checkbox.clicked.connect(lambda: check_for_alternating(ui))

    ui.debounce_timer = QTimer()
    ui.debounce_timer.setSingleShot(True)
    ui.debounce_timer.timeout.connect(lambda: execute_generation(ui))

    ui.input.textChanged.connect(lambda: try_generate(ui))

    ui.download.clicked.connect(lambda: download(ui))

def png_checked(ui: Ui_MainWindow, change: bool):
    hide_alternating(ui)
    on_radio_changed(ui, change)

def gif_checked(ui: Ui_MainWindow, change: bool):
    if ui.include_checkbox.isChecked():
        show_alternating(ui)
    on_radio_changed(ui, change)

def check_for_alternating(ui: Ui_MainWindow):
    if ui.format_gif_option.isChecked() and ui.include_checkbox.isChecked():
        show_alternating(ui)
    else:
        hide_alternating(ui)
    try_generate(ui)

def try_generate(ui: Ui_MainWindow):
    if hasattr(ui, "debounce_timer"):
        ui.debounce_timer.start(300)

def execute_generation(ui: Ui_MainWindow):
    text_input = ui.input.toPlainText()
    default_color: Color = ui.default_color_selector.currentData()
    alternating = None
    if ui.include_checkbox.isChecked() and ui.format_gif_option.isChecked():
        alternating = SelectionManager.get_alternating_expression()

    sprite_settings = SpriteSettings(
        universe=SelectionManager.get_selected_universe(),
        character=SelectionManager.get_selected_character(),
        expression=SelectionManager.get_selected_expression(),
        alternating_expression=alternating,
        alternating_interval=5, #default
        alternating_duration=3, #default
        expression_color=ui.expression_color_selector.currentData()
    )

    asterisk_colors: list[Color] = []

    if ui.asterisk_checkbox.isChecked():
        asterisk_colors.append(ui.asterisk_color_selector_1.currentData())
        asterisk_colors.append(ui.asterisk_color_selector_2.currentData())
        asterisk_colors.append(ui.asterisk_color_selector_3.currentData())

    text_style = TextStyle(TextStyle.REGULAR)
    if ui.text_style_dark_world_option.isChecked():
        text_style = TextStyle(TextStyle.DARK_WORLD)

    font_settings = FontSettings(
        font=ui.font_selector.currentData(),
        asterisk_color=asterisk_colors,
        text_style=text_style,
        transform=ui.text_transform_selector.currentData()
    )

    if not is_valid_configuration_ui(text_input, sprite_settings, ui.include_checkbox.isChecked(), font_settings):
        ui.download.hide()
        ui.output.setText("Nothing...")
        return

    border_settings = BorderSettings(style=ui.border_style_selector.currentData(),
                                     color=ui.border_color_selector.currentData())

    output_format = ExportFormat.PNG

    if ui.format_gif_option.isChecked():
        output_format = ExportFormat.GIF

    output_size = ExportSize.SMALL

    if ui.size_medium_option.isChecked():
        output_size = ExportSize.MEDIUM
    if ui.size_big_option.isChecked():
        output_size = ExportSize.BIG

    export_settings = ExportSettings(export_format=output_format, margin=ui.margin_checkbox.isChecked(),
                                     size=output_size)

    generation_request = GenerationRequest(text_input, default_color, border_settings, sprite_settings, font_settings,
                                           export_settings)

    _current_token[0] += 1
    token = _current_token[0]

    signals = _WorkerSignals()
    _active_signals.add(signals)

    def _on_done(path, fmt, tok):
        _active_signals.discard(signals)
        if tok == _current_token[0]:
            _on_result(ui, path, fmt)

    signals.done.connect(_on_done)
    _pool.start(_GenerationRunnable(signals, generation_request, output_format, token))

def _on_result(ui: Ui_MainWindow, result_path, output_format):
    if not result_path:
        ui.download.hide()
        ui.output.setText("Nothing...")
        return

    if output_format == ExportFormat.GIF:
        ui._movie = QMovie(str(result_path))
        ui.output.setMovie(ui._movie)
        ui._movie.start()
    else:
        ui.output.setPixmap(QPixmap(str(result_path)))

    ui.download.setProperty("path", result_path)
    ui.download.show()


def update_with_function_then_regenerate(ui: Ui_MainWindow, function: Callable):
    function()
    try_generate(ui)

def set_color(color: Color, preview: QLabel):
    border = darken(color.r, color.g, color.b)
    if color.a == 0:
        preview.setStyleSheet("background-color: transparent; border: 2px dashed gray;")
    else:
        preview.setStyleSheet(
            f"background-color: rgb({color.r}, {color.g}, {color.b});"
            f"border: 2px solid rgb({border[0]}, {border[1]}, {border[2]});"
        )

def set_border_color(text_input: QTextEdit, color: Color, preview: QLabel):
    text_input.setStyleSheet("")
    if color.a == 0:
        text_input.setStyleSheet("border: 2px dashed gray;")
    else:
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
    reset_selectors(ui, lambda: set_defaults(SelectionManager.get_selected_character(), ui))

def character_change(ui: Ui_MainWindow):
    character = ui.character_selector.currentData()
    SelectionManager.set_selected_character(character)
    set_defaults(character, ui)
    SelectionManager.try_to_select_first_expression_from_current_character()
    reset_selectors(ui, lambda: set_defaults(SelectionManager.get_selected_character(), ui))

def expression_change(ui: Ui_MainWindow):
    SelectionManager.set_selected_expression(ui.expression_selector.currentData())
    SelectionManager.try_to_init_alternating_expression()

    target = ui.expression_selector.currentData()
    for i in range(ui.alternating_selector.count()):
        if ui.alternating_selector.itemData(i).expression_id == target.expression_id:
            ui.alternating_selector.setCurrentIndex(i)
            break

    set_preview_generator_version(SelectionManager.get_alternating_expression(), ui.alternating_preview)
    set_preview_generator_version(SelectionManager.get_selected_expression(), ui.expression_preview)

def alternate_change(ui: Ui_MainWindow):
    alternating = ui.alternating_selector.currentData()
    SelectionManager.set_alternating_expression(alternating)
    set_preview_generator_version(SelectionManager.get_alternating_expression(), ui.alternating_preview)

def set_preview_generator_version(entity: Universe | Character | Expression | None, preview: QLabel):
    if not entity:
        return
    set_preview(entity.preview_image, preview, entity)

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

def hide_alternating(ui: Ui_MainWindow):
    ui.alternating_everything.hide()
    ui.line_67.hide()
    ui.line_68.hide()
    ui.line_69.hide()

def show_alternating(ui: Ui_MainWindow):
    ui.alternating_everything.show()
    ui.line_67.show()
    ui.line_68.show()
    ui.line_69.show()

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

def download(ui: Ui_MainWindow):
    source: Path | None = ui.download.property("path")

    if source is None:
        return

    suffix = source.suffix
    path, _ = QFileDialog.getSaveFileName(
        caption="Save",
        filter="PNG (*.png)" if suffix == ".png" else "GIF (*.gif)",
        options=QFileDialog.Option.DontConfirmOverwrite
    )
    if not path:
        return

    if not path.endswith(suffix):
        path += suffix

    if Path(path).exists():
        reply = QMessageBox.warning(
            None,
            "Save",
            f'"{Path(path).name}" already exists.\nDo you want to replace it?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

    shutil.copyfile(source, path)
"""
1. Wipe universe/character/expression selector
2. Load universes into select (sorted)
Universes, characters and expressions are added dynamically
"""
def reload_ui(ui: Ui_MainWindow):
    reset_selectors(ui, lambda: set_defaults(SelectionManager.get_selected_character(), ui))
    try_generate(ui)


def reset_selectors(ui: Ui_MainWindow, default_function: Callable):
    ui.expression_selector.clear()
    ui.expression_preview.clear()
    ui.character_selector.clear()
    ui.character_preview.clear()
    ui.universe_selector.clear()
    ui.universe_preview.clear() # Wipe existing items in case of changes
    ui.alternating_selector.clear()
    ui.alternating_preview.clear()

    db = get_db()

    has_any_entity = init_entity(db.select_all_universes, ui.universe_selector, ui.universe_preview, SelectionManager.get_selected_universe())

    if not has_any_entity:
        SelectionManager.reset()
        return

    has_any_entity = init_entity(lambda: db.select_all_characters_from_universe(ui.universe_selector.currentData().universe_id), ui.character_selector, ui.character_preview, SelectionManager.get_selected_character())

    if not has_any_entity:
        SelectionManager.set_selected_character(None)
        SelectionManager.set_selected_expression(None)
        return

    default_function()

    has_expressions = init_entity(
        lambda: db.select_all_expressions_from_character(ui.character_selector.currentData().character_id),
        ui.expression_selector, ui.expression_preview, SelectionManager.get_selected_expression())

    SelectionManager.set_selected_universe(ui.universe_selector.currentData())
    SelectionManager.set_selected_character(ui.character_selector.currentData())
    if has_expressions:
        SelectionManager.set_selected_expression(ui.expression_selector.currentData())
        init_entity(lambda: db.select_all_expressions_from_character(ui.character_selector.currentData().character_id), ui.alternating_selector, ui.alternating_preview, SelectionManager.get_selected_expression())
        SelectionManager.try_to_init_alternating_expression()
    else:
        SelectionManager.set_selected_expression(None)


def get_db():
    return DBDynamicConnection.get_instance()