from models.entities import Universe, Character, Expression
from ui.generated_ui import Ui_MainWindow


def get_all_universes(ui: Ui_MainWindow) -> list[Universe]:
    pass

def get_all_characters(ui: Ui_MainWindow, universe: Universe) -> list[Character]:
    pass

def get_all_expressions(ui: Ui_MainWindow, universe: Universe, character: Character) -> list[Expression]:
    pass