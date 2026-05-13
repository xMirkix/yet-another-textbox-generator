import shutil
from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMessageBox

from services.change_service import Changes
from services.database_service import DBDynamicConnection
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog
from configs.paths import DYNAMIC_DB

db_path = DYNAMIC_DB

def connect_welcome(ui: Ui_MainWindow):
    ui.actionSave.triggered.connect(lambda: save_file(ui=ui))
    ui.actionOpen_2.triggered.connect(lambda: open_file(ui=ui))
    ui.open_file.clicked.connect(lambda: open_file(ui=ui))
    ui.actionQuit.triggered.connect(quit_app)

def save_file(ui: Ui_MainWindow) -> bool:
    file = Changes.get_current_selected_file()
    if file is not None:
        path = file
    else:
        path, _ = QFileDialog.getSaveFileName(
            caption="Save File",
            filter="YATG Files (*.yatg)"
        )
    if path:  # File got selected
        Changes.reset()
        if not path.endswith(".yatg"):
            path += ".yatg"
        shutil.copyfile(db_path, path)  # Override file from path with cache

        name = Path(path).name
        ui.centralwidget.window().setWindowTitle(f"{name} - Saved")
        QTimer.singleShot(3000, lambda: ui.centralwidget.window().setWindowTitle(name))  # Change back after 3 seconds
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
    if path:  # File got selected
        Changes.reset()
        if not path.endswith(".yatg"):
            path += ".yatg"
        shutil.copyfile(db_path, path)  # Override file from path with cache
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
    if path:  # File got selected
        Changes.reset()
        shutil.copyfile(path, db_path) # Override cache file with selected
        DBDynamicConnection.get_instance().reconnect() # reconnect to database
        ui.tabs.setCurrentIndex(0) # Switch to welcome Tab
        window_title = Path(path).name
        ui.centralwidget.window().setWindowTitle(window_title) # Set window title
        Changes.set_current_selected_file(path) # Save current file for quick save
        return True
    return False

def quit_app():
    QApplication.quit()