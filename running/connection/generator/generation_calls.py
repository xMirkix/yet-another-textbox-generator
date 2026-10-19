from pathlib import Path
from typing import Callable

from PySide6.QtCore import QThreadPool, QRunnable, QObject, Signal, Qt
from PySide6.QtGui import QMovie, QPixmap, QColor

from generation.generation_gif_proxy import GenerationGifProxy
from generation.ffmpeg_locator import FfmpegNotFoundError
from generation.generation_mp4_proxy import show_ffmpeg_missing_dialog
from generation.gif_save_logic import Mp4EncodingError
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QMessageBox
from generation.generation_mp4_proxy import GenerationMp4Proxy
from generation.generation_png_proxy import GenerationPngProxy, is_valid_configuration_ui
from generation.generation_request import GenerationRequest
from models.form_bindings import (
    ExportFormat, ExportSettings, ExportSize,
    BorderSettings, FontSettings, TextStyle, SpriteSettings, ColorType, AudioSettings,
)
from services.selection_manager import SelectionManager, SideSelectors, \
    sound_manager
from services.video_player import OutputVideoPlayer
from ui.generated_ui import Ui_MainWindow

png_proxy = GenerationPngProxy()
gif_proxy = GenerationGifProxy()
mp4_proxy = GenerationMp4Proxy()

_pool = QThreadPool.globalInstance()
_pool.setMaxThreadCount(1)
_current_token = [0]
_active_signals: set = set()


class _WorkerSignals(QObject):
    done = Signal(object, object, int)
    failed = Signal(object, int)


_signals = _WorkerSignals()
_ui_ref: list = [None]
_on_complete: dict[int, Callable] = {}
_connected = [False]

def _handle_done(path, fmt, tok):
    callback = _on_complete.pop(tok, None)
    if tok != _current_token[0]:
        return
    on_result(_ui_ref[0], path, fmt)
    if callback:
        callback()

def _handle_failed(error, tok):
    _on_complete.pop(tok, None)
    if tok != _current_token[0]:
        return

    if isinstance(error, FfmpegNotFoundError):
        show_ffmpeg_missing_dialog()
    else:
        QMessageBox.critical(
            None, "Video-Creation failed",
            "The mp4 conversion failed. Please try again or contact the developer, "
            "if the problem persists and/or is reproducible.\n\n"
            f"Details: {error}",
        )


def _ensure_connected():
    if _connected[0]:
        return
    _signals.done.connect(_handle_done, Qt.ConnectionType.QueuedConnection)
    _signals.failed.connect(_handle_failed, Qt.ConnectionType.QueuedConnection)
    _connected[0] = True

class _GenerationRunnable(QRunnable):
    def __init__(self, signals: _WorkerSignals, request, fmt, token):
        super().__init__()
        self._signals = signals
        self._request = request
        self._fmt = fmt
        self._token = token
        self.setAutoDelete(True)

    def run(self):
        try:
            path = ""
            if self._fmt == ExportFormat.MP4:
                path = mp4_proxy.generate(self._request)
            if self._fmt == ExportFormat.GIF:
                path = gif_proxy.generate(self._request)
            if self._fmt == ExportFormat.PNG:
                path = png_proxy.generate(self._request)
        except (FfmpegNotFoundError, Mp4EncodingError) as e:
            self._signals.failed.emit(e, self._token)
            return
        except Exception as e:
            import traceback
            self._signals.failed.emit(RuntimeError(traceback.format_exc()), self._token)
            return
        self._signals.done.emit(path, self._fmt, self._token)


def execute_generation(ui: Ui_MainWindow,
                       left: SideSelectors,
                       right: SideSelectors,
                       on_complete: Callable = None):

    request = make_request(ui, left, right)

    if request is None:
        stop_video_player()
        return

    _ui_ref[0] = ui
    _ensure_connected()

    _current_token[0] += 1
    token = _current_token[0]

    for old in [t for t in _on_complete if t < token]:
        del _on_complete[old]
    if on_complete:
        _on_complete[token] = on_complete


    _pool.start(_GenerationRunnable(_signals, request,
                                    request.export_settings.export_format,
                                    token))

