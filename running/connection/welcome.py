import shutil
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMessageBox

from static.change_service import Changes
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog

BASE_DIR = Path(__file__).parent

def connect_welcome(ui: Ui_MainWindow):
    ui.actionSave.triggered.connect(save_file)
    ui.actionOpen_2.triggered.connect(open_file)
    ui.open_file.clicked.connect(open_file)
    ui.actionQuit.triggered.connect(quit_app)

def save_file() -> bool:
    return manage_file(caption="Save File", filter_name="YATG Files (*.yatg)", isOpening=False)

def open_file() -> bool:
    if Changes.get_state():
        reply = QMessageBox.question(
            QApplication.activeWindow(),
            "Warning!",
            "There are unsaved changes, continue anyway?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.Cancel
        )
        if reply == QMessageBox.StandardButton.Yes:
            return open_file_impl()
        else:
            return False
    else:
        return open_file_impl()

def open_file_impl() -> bool:
    return manage_file(caption="Open File", filter_name="YATG Files (*.yatg)", isOpening=True)

def manage_file(caption: str, filter_name: str, isOpening: bool) -> bool:
    path, _ = QFileDialog.getOpenFileName(
        caption=caption,
        filter=filter_name
    )
    if path:  # File got selected
        Changes.reset()
        db_path = BASE_DIR / "assets" / "temp_dynamic_data" / "temp_data.sqlite3"
        if isOpening:
            shutil.copyfile(path, db_path) # Override cache file with selected
        else:
            shutil.copyfile(db_path, path) # Override file from path with cache
        return True
    return False

def quit_app():
    QApplication.quit()