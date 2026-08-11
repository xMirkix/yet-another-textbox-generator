import os
import zipfile

from PySide6.QtWidgets import QFileDialog, QMessageBox

from models.entities import Character, Expression
from services.database_service import DBDynamicConnection
from services.selection_manager import left_manager


def _get_db() -> DBDynamicConnection:
    return DBDynamicConnection.get_instance()


def _sanitize_filename(name: str) -> str:
    """Remove problematic characters from a filename."""
    invalid_chars = '<>:"/\\|?*'
    cleaned = "".join(c for c in name if c not in invalid_chars).strip()
    return cleaned if cleaned and cleaned != "" else "unknow-filename"


def _unique_zip_path(used_paths: set, folder: str, filename: str, extension: str) -> str:
    """Ensures no path errors occur because of duplicate names
    (e.g., two expressions in the same folder have the same name.)"""
    base = f"{folder}/{filename}" if folder else filename
    candidate = f"{base}.{extension}"
    counter = 2
    while candidate in used_paths:
        candidate = f"{base}_{counter}.{extension}"
        counter += 1
    used_paths.add(candidate)
    return candidate


def _prompt_zip_path(default_name: str):
    path, _ = QFileDialog.getSaveFileName(
        None, "Save export as .zip", default_name, "ZIP Files (*.zip)"
    )
    if not path:
        return None
    if not path.lower().endswith(".zip"):
        path += ".zip"
    return path


def _write_preview_image(zf: zipfile.ZipFile, used_paths: set, folder: str, name: str, preview_image):
    """Writes a universe/character preview image, using the same name as its own folder."""
    if not preview_image:
        return
    filename = _sanitize_filename(name)
    zip_path = _unique_zip_path(used_paths, folder, filename, "png")
    zf.writestr(zip_path, preview_image)


def _write_expression(zf: zipfile.ZipFile, used_paths: set, folder: str, expression: Expression):
    if not expression.preview_image:
        return
    filename = _sanitize_filename(expression.expression_name)
    zip_path = _unique_zip_path(used_paths, folder, filename, "png")
    zf.writestr(zip_path, expression.preview_image)


def _write_character_expressions(zf: zipfile.ZipFile, used_paths: set, folder: str, character: Character):
    db = _get_db()
    for expression in db.select_all_expressions_from_character(character.character_id):
        _write_expression(zf, used_paths, folder, expression)


def _export_to_zip(default_name: str, writer):
    path = _prompt_zip_path(default_name)
    if path is None:
        return

    used_paths = set()
    try:
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
            writer(zf, used_paths)

        if not used_paths:
            os.remove(path)
            QMessageBox.warning(None, "Export", "No image found.")
            return

        if len(used_paths) == 1:
            QMessageBox.information(None, "Export", f"Export finished: {len(used_paths)} image was saved.")
        else:
            QMessageBox.information(None, "Export", f"Export finished: {len(used_paths)} images were saved.")
    except OSError as e:
        QMessageBox.critical(
            None, "Export failed",
            f"An error occurred while saving the zip file:\n{e}"
        )


def export_all_universes():
    db = _get_db()

    def writer(zf, used_paths):
        for universe in db.select_all_universes():
            universe_folder = _sanitize_filename(universe.universe_name)
            _write_preview_image(zf, used_paths, universe_folder, universe.universe_name, universe.preview_image)
            for character in db.select_all_characters_from_universe(universe.universe_id):
                character_folder = f"{universe_folder}/{_sanitize_filename(character.character_name)}"
                _write_preview_image(zf, used_paths, character_folder, character.character_name,
                                     character.preview_image)
                _write_character_expressions(zf, used_paths, character_folder, character)

    _export_to_zip("all_universes.zip", writer)


def export_selected_universe():
    universe = left_manager.get_selected_universe()
    if universe is None:
        QMessageBox.warning(None, "Export", "No universe selected.")
        return

    db = _get_db()

    def writer(zf, used_paths):
        _write_preview_image(zf, used_paths, "", universe.universe_name, universe.preview_image)
        for character in db.select_all_characters_from_universe(universe.universe_id):
            character_folder = _sanitize_filename(character.character_name)
            _write_preview_image(zf, used_paths, character_folder, character.character_name, character.preview_image)
            _write_character_expressions(zf, used_paths, character_folder, character)

    _export_to_zip(f"{_sanitize_filename(universe.universe_name)}.zip", writer)


def export_all_characters():
    universe = left_manager.get_selected_universe()
    if universe is None:
        QMessageBox.warning(None, "Export", "No universe selected.")
        return

    db = _get_db()

    def writer(zf, used_paths):
        _write_preview_image(zf, used_paths, "", universe.universe_name, universe.preview_image)
        for character in db.select_all_characters_from_universe(universe.universe_id):
            character_folder = _sanitize_filename(character.character_name)
            _write_preview_image(zf, used_paths, character_folder, character.character_name, character.preview_image)
            _write_character_expressions(zf, used_paths, character_folder, character)

    _export_to_zip(f"{_sanitize_filename(universe.universe_name)}_characters.zip", writer)


def export_selected_character():
    character = left_manager.get_selected_character()
    if character is None:
        QMessageBox.warning(None, "Export", "No character selected.")
        return

    def writer(zf, used_paths):
        _write_preview_image(zf, used_paths, "", character.character_name, character.preview_image)
        _write_character_expressions(zf, used_paths, "", character)

    _export_to_zip(f"{_sanitize_filename(character.character_name)}.zip", writer)


def export_all_expressions():
    character = left_manager.get_selected_character()
    if character is None:
        QMessageBox.warning(None, "Export", "No character selected.")
        return

    def writer(zf, used_paths):
        _write_preview_image(zf, used_paths, "", character.character_name, character.preview_image)
        _write_character_expressions(zf, used_paths, "", character)

    _export_to_zip(f"{_sanitize_filename(character.character_name)}_expressions.zip", writer)


def export_selected_expression():
    expression = left_manager.get_selected_expression()
    if expression is None:
        QMessageBox.warning(None, "Export", "No expression selected.")
        return

    def writer(zf, used_paths):
        _write_expression(zf, used_paths, "", expression)

    _export_to_zip(f"{_sanitize_filename(expression.expression_name)}.zip", writer)
