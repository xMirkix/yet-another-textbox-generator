import colorsys
from typing import Callable

from PySide6.QtCore import QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QComboBox, QLabel, QPushButton

from models.entities import Character, Universe, Expression
from models.form_bindings import ColorType
from running.connection.generator.generation_calls import execute_generation, make_request
from running.connection.generator.generator_utils import set_color, set_border_style, set_stylesheet, set_defaults, \
    set_preview_generator_version, set_border_color, show_alternating, \
    hide_alternating, hide_or_show, download
from running.connection.stacker import stacker, stacker_ui
from services.color_service import bytes_to_image, get_primary_color, is_similar
from services.color_window_service import create_color_window
from services.database_service import DBDynamicConnection
from services.new_window_service import connect_universe_create, connect_character_create, \
    connect_expression_create, connect_alt_expression
from services.selection_manager import SelectionManager, init_entity, SideSelectors, left_manager, right_manager, \
    select_entity_in_combo
from startup.in_memory.static_classes import Color
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
        color_type_selector=ui.expression_color_type_selector,
        color_type_button=ui.expression_color_type_button,
        color_type_everything= [ui.expression_color_type_selector,
                                ui.expression_color_type_label,
                                ui.expression_color_type_button,
                                ui.line_79,
                                ui.line_80,
                                ui.label_left,
                                ui.label_right
                                ],
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
        color_type_selector=ui.expression_color_type_selector_2,
        color_type_button=ui.expression_color_type_button_2,
        color_type_everything=[ui.expression_color_type_selector_2,
                               ui.expression_color_type_label_2,
                               ui.expression_color_type_button_2,
                               ui.line_37,
                               ui.line_82,
                               ui.label_left_2,
                               ui.label_right_2
                               ],
        alternating_container=ui.alternating_everything_right,
        alternating_lines=[ui.line_70, ui.line_71, ui.line_72],
    )
    return left, right



def connect_generator(ui: Ui_MainWindow):

    def post_universe_fn(universe: Universe, man: SelectionManager):
        man.set_selected_universe(universe)
        reload_ui(ui, True, left, right)

    def post_character_fn(character: Character, man: SelectionManager):
        man.set_selected_character(character)
        reload_ui(ui, True, left, right)

    def post_expression_fn(expression: Expression, man: SelectionManager):
        man.set_selected_expression(expression)
        reload_ui(ui, False, left, right)

    connect_universe_create(ui, ui.all_universes, left_manager, post_universe_fn)
    connect_character_create(ui, ui.all_characters, left_manager, post_character_fn)
    connect_expression_create(ui, ui.all_expressions, left_manager, post_expression_fn)

    connect_universe_create(ui, ui.all_universes_2, right_manager, post_universe_fn)
    connect_character_create(ui, ui.all_characters_2, right_manager, post_character_fn)
    connect_expression_create(ui, ui.all_expressions_2, right_manager, post_expression_fn)

    left, right = make_sides(ui)

    def post_alt_expression_fn(expression: Expression, man: SelectionManager, sel_side: SideSelectors, selector: QComboBox):
        man.set_alternating_expression(expression)
        select_entity_in_combo(selector, expression)
        set_preview_generator_version(expression, sel_side.alternating_preview)
        try_generate(ui)

    connect_alt_expression(ui, ui.all_expressions_alt, left_manager, post_alt_expression_fn, left, ui.alternating_selector)
    connect_alt_expression(ui, ui.all_expressions_alt_2, right_manager, post_alt_expression_fn, right, ui.alternating_right_selector)

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

    def create_window(man: SelectionManager):
        included, excluded, simple = create_color_window(ui, man.get_color_manager().get_selected_colors(),
                            man.get_color_manager().get_excluded_colors(), man.get_color_manager().get_simple_recoloring())
        man.get_color_manager().set_selected_colors(tuple(included))
        man.get_color_manager().set_excluded_colors(tuple(excluded))
        man.get_color_manager().set_simple_recoloring(simple)
        try_generate(ui)

    ui.expression_color_type_button.clicked.connect(lambda: create_window(left_manager))
    ui.expression_color_type_button_2.clicked.connect(lambda: create_window(right_manager))


    helper(ui.expression_color_type_selector, lambda: left_manager.get_color_manager().set_selected_color_type(ui.expression_color_type_selector.currentData()))

    helper(ui.expression_color_type_selector_2, lambda: right_manager.get_color_manager().set_selected_color_type(ui.expression_color_type_selector.currentData()))

    left.expression_color_selector.activated.connect(lambda: show_type_if_valid(left))
    right.expression_color_selector.activated.connect(lambda: show_type_if_valid(right))

    def color_button_enabling(affected_side: SideSelectors, man: SelectionManager, selector: QComboBox, button: QPushButton):
        enabled = selector.currentData() == ColorType.CUSTOM
        if enabled and man.get_color_manager().get_selected_colors() is None:
            colors, excluded = try_to_set_simple_colors(affected_side)
            man.get_color_manager().set_selected_colors(tuple(colors))
            man.get_color_manager().set_excluded_colors(tuple(excluded))
            man.get_color_manager().set_simple_recoloring(True)
        button.setEnabled(enabled)
        try_generate(ui)

    helper(ui.expression_color_type_selector, lambda: color_button_enabling(left, left_manager, ui.expression_color_type_selector, ui.expression_color_type_button))
    helper(ui.expression_color_type_selector_2, lambda: color_button_enabling(right, right_manager, ui.expression_color_type_selector_2, ui.expression_color_type_button_2))

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

    def add_to_stack():
        req = make_request(ui, left, right)
        if req is None:
            return
        stacker_ui.add_to_stack(ui, req)
        stacker.generate_stack(ui)

    ui.add_to_stack.clicked.connect(lambda: add_to_stack())

    ui.input.textChanged.connect(lambda: try_generate(ui))

    ui.debounce_timer = QTimer()
    ui.debounce_timer.setSingleShot(True)
    ui.debounce_timer.timeout.connect(lambda: execute_generation(ui, left, right))

    ui.download.clicked.connect(lambda: download(ui))

    ui.copy_to_clipboard.clicked.connect(lambda: on_copy(ui))

