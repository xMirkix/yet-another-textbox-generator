from PySide6.QtWidgets import QApplication

from main_window_overrides import MainWindow
from running.ui_connection_service import connect_ui
from startup.init_population_service import InitPopulationService
from ui.generated_ui import Ui_MainWindow
from configs.paths import DYNAMIC_DB

db_path =  DYNAMIC_DB

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window) # Define UI from generated file
    window.ui = ui

    db_path.unlink(missing_ok=True) # Delete possible existing file from unexpected exit
    db_path.touch() # Create cache file

    p = InitPopulationService()
    p.init_populate(ui) # Initialize/Populate UI with data from Files (e.g. Colors)

    connect_ui(ui) # Connect UI to Logic Code, Respond to input


    window.show()
    app.exec()
