from logic.services.connection.characters import connect_characters
from logic.services.connection.expressions import connect_expressions
from logic.services.connection.generator import connect_generator
from logic.services.connection.universes import connect_universes
from logic.services.connection.welcome import connect_welcome
from ui.generated_ui import Ui_MainWindow

def connect_ui(ui: Ui_MainWindow):
    connect_welcome(ui)
    connect_generator(ui)
    connect_universes(ui)
    connect_characters(ui)
    connect_expressions(ui)