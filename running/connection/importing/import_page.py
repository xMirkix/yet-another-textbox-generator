import requests
from PySide6.QtCore import QTimer, QThreadPool, QObject, Signal, QRunnable
from PySide6.QtWidgets import QMessageBox, QApplication, QPushButton

from configs.paths import STATIC_DB
from models.entities import Character, Expression, Universe
from running.connection.importing.import_logic import fetch_character, ImportedCharacter, ImportedExpression
from running.connection.importing.import_cache import RequestCache
from running.connection.importing.import_utils import parse_import_url, on_failure, on_import_done, reset_progress, \
    on_import_startup
from services.database_service import DBDynamicConnection, DBStaticConnection
from services.new_window_service import create_preview_window
from services.selection_manager import left_manager, init_entity, SelectionManager
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
    ui.new_universe_for_import.textChanged.connect(lambda: new_universe(ui))

    def connect_universe(button: QPushButton):
        def open_picker():
            universe = create_preview_window(
                ui,
                get_db().select_all_universes(),
                left_manager.get_selected_universe()
            )

            if universe is not None:
                left_manager.set_selected_universe(universe)
                left_manager.try_to_select_first_character_from_current_universe()
                left_manager.try_to_select_first_expression_from_current_character()
            reload_ui(ui)

        button.clicked.connect(open_picker)

    connect_universe(ui.all_universes_7)

def new_universe(ui: Ui_MainWindow):
    universe_name = ui.new_universe_for_import.text()
    if universe_name == "":
        ui.universe_import_label.show()
        ui.universe_for_import.show()
        ui.all_universes_7.show()
    else:
        ui.universe_import_label.hide()
        ui.universe_for_import.hide()
        ui.all_universes_7.hide()

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
    db = get_db()

    universe = left_manager.get_selected_universe()

    new_universe_name = ui.new_universe_for_import.text()
    new_universe_position = db.count_universes() + 1

    if new_universe_name and new_universe_name.strip() != "":
        u = Universe(-1, new_universe_name, None, 1, new_universe_position)
        db.insert_universe(u)
        universe = db.select_universe_by_order_position(new_universe_position)
        left_manager.set_selected_universe(universe)

    mira_url = ui.character_page_for_import.text()

    if universe is None:
        on_failure(ui, "No universe selected", new_universe_name)
        return

    if mira_url is None or mira_url == "":
        on_failure(ui, "No link provided", new_universe_name)
        return

    parsed = parse_import_url(mira_url)

    if parsed is None:
        on_failure(ui, "Invalid URL", new_universe_name)
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
            on_failure(ui, error_message, new_universe_name)
            return

        try_set_selected(new_character)
        ui.character_page_for_import.clear()
        ui.new_universe_for_import.clear()
        reload_ui(ui)
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