def try_to_set_simple_colors(side: SideSelectors) -> tuple[list[Color], list[Color]]:
    color_list = []
    excluded_list = []
    affected_expression: Expression = side.expression_selector.currentData()
    image = bytes_to_image(affected_expression.preview_image)
    primary = get_primary_color(image)
    if primary is None:
        return [], []

    pr, pg, pb = primary
    primary_color = Color(-1, "", pr, pg, pb, 255)
    color_list.append(primary_color)

    hp, sp, vp = colorsys.rgb_to_hsv(pr / 255, pg / 255, pb / 255)
    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = pixels[x, y]
            if a == 0: # skip transparent pixels
                continue
            if (r, g, b) == (0, 0, 0): # skip black pixels
                continue

            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

            color = Color(-1, "", r, g, b, a)
            if is_similar((hp, sp, vp), (h, s, v), 0.08, 0.25): # color is not distinct enough and gets included
                try:
                    color_list.index(color)
                except ValueError:
                    color_list.append(color)
            else:
                try:
                    excluded_list.index(color)
                except ValueError:
                    excluded_list.append(color)

    return color_list, excluded_list


def show_type_if_valid(side):
    if side.expression_selector.currentData() is None: # no expression exists
        for item in side.color_type_everything:
            item.hide()
        side.expression_color_selector.setEnabled(False)
        return

    if side.expression_color_selector.currentData() is None: # no changes
        for item in side.color_type_everything:
            item.hide()
        side.expression_color_selector.setEnabled(True)
        return

    for item in side.color_type_everything:
        item.show()
    side.expression_color_selector.setEnabled(True)

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
def reload_ui(ui: Ui_MainWindow, reset_color_things: bool, left: SideSelectors, right: SideSelectors):
    reset_selectors(ui, left_manager,  left, reset_color_things)
    reset_selectors(ui, right_manager, right, reset_color_things)
    set_universe_default_border(ui)
    try_generate(ui)

def reset_selectors(ui: Ui_MainWindow, manager: SelectionManager, side: SideSelectors, reset_color_things: bool = True):
    db = get_db()

    if reset_color_things:
        side.color_type_selector.setCurrentIndex(0)
        manager.get_color_manager().set_selected_color_type(side.color_type_selector.currentData())
        manager.get_color_manager().set_selected_colors(None)
        manager.get_color_manager().set_excluded_colors(None)
        manager.get_color_manager().set_simple_recoloring(None)
        side.color_type_button.setEnabled(False)

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
        show_type_if_valid(side)
        return

    universe_id = side.universe_selector.currentData().universe_id
    if not init_entity(lambda: db.select_all_characters_from_universe(universe_id),
                       side.character_selector, side.character_preview,
                       manager.get_selected_character()):
        manager.set_selected_character(None)
        manager.set_selected_expression(None)
        show_type_if_valid(side)
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
    show_type_if_valid(side)

def set_universe_default_border(ui: Ui_MainWindow):
    universe = ui.universe_selector.currentData()
    if universe is not None:
        ui.border_style_selector.setCurrentIndex(universe.default_border_style - 1)
        set_border_style(ui.border_style_selector.currentData(), ui.border_style_preview)

def get_db():
    return DBDynamicConnection.get_instance()