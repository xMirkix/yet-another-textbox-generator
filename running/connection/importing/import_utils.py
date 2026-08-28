from __future__ import annotations

import json
import re
from pathlib import Path
from PySide6.QtWidgets import QMessageBox, QFileDialog, QApplication
from services.database_service import DBDynamicConnection
from services.selection_manager import left_manager
from ui.generated_ui import Ui_MainWindow

CORE_PATTERN = re.compile(
    r"^demirramon\.com/user_content/undertale_character/([^/]+)/([^/]+)/?$",
    re.IGNORECASE
)

URL_FINDALL_PATTERN = re.compile(
    r"(?:https?://)?(?:www\.)?demirramon\.com/user_content/undertale_character/[^\s\"'<>]+",
    re.IGNORECASE
)

CHARACTERS_ARRAY_MARKER = re.compile(r'"characters"\s*:\s*\[')


def normalize_url(url: str) -> str:
    url = url.strip().rstrip(".,;:)\"'>")
    url = re.sub(r"^https?://", "", url, flags=re.IGNORECASE)
    url = re.sub(r"^www\.", "", url, flags=re.IGNORECASE)
    return url

def parse_import_url(mira_url: str) -> tuple[str, str] | None:
    match = CORE_PATTERN.match(normalize_url(mira_url))
    if match is None:
        return None
    return match.group(1), match.group(2)

def is_url_valid(mira_url: str) -> bool:
    return CORE_PATTERN.match(normalize_url(mira_url)) is not None


def get_import_source_text(ui: Ui_MainWindow) -> str | None:
    path = ui.select_import_file_button.property("path")
    if path:
        try:
            return Path(path).read_text(encoding="utf-8", errors="ignore")
        except OSError:
            return None

    text = ui.character_page_for_import.text()
    return text if text and text.strip() else None


def find_matching_bracket(text: str, open_idx: int, open_char: str, close_char: str) -> int | None:
    depth = 0
    i = open_idx
    in_string = False
    escape = False
    while i < len(text):
        ch = text[i]
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
        else:
            if ch == '"':
                in_string = True
            elif ch == open_char:
                depth += 1
            elif ch == close_char:
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return None

def extract_character_dicts(raw: str) -> list[dict]:
    results: list[dict] = []
    for match in CHARACTERS_ARRAY_MARKER.finditer(raw):
        array_start = match.end() - 1
        array_end = find_matching_bracket(raw, array_start, "[", "]")
        if array_end is None:
            continue
        array_text = raw[array_start:array_end + 1]
        try:
            characters = json.loads(array_text)
        except json.JSONDecodeError:
            continue
        if isinstance(characters, list):
            for entry in characters:
                if isinstance(entry, dict):
                    results.append(entry)
    return results


def character_dicts_to_pairs(character_dicts: list[dict]) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for entry in character_dicts:
        slug = entry.get("codename")
        creator = entry.get("creator") or {}
        username = creator.get("username") if isinstance(creator, dict) else None
        if slug and username:
            pairs.append((username, slug))
    return pairs


def parse_import_urls(raw: str) -> tuple[list[tuple[str, str]], list[str]]:
    valid: list[tuple[str, str]] = []
    invalid: list[str] = []
    seen: set[tuple[str, str]] = set()

    for candidate in URL_FINDALL_PATTERN.findall(raw):
        parsed = parse_import_url(candidate)
        if parsed is None:
            invalid.append(candidate)
        elif parsed not in seen:
            seen.add(parsed)
            valid.append(parsed)

    character_dicts = extract_character_dicts(raw)
    for pair in character_dicts_to_pairs(character_dicts):
        if pair not in seen:
            seen.add(pair)
            valid.append(pair)

    if not valid and not invalid:
        for line in re.split(r"[\n,;]+", raw):
            line = line.strip()
            if not line:
                continue
            parsed = parse_import_url(line)
            if parsed is None:
                invalid.append(line)
            elif parsed not in seen:
                seen.add(parsed)
                valid.append(parsed)

    return valid, invalid


def reset_progress(ui: Ui_MainWindow):
    ui.import_progress.setMinimum(0)
    ui.import_progress.setMaximum(0)
    ui.import_progress.setValue(0)

def on_import_startup(ui: Ui_MainWindow):
    ui.import_progress.show()
    ui.import_button.setEnabled(False)
    ui.tabs.setDisabled(True)
    ui.actionSave.setEnabled(False)
    ui.actionOpen_2.setEnabled(False)
    ui.actionNew_File_2.setEnabled(False)

    ui.menuGenerator.setEnabled(False)


def on_import_done(ui: Ui_MainWindow):
    ui.import_button.setEnabled(True)
    ui.import_progress.hide()
    ui.tabs.setDisabled(False)
    ui.actionSave.setEnabled(True)
    ui.actionOpen_2.setEnabled(True)
    ui.actionNew_File_2.setEnabled(True)

    ui.menuGenerator.setEnabled(True)
    ui.select_import_file_filename.setText("No file selected")


def on_failure(ui: Ui_MainWindow, message: str, new_universe_name: str | None):
    cleanup_new_universe_if_needed(new_universe_name)
    on_import_done(ui)
    QMessageBox.warning(ui.centralwidget, "Error", message)


def cleanup_new_universe_if_needed(new_universe_name: str | None):
    if new_universe_name and new_universe_name.strip() != "":
        universe = left_manager.get_selected_universe()
        if universe is not None:
            get_db().delete_universe(universe.universe_id, universe.order_position)
        left_manager.set_selected_universe(None)
        left_manager.set_selected_character(None)
        left_manager.set_selected_expression(None)
        left_manager.try_to_select_first_universe_character_expression()


def finish_batch(ui: Ui_MainWindow, new_universe_name: str | None,
                  successes: int, errors: list[tuple[str, str, str]]):
    on_import_done(ui)

    if successes == 0:
        cleanup_new_universe_if_needed(new_universe_name)

    if not errors:
        QMessageBox.information(
            QApplication.activeWindow(), "Success",
            f"{successes} character(s) imported successfully"
        )
        return

    error_lines = "\n".join(f"- {u}/{s}: {msg}" for u, s, msg in errors)
    text = f"{successes} succeeded, {len(errors)} failed:\n{error_lines}"

    if successes > 0:
        QMessageBox.warning(ui.centralwidget, "Import finished with errors", text)
    else:
        QMessageBox.warning(ui.centralwidget, "Import failed", text)


def open_import_file(ui: Ui_MainWindow):
    path, _ = QFileDialog.getOpenFileName(
        ui.centralwidget,
        caption="Open Text File",
        filter="Text Files (*.txt *.html *.md)"
    )
    if not path:
        return
    p = Path(path)
    short_path = f"{p.parent.name}/{p.name}"
    ui.select_import_file_filename.setText(short_path)
    ui.select_import_file_button.setProperty("path", path)


def get_db():
    return DBDynamicConnection.get_instance()
