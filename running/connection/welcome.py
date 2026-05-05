import shutil

from PySide6.QtWidgets import QApplication, QMessageBox

from static.change_service import Changes
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog
from configs.paths import DYNAMIC_DB

db_path = DYNAMIC_DB

def connect_welcome(ui: Ui_MainWindow):
    ui.actionSave.triggered.connect(save_file)
    ui.actionOpen_2.triggered.connect(lambda: open_file(ui=ui))
    ui.open_file.clicked.connect(lambda: open_file(ui=ui))
    ui.actionQuit.triggered.connect(quit_app)

def save_file() -> bool:
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
        ui.tabs.setCurrentIndex(0)
        return True
    return False

def quit_app():
    QApplication.quit()