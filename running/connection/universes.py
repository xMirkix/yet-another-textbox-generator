from ui.generated_ui import Ui_MainWindow


def connect_universes(ui: Ui_MainWindow):
    pass

"""
1. hide edit like initial
2. clear filter
"""
def on_tab_change(ui: Ui_MainWindow):
    ui.edit_universe.hide()
    ui.universe_filter_input.clear()