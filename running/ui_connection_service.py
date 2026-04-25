from running.connection.characters import connect_characters
from running.connection.expressions import connect_expressions
from running.connection.generator import connect_generator
from running.connection.universes import connect_universes
from running.connection.welcome import connect_welcome
from ui.generated_ui import Ui_MainWindow

def connect_ui(ui: Ui_MainWindow):
    connect_welcome(ui)
    connect_generator(ui)
    connect_universes(ui)
    connect_characters(ui)
    connect_expressions(ui)