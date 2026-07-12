from typing import Callable

from PySide6.QtCore import QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QComboBox, QLabel

from running.connection.generator.generation_calls import execute_generation
from running.connection.generator.generator_utils import set_color, set_border_style, set_stylesheet, set_defaults, \
    set_preview_generator_version, set_border_color, show_alternating, \
    hide_alternating, hide_or_show, download
from services.database_service import DBDynamicConnection
from services.selection_manager import SelectionManager, init_entity, SideSelectors, left_manager, right_manager
from ui.generated_ui import Ui_MainWindow

def make_sides(ui: Ui_MainWindow) -> tuple[SideSelectors, SideSelectors]:
    left = SideSelectors(
        universe_selector=ui.universe_selector,
        universe_preview=ui.universe_preview,
        character_selector=ui.character_selector,
        character_preview=ui.character_preview,
        expression_selector=ui.expression_selector,
        expression_preview=ui.expression_preview,
        alternating_selector=ui.alternating_selector,
        alternating_preview=ui.alternating_preview,
        include_checkbox=ui.include_checkbox,
        expression_color_selector=ui.expression_color_selector,
        expression_color_preview=ui.expression_color_preview,
        alternating_container=ui.alternating_everything,
        alternating_lines=[ui.line_67, ui.line_68, ui.line_69],
    )
    right = SideSelectors(
        universe_selector=ui.universe_selector_2,
        universe_preview=ui.universe_preview_2,
        character_selector=ui.character_selector_2,
        character_preview=ui.character_preview_2,
        expression_selector=ui.expression_selector_2,
        expression_preview=ui.expression_preview_2,
        alternating_selector=ui.alternating_right_selector,
        alternating_preview=ui.alternating_right_preview,
        include_checkbox=ui.include_checkbox_2,
        expression_color_selector=ui.expression_color_selector_2,
        expression_color_preview=ui.expression_color_preview_2,
        alternating_container=ui.alternating_everything_right,
        alternating_lines=[ui.line_70, ui.line_71, ui.line_72],
    )
    return left, right

def connect_generator(ui: Ui_MainWindow):
    left, right = make_sides(ui)

    def helper(selector: QComboBox, fn: Callable):
        selector.activated.connect(lambda: update_with_function_then_regenerate(ui, fn))

    # Colors
    helper(ui.border_color_selector,
           lambda: set_border_color(ui.input,
                                    ui.border_color_selector.currentData(),
                                    ui.border_color_preview))
    for sel, prev in [
        (ui.asterisk_color_selector_1, ui.asterisk_color_preview_1),
        (ui.asterisk_color_selector_2, ui.asterisk_color_preview_2),
        (ui.asterisk_color_selector_3, ui.asterisk_color_preview_3),
    ]:
        helper(sel, lambda s=sel, p=prev: set_color(s.currentData(), p))

    for side in (left, right):
        helper(side.expression_color_selector,
               lambda s=side: set_color(s.expression_color_selector.currentData(),
                                        s.expression_color_preview))
        set_stylesheet(side.expression_selector)
        set_stylesheet(side.alternating_selector)

    # Border style
    helper(ui.border_style_selector,
           lambda: set_border_style(ui.border_style_selector.currentData(),
                                    ui.border_style_preview))

    # Entity selectors — both sides via shared logic
    for manager, side in ((left_manager, left), (right_manager, right)):
        connect_side(ui, manager, side)

    # Asterisk
    ui.asterisk_checkbox.clicked.connect(
        lambda: update_with_function_then_regenerate(ui, lambda: hide_or_show(ui))
    )

    # Alternating visibility toggles
    ui.include_checkbox.clicked.connect(lambda: check_for_alternating(ui, left))
    ui.include_checkbox_2.clicked.connect(lambda: check_for_alternating(ui, right))

    # Format / size / misc
    ui.font_selector.activated.connect(lambda: try_generate(ui))
    ui.default_color_selector.activated.connect(
        lambda: update_with_function_then_regenerate(ui,
            lambda: set_color(ui.default_color_selector.currentData(),
                              ui.default_color_preview))
    )
    ui.text_style_regular_option.toggled.connect(lambda c: on_radio_changed(ui, c))
    ui.text_style_dark_world_option.toggled.connect(lambda c: on_radio_changed(ui, c))
    ui.text_transform_selector.activated.connect(lambda: try_generate(ui))
    ui.format_png_option.toggled.connect(lambda c: png_checked(ui, c, left, right))
    ui.format_gif_option.toggled.connect(lambda c: gif_checked(ui, c, left, right))
    ui.margin_checkbox.clicked.connect(lambda: try_generate(ui))
    ui.size_small_option.toggled.connect(lambda c: on_radio_changed(ui, c))
    ui.size_medium_option.toggled.connect(lambda c: on_radio_changed(ui, c))
    ui.size_big_option.toggled.connect(lambda c: on_radio_changed(ui, c))

    ui.input.textChanged.connect(lambda: try_generate(ui))

    ui.debounce_timer = QTimer()
    ui.debounce_timer.setSingleShot(True)
    ui.debounce_timer.timeout.connect(lambda: execute_generation(ui, left, right))

    ui.download.clicked.connect(lambda: download(ui))

    ui.copy_to_clipboard.clicked.connect(lambda: on_copy(ui))

def on_copy(ui: Ui_MainWindow):
    worked = copy_to_clipboard(ui.output)
    if not worked:
        return
    ui.copy_to_clipboard.setText("Copied!")
    QTimer.singleShot(1500, lambda: ui.copy_to_clipboard.setText("Copy to Clipboard"))

