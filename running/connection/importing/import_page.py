import requests
from PySide6.QtCore import QTimer, QThreadPool, QObject, Signal, QRunnable
from PySide6.QtWidgets import QMessageBox, QApplication

from configs.paths import STATIC_DB
from models.entities import Character, Expression
from running.connection.importing.import_logic import fetch_character, ImportedCharacter, ImportedExpression
from running.connection.importing.import_cache import RequestCache
from running.connection.importing.import_utils import parse_import_url, on_failure, on_import_done, reset_progress, \
    on_import_startup
from services.database_service import DBDynamicConnection, DBStaticConnection
from services.selection_manager import left_manager, init_entity
from ui.generated_ui import Ui_MainWindow

connection = DBStaticConnection(STATIC_DB)

_import_pool = QThreadPool()
_import_pool.setMaxThreadCount(1)
_active_import_signals: set = set()

class _ImportWorkerSignals(QObject):
    progress = Signal(int, int)
    done = Signal(object, object)

class _ImportRunnable(QRunnable):
    def __init__(self, signals: _ImportWorkerSignals, universe, username: str, slug: str):
        super().__init__()
        self._signals = signals
        self._universe = universe
        self._username = username
        self._slug = slug
        self.setAutoDelete(True)

    def run(self):
        try:
            cache = RequestCache.get_instance()

            def report_progress(current: int, total: int):
                self._signals.progress.emit(current, total)

            character = fetch_character(self._username, self._slug, cache, report_progress)
        except requests.RequestException as e:
            self._signals.done.emit(None, f"Could not reach the page: {e}")
            return
        except Exception as e:
            self._signals.done.emit(None, f"Could not read the page: {e}")
            return

        if not character.expressions:
            self._signals.done.emit(None, "No expressions found on that page")
            return

        new_character, error = save_imported_character(self._universe, character)
        self._signals.done.emit(new_character, error)

def connect_import(ui: Ui_MainWindow):
    ui.token_import_label.hide()
    ui.token_for_import.hide()
    ui.disclaimer_1.hide()
    ui.disclaimer_2.hide()
    ui.import_button.clicked.connect(lambda: on_import(ui))
    ui.universe_for_import.activated.connect(lambda index: universe_change(ui, index))

def universe_change(ui: Ui_MainWindow, index):
    left_manager.set_selected_universe(
        ui.universe_for_import.itemData(index))
    left_manager.try_to_select_first_character_from_current_universe()
    left_manager.try_to_select_first_expression_from_current_character()
    QTimer.singleShot(0, lambda: reload_ui(ui))

def reload_ui(ui: Ui_MainWindow):
    ui.universe_for_import.clear()

    universe = left_manager.get_selected_universe()

    if universe is None:
        return

    init_entity(get_db().select_all_universes, ui.universe_for_import, None, universe)

def on_import(ui: Ui_MainWindow):
    universe = left_manager.get_selected_universe()
    mira_url = ui.character_page_for_import.text()

    if universe is None:
        on_failure(ui, "No universe selected")
        return

    if mira_url is None or mira_url == "":
        on_failure(ui, "No link provided")
        return

    parsed = parse_import_url(mira_url)

    if parsed is None:
        on_failure(ui, "Invalid URL")
        return

    username, slug = parsed

    reset_progress(ui)

    on_import_startup(ui)

    signals = _ImportWorkerSignals()
    _active_import_signals.add(signals)

    def on_progress(current: int, total: int):
        ui.import_progress.setMaximum(total)
        ui.import_progress.setValue(current)

    def on_done(new_character, error_message):
        _active_import_signals.discard(signals)
        on_import_done(ui)

        if error_message is not None:
            on_failure(ui, error_message)
            return

        try_set_selected(new_character)
        ui.character_page_for_import.clear()
        QMessageBox.information(QApplication.activeWindow(), "Success", "Character imported successfully")

    signals.progress.connect(on_progress)
    signals.done.connect(on_done)
    _import_pool.start(_ImportRunnable(signals, universe, username, slug))

def try_set_selected(new_character: Character):
    left_manager.set_selected_character(new_character)
    left_manager.try_to_select_first_expression_from_current_character()

def save_imported_character(universe, character: ImportedCharacter):
    try:
        db = get_db()

        universe_id = universe.universe_id

        font = connection.select_font_by_name(character.font_name.title())
        font_id = 1

        if font is not None:
            font_id = font.font_id

        order_position = db.count_characters(universe_id) + 1

        name = character.name.strip() + " (Imported)"

        preview = None

        if len(character.expressions) > 0:
            preview = character.expressions[0].image_bytes

        new_character = Character(-1, name, universe_id, 1, font_id, character.transform_id, preview, order_position)

        new_character = db.insert_character(new_character)

        save_associated_expressions(new_character, character.expressions)

        return new_character, None
    except Exception as _:
        return None, "An error occurred while saving the character"

def save_associated_expressions(character: Character, expressions: list[ImportedExpression]):
    db = get_db()
    character_id = character.character_id
    position = 1
    for expression in expressions:
        db.insert_expression(to_expression(expression, character_id, position))
        position += 1

def to_expression(expression: ImportedExpression, character_id: int, position: int) -> Expression:
    return Expression(-1, expression.title, character_id, expression.image_bytes, position)

def get_db():
    return DBDynamicConnection.get_instance()