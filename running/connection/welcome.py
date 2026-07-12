import shutil
import zipfile
from pathlib import Path
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMessageBox
from services.change_service import Changes
from services.database_service import DBDynamicConnection
from services.selection_manager import left_manager
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog
from configs.paths import DYNAMIC_DB
from configs.paths import TITLE

db_path = DYNAMIC_DB

def connect_welcome(ui: Ui_MainWindow):
    ui.logo.setPixmap(QPixmap(str(TITLE)))
    ui.actionSave.triggered.connect(lambda: save_file(ui=ui))
    ui.actionOpen_2.triggered.connect(lambda: open_file(ui=ui))
    ui.open_file.clicked.connect(lambda: open_file(ui=ui))
    ui.actionQuit.triggered.connect(quit_app)
    ui.generator_link.clicked.connect(lambda: ui.tabs.setCurrentIndex(1))
    ui.import_link.clicked.connect(lambda: ui.tabs.setCurrentIndex(5))
    ui.universe_link.clicked.connect(lambda: ui.tabs.setCurrentIndex(2))

def _zip_db_to(path: str):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(db_path, arcname="data.db")

def _unzip_db_from(path: str):
    with zipfile.ZipFile(path, "r") as zf:
        with zf.open("data.db") as src, open(db_path, "wb") as dst:
            shutil.copyfileobj(src, dst)

def save_file(ui: Ui_MainWindow) -> bool:
    file = Changes.get_current_selected_file()
    if file is not None:
        path = file
    else:
        path, _ = QFileDialog.getSaveFileName(
            caption="Save File",
            filter="YATG Files (*.yatg)"
        )
    if path:
        if not path.endswith(".yatg"):
            path += ".yatg"
        _zip_db_to(path)
        Changes.reset()
        name = Path(path).name
        ui.centralwidget.window().setWindowTitle(f"{name} - Saved")
        QTimer.singleShot(3000, lambda: ui.centralwidget.window().setWindowTitle(name))
        return True
    return False

def save_file_without_ui() -> bool:
    file = Changes.get_current_selected_file()
    if file is not None:
        path = file
    else:
        path, _ = QFileDialog.getSaveFileName(
            caption="Save File",
            filter="YATG Files (*.yatg)"
        )
    if path: # File got selected
        if not path.endswith(".yatg"):
            path += ".yatg"
        _zip_db_to(path)
        Changes.reset()
        return True
    return False


def open_file(ui: Ui_MainWindow) -> bool:
    if Changes.get_state():
        reply = QMessageBox.question(
            QApplication.activeWindow(),
            "Warning!",
            "There are unsaved changes, continue anyway?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.Cancel
        )
        if reply == QMessageBox.StandardButton.Cancel:
            return False
    return manage_file(ui=ui, caption="Open File", filter_name="YATG Files (*.yatg)")

def manage_file(ui: Ui_MainWindow, caption: str, filter_name: str) -> bool:
    path, _ = QFileDialog.getOpenFileName(
        caption=caption,
        filter=filter_name
    )
    if path:
        Changes.reset()
        _unzip_db_from(path)
        DBDynamicConnection.get_instance().reconnect()
        ui.tabs.setCurrentIndex(0)
        window_title = Path(path).name
        ui.centralwidget.window().setWindowTitle(window_title)
        Changes.set_current_selected_file(path)
        left_manager.try_to_select_first_universe_character_expression()
        return True
    return False

def quit_app():
    QApplication.quit()