from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QScrollArea

from running.connection.importing import import_page
from running.connection import universes, characters, expressions, generator
from running.connection.stacker import stacker
from running.connection.characters import connect_characters
from running.connection.expressions import connect_expressions
from running.connection.generator.generator import connect_generator, make_sides
from running.connection.universes import connect_universes
from running.connection.welcome import connect_welcome
from running.connection.importing.import_page import connect_import
from running.connection.stacker.stacker import connect_stacker
from services.selection_manager import left_manager, right_manager
from ui.generated_ui import Ui_MainWindow

def connect_ui(ui: Ui_MainWindow):
    connect_welcome(ui)
    connect_generator(ui)
    connect_universes(ui)
    connect_characters(ui)
    connect_expressions(ui)
    connect_import(ui)
    connect_stacker(ui)
    ui.tabs.currentChanged.connect(lambda index: on_tab_changed(ui, index))

def on_tab_changed(ui: Ui_MainWindow, index: int):
    tab_name = ui.tabs.tabText(index)
    if tab_name == "Generator":
        check_uncheck_include(ui)
        generator.generator.reload_ui(ui, True, *make_sides(ui))
    elif tab_name == "Universes":
        QTimer.singleShot(0, lambda: reset_scroll_position(ui.scrollArea))
        universes.reload_ui(ui)
    elif tab_name == "Characters":
        QTimer.singleShot(0, lambda: reset_scroll_position(ui.scrollArea_2))
        characters.reload_ui(ui)
    elif tab_name == "Expressions":
        QTimer.singleShot(0, lambda: reset_scroll_position(ui.scrollArea_3))
        expressions.reload_ui(ui)
    elif tab_name == "Import Characters":
        import_page.reload_ui(ui)
    elif tab_name == "Textbox Stacker":
        stacker.reload_ui(ui)


def reset_scroll_position(scroll_area: QScrollArea):
    scroll_area.verticalScrollBar().setValue(0)

def check_uncheck_include(ui: Ui_MainWindow):
    if left_manager.get_selected_universe() is None:
        ui.tabWidget.setTabEnabled(1, False)
        ui.tabWidget.setTabEnabled(2, False)
        if left_manager.get_toggled() is None:
            left_manager.set_toggled(ui.include_checkbox.isChecked())
        if right_manager.get_toggled() is None:
            right_manager.set_toggled(ui.include_checkbox_2.isChecked())
        ui.include_checkbox.setChecked(False)
        ui.include_checkbox_2.setChecked(False)
    else:
        if left_manager.get_toggled() is not None or right_manager.get_toggled() is not None:
            ui.tabWidget.setTabEnabled(1, True)
            ui.tabWidget.setTabEnabled(2, True)
            ui.include_checkbox.setChecked(left_manager.get_toggled())
            ui.include_checkbox_2.setChecked(right_manager.get_toggled())
            left_manager.set_toggled(None)
            right_manager.set_toggled(None)