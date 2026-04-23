from logic.services.connection.welcome import connect_welcome
from ui.generated_ui import Ui_MainWindow


class UiConnectionService:

    def connect(self, ui: Ui_MainWindow):
        connect_welcome(ui)
        pass
