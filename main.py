import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QComboBox, QStyleFactory
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from main_window_overrides import MainWindow
from running.ui_connection_service import connect_ui
from startup.init_population_service import InitPopulationService
from ui.generated_ui import Ui_MainWindow
from configs.paths import DYNAMIC_DB, LOCO_ICON

db_path =  DYNAMIC_DB

APP_KEY = "yet-another-textbox-generator"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(str(LOCO_ICON)))

    # Check if instance is running
    socket = QLocalSocket()
    socket.connectToServer(APP_KEY)

    if socket.waitForConnected(500):
        # App is already running
        sys.exit(0)

    # First instance - continue
    server = QLocalServer()
    server.setSocketOptions(QLocalServer.SocketOption.WorldAccessOption)
    QLocalServer.removeServer(APP_KEY)  # clear up old socket in case of crashes
    server.listen(APP_KEY)

    window = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window) # Define UI from generated file
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
