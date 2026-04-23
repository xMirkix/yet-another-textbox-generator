from PySide6.QtWidgets import QApplication, QMainWindow

from logic.services.init_population_service import InitPopulationService
from logic.services.connection.ui_connection_service import connect_ui
from main_window_overrides import MainWindow
from ui.generated_ui import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window) # Define UI from generated file
    window.ui = ui

    p = InitPopulationService()
    p.init_populate(ui) # Initialize/Populate UI with data from Files (e.g. Colors)

    connect_ui(ui) # Connect UI to Logic Code, Respond to input


    window.show()
    app.exec()
