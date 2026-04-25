from PySide6.QtWidgets import QComboBox, QLabel
from ui.generated_ui import Ui_MainWindow
import sqlite3
from pathlib import Path
import PySide6.QtGui

DB_PATH = Path(__file__).parent / 'in_memory' / 'static_data.sqlite3'
IMAGE_PATH = Path(__file__).parent.parent / 'assets' / 'previews' / 'undertale_preview.png'
COLOR_IMAGE_PATH = Path(__file__).parent.parent / 'assets' / 'previews' / 'white_preview.png'


class InitPopulationService:

    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

    def init_populate(self, ui: Ui_MainWindow):
        self.populate_border_settings(ui)  # Original/Deltarune/... and Color
        self.populate_sprite_settings(ui)  # Color
        self.populate_font_settings(ui)  # Determination Mono/Comic Sans/..., Asterisk Colors, Uppercase/Lowercase/...
        self.hide_universes_edit(ui)  # Hide edit block
        self.hide_characters_edit(ui)  # Hide edit block
        self.hide_expressions_edit(ui)  # Hide edit block

    def populate_border_settings(self, ui: Ui_MainWindow):
        self.query_db_and_set_ui("BorderStyles", [ui.border_style_selector], [ui.border_style_preview], IMAGE_PATH)
        self.query_db_and_set_ui("Colors", [ui.border_color_selector], [ui.border_color_preview], COLOR_IMAGE_PATH)

    def populate_sprite_settings(self, ui: Ui_MainWindow):
        self.query_db_and_set_ui("Colors", [ui.expression_color_selector], [ui.expression_color_preview], COLOR_IMAGE_PATH)

    def populate_font_settings(self, ui: Ui_MainWindow):
        self.query_db_and_set_ui("Fonts", [ui.font_selector], [], IMAGE_PATH)
        self.query_db_and_set_ui("Colors", [ui.asterisk_color_selector_1, ui.asterisk_color_selector_2, ui.asterisk_color_selector_3],
                                 [ui.asterisk_color_preview_1, ui.asterisk_color_preview_2, ui.asterisk_color_preview_3],
                                 COLOR_IMAGE_PATH)
        self.query_db_and_set_ui("Transforms", [ui.text_transform_selector], [], IMAGE_PATH)

    def query_db_and_set_ui(self, table_name: str, elements: list[QComboBox], pixmaps: list[QLabel], image_path: Path):
        rows = self.connection.execute(f"""
            SELECT * FROM {table_name}
        """).fetchall()

        for row in rows:
            for element in elements:
                element.addItem(row[1])

        for pixmap in pixmaps:
            pixmap.setPixmap(PySide6.QtGui.QPixmap(str(image_path)))

    def hide_universes_edit(self, ui: Ui_MainWindow):
        ui.edit_universe.hide()

    def hide_characters_edit(self, ui: Ui_MainWindow):
        ui.edit_character.hide()

    def hide_expressions_edit(self, ui: Ui_MainWindow):
        ui.edit_expression.hide()
