import re

from PySide6.QtWidgets import QMessageBox

from services.database_service import DBDynamicConnection
from services.selection_manager import left_manager
from ui.generated_ui import Ui_MainWindow

CORE_PATTERN = re.compile(
    r"^demirramon\.com/user_content/undertale_character/([^/]+)/([^/]+)/?$",
    re.IGNORECASE
)

def normalize_url(url: str) -> str:
    url = url.strip()
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

    #ui.actionDownload_current_Textbox.setEnabled(False)
    #ui.actionCopy_current_Textbox_to_Clipboard.setEnabled(False)
    #ui.actionAdd_current_Box_to_Stack.setEnabled(False)
    #ui.actionDownload_Textbox_Stack.setEnabled(False)
    #ui.actionCopy_Stack_to_Clipboard.setEnabled(False)

def on_import_done(ui: Ui_MainWindow):
    ui.import_button.setEnabled(True)
    ui.import_progress.hide()
    ui.tabs.setDisabled(False)
    ui.actionSave.setEnabled(True)
    ui.actionOpen_2.setEnabled(True)
    ui.actionNew_File_2.setEnabled(True)

    ui.menuGenerator.setEnabled(True)

    #ui.actionDownload_current_Textbox.setEnabled(True)
    #ui.actionCopy_current_Textbox_to_Clipboard.setEnabled(True)
    #ui.actionAdd_current_Box_to_Stack.setEnabled(True)
    #ui.actionDownload_Textbox_Stack.setEnabled(True)
    #ui.actionCopy_Stack_to_Clipboard.setEnabled(True)

def on_failure(ui: Ui_MainWindow, message: str, new_universe_name: str | None):
    if new_universe_name and new_universe_name.strip() != "":
        universe = left_manager.get_selected_universe()
        get_db().delete_universe(universe.universe_id, universe.order_position)
        left_manager.set_selected_universe(None)
        left_manager.set_selected_character(None)
        left_manager.set_selected_expression(None)
        left_manager.try_to_select_first_universe_character_expression()

    on_import_done(ui)
    QMessageBox.warning(ui.centralwidget, "Error", message)

def get_db():
    return DBDynamicConnection.get_instance()
