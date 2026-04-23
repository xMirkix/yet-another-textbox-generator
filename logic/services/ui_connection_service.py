from logic.connection.characters import connect_characters
from logic.connection.expressions import connect_expressions
from logic.connection.generator import connect_generator
from logic.connection.universes import connect_universes
from logic.connection.welcome import connect_welcome
from ui.generated_ui import Ui_MainWindow

def connect_ui(ui: Ui_MainWindow):
    connect_welcome(ui)
    connect_generator(ui)
    connect_universes(ui)
    connect_characters(ui)
    connect_expressions(ui)