from PySide6.QtWidgets import QApplication, QMessageBox

from logic.services.change_service import Changes
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog



def connect_welcome(ui: Ui_MainWindow):
    ui.actionSave.triggered.connect(save_file)
    ui.actionOpen_2.triggered.connect(open_file)
    ui.open_file.clicked.connect(open_file)
    ui.actionQuit.triggered.connect(quit_app)

def save_file() -> bool:
    path, _ = QFileDialog.getSaveFileName(
        caption="Save File",
        filter="YATG Files (*.yatg)"
    )
    if path:
        Changes.saved()
        print(path)  # TODO Write file
        return True
    return False

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
        path, _ = QFileDialog.getOpenFileName(
            caption="Open File",
            filter="YATG Files (*.yatg)"
        )
        if path:  # File got selected
            Changes.reset()
            print(path)  # TODO Load File
            return True
        return False

def quit_app():
    QApplication.quit()