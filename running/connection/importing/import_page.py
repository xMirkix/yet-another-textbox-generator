from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox, QApplication, QPushButton

from configs.paths import STATIC_DB
from models.entities import Character, Expression, Universe
from running.connection.importing.import_logic import ImportedCharacter, ImportedExpression
from running.connection.importing.import_manager import ImportManager
from running.connection.importing.import_utils import parse_import_url, on_failure, on_import_done, reset_progress, \
    on_import_startup, open_import_file, get_import_source_text, parse_import_urls, finish_batch
from services.database_service import DBDynamicConnection, DBStaticConnection
from services.new_window_service import create_preview_window
from services.selection_manager import left_manager, init_entity
from ui.generated_ui import Ui_MainWindow

connection = DBStaticConnection(STATIC_DB)

_import_manager: ImportManager | None = None


def connect_import(ui: Ui_MainWindow):
    ui.import_button.clicked.connect(lambda: on_import(ui))
    ui.universe_for_import.activated.connect(lambda index: universe_change(ui, index))
    ui.new_universe_for_import.textChanged.connect(lambda: new_universe(ui))
    ui.select_import_file_button.clicked.connect(lambda: open_import_file(ui))

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
            QTimer.singleShot(0, lambda: reload_ui(ui))

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
    global _import_manager
    db = get_db()

    universe = left_manager.get_selected_universe()

    new_universe_name = ui.new_universe_for_import.text()
    new_universe_position = db.count_universes() + 1

    if new_universe_name and new_universe_name.strip() != "":
        u = Universe(-1, new_universe_name, None, 1, new_universe_position)
        db.insert_universe(u)
        universe = db.select_universe_by_order_position(new_universe_position)
        left_manager.set_selected_universe(universe)

    if universe is None:
        on_failure(ui, "No universe selected", new_universe_name)
        return

    source_text = get_import_source_text(ui)
    if source_text is None:
        on_failure(ui, "No link/file provided", new_universe_name)
        return


    pairs, invalid = parse_import_urls(source_text)

    if not pairs:
        on_failure(ui, "No valid URLs found", new_universe_name)
        return

    reset_progress(ui)
    on_import_startup(ui)

    _import_manager = ImportManager(save_callback=save_imported_character)

    def on_overall_progress(value: int, maximum: int):
        ui.import_progress.setMaximum(maximum)
        ui.import_progress.setValue(value)

    def on_all_finished(successes: int, errors: list[tuple[str, str, str]]):
        ui.character_page_for_import.clear()
        ui.new_universe_for_import.clear()
        ui.select_import_file_button.setProperty("path", "")
        ui.select_import_file_filename.setText("")
        reload_ui(ui)
        finish_batch(ui, new_universe_name, successes, errors)

    _import_manager.overall_progress.connect(on_overall_progress)
    _import_manager.all_finished.connect(on_all_finished)

    _import_manager.start(universe, pairs)

def try_set_selected(new_character: Character):
    left_manager.set_selected_character(new_character)
    left_manager.try_to_select_first_expression_from_current_character()

def save_imported_character(universe, character: ImportedCharacter):
    try:
        db = get_db()

        universe_id = universe.universe_id

        font = connection.select_font_by_name(character.font_name.title())
        font_id = font.font_id if font is not None else 1

        order_position = db.count_characters(universe_id) + 1

        name = character.name.strip() + " (Imported)"

        preview = character.expressions[0].image_bytes if character.expressions else None

        new_character = Character(-1, name, universe_id, 1, font_id, character.transform_id, preview, order_position)

        new_character = db.insert_character(new_character)

        save_associated_expressions(new_character, character.expressions)
        try_set_selected(new_character)

        return new_character, None
    except Exception:
        return None, "An error occurred while saving the character"

def save_associated_expressions(character: Character, expressions: list[ImportedExpression]):
    db = get_db()
    character_id = character.character_id
    for position, expression in enumerate(expressions, start=1):
        db.insert_expression(to_expression(expression, character_id, position))

def to_expression(expression: ImportedExpression, character_id: int, position: int) -> Expression:
    return Expression(-1, expression.title, character_id, expression.image_bytes, position)

def get_db():
    return DBDynamicConnection.get_instance()