def copy_to_clipboard(output: QLabel) -> bool:
    pixmap = output.movie().currentPixmap() if output.movie() else output.pixmap()
    if pixmap and not pixmap.isNull() and not output.text():
        QGuiApplication.clipboard().setPixmap(pixmap)
        return True
    return False

def connect_side(ui: Ui_MainWindow, manager: SelectionManager, side: SideSelectors):
    def helper(selector: QComboBox, fn: Callable):
        selector.activated.connect(lambda: update_with_function_then_regenerate(ui, fn))

    helper(side.universe_selector,  lambda: universe_change(ui, manager, side))
    helper(side.character_selector, lambda: character_change(ui, manager, side))
    helper(side.expression_selector, lambda: expression_change(manager, side))
    helper(side.alternating_selector, lambda: alternate_change(manager, side))

def png_checked(ui: Ui_MainWindow, change: bool,
                 left: SideSelectors, right: SideSelectors):
    hide_alternating(left)
    hide_alternating(right)
    on_radio_changed(ui, change)


def gif_checked(ui: Ui_MainWindow, change: bool,
                 left: SideSelectors, right: SideSelectors):
    for side in (left, right):
        if side.include_checkbox.isChecked():
            show_alternating(side)
    on_radio_changed(ui, change)


def check_for_alternating(ui: Ui_MainWindow, side: SideSelectors):
    if ui.format_gif_option.isChecked() and side.include_checkbox.isChecked():
        show_alternating(side)
    else:
        hide_alternating(side)
    try_generate(ui)


def on_radio_changed(ui: Ui_MainWindow, checked: bool):
    if checked:
        try_generate(ui)

def try_generate(ui: Ui_MainWindow):
    if hasattr(ui, "debounce_timer"):
        ui.debounce_timer.start(300)

def update_with_function_then_regenerate(ui: Ui_MainWindow, function: Callable):
    function()
    try_generate(ui)

def universe_change(ui: Ui_MainWindow, manager: SelectionManager, side: SideSelectors):
    manager.set_selected_universe(side.universe_selector.currentData())
    manager.try_to_select_first_character_from_current_universe()
    manager.try_to_select_first_expression_from_current_character()
    reset_selectors(ui, manager, side)
    set_universe_default_border(ui)

def character_change(ui: Ui_MainWindow, manager: SelectionManager, side: SideSelectors):
    manager.set_selected_character(side.character_selector.currentData())
    set_defaults(manager.get_selected_character(), ui)
    manager.try_to_select_first_expression_from_current_character()
    reset_selectors(ui, manager, side)

def expression_change(manager: SelectionManager, side: SideSelectors):
    manager.set_selected_expression(side.expression_selector.currentData())
    manager.try_to_init_alternating_expression()

    target = side.expression_selector.currentData()
    for i in range(side.alternating_selector.count()):
        if side.alternating_selector.itemData(i).expression_id == target.expression_id:
            side.alternating_selector.setCurrentIndex(i)
            break

    set_preview_generator_version(manager.get_alternating_expression(), side.alternating_preview)
    set_preview_generator_version(manager.get_selected_expression(),    side.expression_preview)

def alternate_change(manager: SelectionManager, side: SideSelectors):
    manager.set_alternating_expression(side.alternating_selector.currentData())
    set_preview_generator_version(manager.get_alternating_expression(), side.alternating_preview)

"""
1. Wipe universe/character/expression selector
2. Load universes into select (sorted)
Universes, characters and expressions are added dynamically
"""
def reload_ui(ui: Ui_MainWindow, left: SideSelectors, right: SideSelectors):
    reset_selectors(ui, left_manager,  left)
    reset_selectors(ui, right_manager, right,)
    set_universe_default_border(ui)
    try_generate(ui)

def reset_selectors(ui: Ui_MainWindow, manager: SelectionManager, side: SideSelectors):
    db = get_db()

    for selector, preview in [
        (side.universe_selector,   side.universe_preview),
        (side.character_selector,  side.character_preview),
        (side.expression_selector, side.expression_preview),
        (side.alternating_selector, side.alternating_preview),
    ]:
        selector.clear()
        preview.clear()

    if not init_entity(db.select_all_universes,
                       side.universe_selector, side.universe_preview,
                       manager.get_selected_universe()):
        manager.reset()
        return

    universe_id = side.universe_selector.currentData().universe_id
    if not init_entity(lambda: db.select_all_characters_from_universe(universe_id),
                       side.character_selector, side.character_preview,
                       manager.get_selected_character()):
        manager.set_selected_character(None)
        manager.set_selected_expression(None)
        return

    character_id = side.character_selector.currentData().character_id
    has_expressions = init_entity(
        lambda: db.select_all_expressions_from_character(character_id),
        side.expression_selector, side.expression_preview,
        manager.get_selected_expression(),
    )

    manager.set_selected_universe(side.universe_selector.currentData())
    manager.set_selected_character(side.character_selector.currentData())

    set_defaults(left_manager.get_selected_character(), ui)

    if has_expressions:
        manager.set_selected_expression(side.expression_selector.currentData())
        init_entity(
            lambda: db.select_all_expressions_from_character(character_id),
            side.alternating_selector, side.alternating_preview,
            manager.get_selected_expression(),
        )
        manager.try_to_init_alternating_expression()
    else:
        manager.set_selected_expression(None)

def set_universe_default_border(ui: Ui_MainWindow):
    universe = ui.universe_selector.currentData()
    if universe is not None:
        ui.border_style_selector.setCurrentIndex(universe.default_border_style - 1)
        set_border_style(ui.border_style_selector.currentData(), ui.border_style_preview)

def get_db():
    return DBDynamicConnection.get_instance()