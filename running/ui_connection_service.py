from running.connection.importing import import_page
from running.connection import universes, characters, expressions, generator
from running.connection.characters import connect_characters
from running.connection.expressions import connect_expressions
from running.connection.generator.generator import connect_generator, make_sides
from running.connection.universes import connect_universes
from running.connection.welcome import connect_welcome
from running.connection.importing.import_page import connect_import
from ui.generated_ui import Ui_MainWindow

def connect_ui(ui: Ui_MainWindow):
    connect_welcome(ui)
    connect_generator(ui)
    connect_universes(ui)
    connect_characters(ui)
    connect_expressions(ui)
    connect_import(ui)
    ui.tabs.currentChanged.connect(lambda index: on_tab_changed(ui, index))

def on_tab_changed(ui: Ui_MainWindow, index: int):
    tab_name = ui.tabs.tabText(index)
    if tab_name == "Generator":
        generator.generator.reload_ui(ui, *make_sides(ui))
    elif tab_name == "Universes":
        universes.reload_ui(ui)
    elif tab_name == "Characters":
        characters.reload_ui(ui)
    elif tab_name == "Expressions":
        expressions.reload_ui(ui)
    elif tab_name == "Import Character":
        import_page.reload_ui(ui)