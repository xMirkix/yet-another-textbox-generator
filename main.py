import sys
import tempfile
from pathlib import Path

from PySide6.QtCore import QLockFile
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QComboBox, QStyleFactory
from main_window_overrides import MainWindow
from running.ui_connection_service import connect_ui
from startup.init_population_service import InitPopulationService
from ui.generated_ui import Ui_MainWindow
from configs.paths import DYNAMIC_DB, LOGO_ICON

db_path =  DYNAMIC_DB

APP_KEY = "yet-another-textbox-generator"

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setDesktopFileName("YATG")

    app.setWindowIcon(QIcon(str(LOGO_ICON)))

    lock_path = Path(tempfile.gettempdir()) / "yatg.lock"
    lock = QLockFile(str(lock_path))

    if not lock.tryLock(200):
        sys.exit(0)

    window = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window) # Define UI from generated file
    window.setWindowTitle("Yet Another Textbox Generator")
    window.ui = ui

    if sys.platform == "win32":
        fusion_style = QStyleFactory.create("Fusion")
        for combo in window.findChildren(QComboBox):
            combo.view().setStyle(fusion_style)

    db_path.touch() # Create cache file in case it doesn't exist

    p = InitPopulationService()
    p.init_populate(ui) # Initialize/Populate UI with data from Files (e.g. Colors)

    connect_ui(ui) # Connect UI to Logic Code, Respond to input


    window.show()
    app.exec()
