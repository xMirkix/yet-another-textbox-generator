import copy

from PySide6.QtCore import QThreadPool, QRunnable, QObject, Signal
from PySide6.QtGui import QMovie, QPixmap

from generation.generation_gif_proxy import GenerationGifProxy
from generation.generation_png_proxy import GenerationPngProxy, is_valid_configuration_ui
from generation.generation_request import GenerationRequest
from models.form_bindings import (
    ExportFormat, ExportSettings, ExportSize,
    BorderSettings, FontSettings, TextStyle, SpriteSettings,
)
from services.selection_manager import SelectionManager, SideSelectors
from ui.generated_ui import Ui_MainWindow

png_proxy = GenerationPngProxy()
gif_proxy = GenerationGifProxy()

_pool = QThreadPool.globalInstance()
_pool.setMaxThreadCount(1)
_current_token = [0]
_active_signals: set = set()


class _WorkerSignals(QObject):
    done = Signal(object, object, int)


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


def execute_generation(ui: Ui_MainWindow,
                       left: SideSelectors,
                       right: SideSelectors):
    from services.selection_manager import left_manager, right_manager

    text_input   = ui.input.toPlainText()
    default_color = ui.default_color_selector.currentData()
    output_format = ExportFormat.GIF if ui.format_gif_option.isChecked() else ExportFormat.PNG

    sprite_left  = build_sprite_settings(left_manager,  left,  output_format)

    if sprite_left is None:
        ui.download.hide()
        ui.output.setText("Nothing...")
        return

    right_built = build_sprite_settings(right_manager, right, output_format)
    sprite_right = right_built if right_built is not None else empty_sprite(sprite_left)

    asterisk_colors = []
    if ui.asterisk_checkbox.isChecked():
        asterisk_colors = [
            ui.asterisk_color_selector_1.currentData(),
            ui.asterisk_color_selector_2.currentData(),
            ui.asterisk_color_selector_3.currentData(),
        ]

    text_style = (TextStyle(TextStyle.DARK_WORLD)
                  if ui.text_style_dark_world_option.isChecked()
                  else TextStyle(TextStyle.REGULAR))

    font_settings = FontSettings(
        font=ui.font_selector.currentData(),
        asterisk_color=asterisk_colors,
        text_style=text_style,
        transform=ui.text_transform_selector.currentData(),
    )

    if not is_valid_configuration_ui(text_input, sprite_left,
                                     left.include_checkbox.isChecked(),
                                     sprite_right, right.include_checkbox.isChecked(),
                                     font_settings):
        ui.download.hide()
        ui.output.setText("Nothing...")
        return

    border_settings = BorderSettings(
        style=ui.border_style_selector.currentData(),
        color=ui.border_color_selector.currentData(),
    )

    output_size = ExportSize.SMALL
    if ui.size_medium_option.isChecked(): output_size = ExportSize.MEDIUM
    if ui.size_big_option.isChecked():    output_size = ExportSize.BIG

    export_settings = ExportSettings(
        export_format=output_format,
        margin=ui.margin_checkbox.isChecked(),
        size=output_size,
    )

    generation_request = GenerationRequest(
        text_input,
        default_color,
        border_settings,
        sprite_left,
        sprite_right,
        font_settings,
        export_settings,
    )

    _current_token[0] += 1
    token = _current_token[0]

    signals = _WorkerSignals()
    _active_signals.add(signals)

    def on_done(path, fmt, tok):
        _active_signals.discard(signals)
        if tok == _current_token[0]:
            on_result(ui, path, fmt)

    signals.done.connect(on_done)
    _pool.start(_GenerationRunnable(signals, generation_request, output_format, token))

def empty_sprite(base: SpriteSettings) -> SpriteSettings:
    empty = copy.copy(base)
    empty.expression = None
    empty.alternating_expression = None
    return empty

def build_sprite_settings(manager: SelectionManager,
                            side: SideSelectors,
                            output_format: ExportFormat) -> SpriteSettings | None:
    universe   = side.universe_selector.currentData()
    character  = side.character_selector.currentData()
    expression = side.expression_selector.currentData()

    if None in (universe, character, expression):
        return None

    alternating = None
    if side.include_checkbox.isChecked() and output_format == ExportFormat.GIF:
        alternating = side.alternating_selector.currentData() or manager.get_alternating_expression()

    return SpriteSettings(
        universe=universe,
        character=character,
        expression=expression,
        alternating_expression=alternating,
        alternating_interval=5,
        alternating_duration=3,
        expression_color=side.expression_color_selector.currentData(),
    )


def on_result(ui: Ui_MainWindow, result_path, output_format):
    if not result_path:
        ui.download.hide()
        ui.output.setText("Nothing...")
        return

    if output_format == ExportFormat.GIF:
        ui.movie = QMovie(str(result_path))
        ui.output.setMovie(ui.movie)
        ui.movie.start()
    else:
        ui.output.setPixmap(QPixmap(str(result_path)))

    ui.download.setProperty("path", result_path)
    ui.download.show()