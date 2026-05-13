from PySide6.QtWidgets import QApplication
from PySide6.QtNetwork import QLocalServer, QLocalSocket
import sys
from main_window_overrides import MainWindow
from running.ui_connection_service import connect_ui
from startup.init_population_service import InitPopulationService
from ui.generated_ui import Ui_MainWindow
from configs.paths import DYNAMIC_DB

db_path =  DYNAMIC_DB

APP_KEY = "yet-another-textbox-generator"

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Check if instance is running
    socket = QLocalSocket()
    socket.connectToServer(APP_KEY)

    if socket.waitForConnected(500):
        # App is already running
        sys.exit(0)

    # First instance - continue
    server = QLocalServer()
    QLocalServer.removeServer(APP_KEY)  # clear up old socket in case of crashes
    server.listen(APP_KEY)

    window = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window) # Define UI from generated file
    window.ui = ui

    db_path.touch() # Create cache file in case it doesn't exist

    p = InitPopulationService()
    p.init_populate(ui) # Initialize/Populate UI with data from Files (e.g. Colors)

    connect_ui(ui) # Connect UI to Logic Code, Respond to input


    window.show()
    app.exec()