def make_request(ui: Ui_MainWindow,
                       left: SideSelectors,
                       right: SideSelectors) -> GenerationRequest | None:
    from services.selection_manager import left_manager, right_manager

    text_input   = ui.input.toPlainText()
    default_color = ui.default_color_selector.currentData()

    output_format = ExportFormat.PNG
    if ui.format_gif_option.isChecked():
        output_format = ExportFormat.GIF
    if ui.format_mp4_option.isChecked():
        output_format = ExportFormat.MP4

    sprite_left  = build_sprite_settings(left_manager,  left,  output_format)

    if sprite_left.expression is None and ui.include_checkbox.isChecked():
        hide_download(ui, "ERROR in Sprite Settings (Left) \n Fixes: Uncheck include, create an universe, character and expression or open a filled .yatg file")
        return None

    sprite_right = build_sprite_settings(right_manager, right, output_format)

    if sprite_right.expression is None and ui.include_checkbox_2.isChecked():
        hide_download(ui, "ERROR in Sprite Settings (Right) \n Fixes: Uncheck include, create an universe, character and expression or open a filled .yatg file")
        return None

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

    message = is_valid_configuration_ui(text_input, sprite_left,
                                     left.include_checkbox.isChecked(),
                                     sprite_right, right.include_checkbox.isChecked(),
                                     font_settings)

    if message is not None:
        ui.download.hide()
        ui.actionDownload_current_Textbox.setEnabled(False)
        ui.copy_to_clipboard.hide()
        ui.actionCopy_current_Textbox_to_Clipboard.setEnabled(False)
        ui.add_to_stack.hide()
        ui.actionAdd_current_Box_to_Stack.setEnabled(False)
        ui.output.setText(message)
        stop_video_player()
        return None

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
        audio_settings=AudioSettings(sound_manager.get_mono(), sound_manager.get_master_volume(),
                                     sound_manager.get_left_sound_files(), sound_manager.get_right_sound_files(),
                                     sound_manager.get_left_overlap(), sound_manager.get_right_overlap(),
                                     sound_manager.get_left_volume(), sound_manager.get_right_volume(),)
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

    return generation_request

def build_sprite_settings(manager: SelectionManager,
                            side: SideSelectors,
                            output_format: ExportFormat) -> SpriteSettings:
    universe   = side.universe_selector.currentData()
    character  = side.character_selector.currentData()
    expression = side.expression_selector.currentData()

    if None in (universe, character, expression):
        universe = None
        character = None
        expression = None

    alternating = None
    if side.include_checkbox.isChecked() and output_format == ExportFormat.GIF:
        alternating = side.alternating_selector.currentData() or manager.get_alternating_expression()

    expression_color = side.expression_color_selector.currentData()

    color_type = manager.get_color_manager().get_selected_color_type()

    selected_colors = manager.get_color_manager().get_selected_colors()

    simple_recoloring = manager.get_color_manager().get_simple_recoloring()

    if color_type != ColorType.CUSTOM:
        selected_colors = None
        simple_recoloring = None

    if expression_color is None:
        color_type = None
        selected_colors = None
        simple_recoloring = None

    return SpriteSettings(
        universe=universe,
        character=character,
        expression=expression,
        alternating_expression=alternating,
        alternating_interval=5,
        alternating_duration=5,
        expression_color=expression_color,
        color_type=color_type,
        selected_colors=selected_colors,
        simple_recoloring=simple_recoloring
    )



_video_player: OutputVideoPlayer | None = None

def get_video_player(ui: Ui_MainWindow) -> OutputVideoPlayer:
    global _video_player
    if _video_player is None:
        _video_player = OutputVideoPlayer(ui.output)
    return _video_player

def stop_video_player():
    if _video_player is not None:
        _video_player.stop()

def on_result(ui: Ui_MainWindow, result_path, output_format):
    if not result_path:
        hide_download(ui, "ERROR! Textbox could not be generated. \n Please try again, and restart the app if it keeps failing.")
        return

    if output_format == ExportFormat.MP4:
        ui.add_to_stack.hide()
        ui.actionAdd_current_Box_to_Stack.setEnabled(False)
        if getattr(ui, "movie", None):
            ui.movie.stop()
        video_result = get_video_player(ui).play_file(Path(result_path))
        if not video_result:
            ui.output.setText("Video preview not available")

    if output_format == ExportFormat.GIF:
        ui.add_to_stack.hide()
        ui.actionAdd_current_Box_to_Stack.setEnabled(False)
        stop_video_player()
        ui.movie = QMovie(str(result_path))
        ui.output.setMovie(ui.movie)
        ui.movie.start()

    if output_format == ExportFormat.PNG:
        stop_video_player()
        ui.add_to_stack.show()
        ui.actionAdd_current_Box_to_Stack.setEnabled(True)
        ui.output.setPixmap(QPixmap(str(result_path)))

    ui.download.setProperty("path", result_path)
    ui.download.show()
    ui.actionDownload_current_Textbox.setEnabled(True)
    ui.copy_to_clipboard.show()
    ui.actionCopy_current_Textbox_to_Clipboard.setEnabled(True)

def hide_download(ui: Ui_MainWindow, message: str):
    effect = QGraphicsDropShadowEffect()
    stop_video_player()
    effect.setColor(QColor("black"))
    effect.setOffset(0, 0)
    effect.setBlurRadius(4)
    ui.output.setGraphicsEffect(effect)

    ui.download.hide()
    ui.actionDownload_current_Textbox.setEnabled(False)
    ui.copy_to_clipboard.hide()
    ui.output.setText(message)