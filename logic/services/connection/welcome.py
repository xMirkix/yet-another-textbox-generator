from PySide6.QtWidgets import QApplication
from ui.generated_ui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog



def connect_welcome(ui: Ui_MainWindow):
    ui.actionSave.triggered.connect(save_file)
    ui.actionOpen_2.triggered.connect(open_file)
    ui.open_file.clicked.connect(open_file)
    ui.actionQuit.triggered.connect(quit_app)
    pass

def save_file():
    path, _ = QFileDialog.getSaveFileName(
        caption="Save File",
        filter="YATG Files (*.yatg)"
    )
    if path:
        print(path)  # Write file

def open_file():
    path, _ = QFileDialog.getOpenFileName(
        caption="Open File",
        filter="YATG Files (*.yatg)"
    )
    if path:  # File got selected
        print(path)  # Load File

def quit_app():
    QApplication.quit()