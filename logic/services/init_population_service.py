from ui.generated_ui import Ui_MainWindow
import sqlite3
from pathlib import Path
import PySide6.QtGui

DB_PATH = Path(__file__).parent.parent.parent / 'models' / 'in_memory' / 'static_data.sqlite3'
IMAGE_PATH = Path(__file__).parent.parent.parent / 'undertale_preview.png'
COLOR_IMAGE_PATH = Path(__file__).parent.parent.parent / 'white_preview.png'


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

        styles = self.connection.execute("""
                                         SELECT *
                                         FROM BorderStyles;
                                         """).fetchall()

        for row in styles:
            ui.border_style_selector.addItem(row[1])

        ui.border_style_preview.setPixmap(PySide6.QtGui.QPixmap(str(IMAGE_PATH)))

        colors = self.connection.execute("""
                                         SELECT *
                                         FROM Colors;
                                         """).fetchall()

        for row in colors:
            ui.border_color_selector.addItem(row[1])

        ui.border_color_preview.setPixmap(PySide6.QtGui.QPixmap(str(COLOR_IMAGE_PATH)))

    def populate_sprite_settings(self, ui: Ui_MainWindow):

        colors = self.connection.execute("""
                                         SELECT *
                                         FROM Colors;
                                         """)

        for row in colors:
            ui.expression_color_selector.addItem(row[1])

        ui.expression_color_preview.setPixmap(PySide6.QtGui.QPixmap(str(COLOR_IMAGE_PATH)))

    def populate_font_settings(self, ui: Ui_MainWindow):
        fonts = self.connection.execute("""
                                        SELECT *
                                        FROM Fonts;
                                        """).fetchall()

        for row in fonts:
            ui.font_selector.addItem(row[1])

        colors = self.connection.execute("""
                                         SELECT *
                                         FROM Colors;
                                         """).fetchall()

        for row in colors:
            ui.asterisk_color_selector_1.addItem(row[1])
            ui.asterisk_color_selector_2.addItem(row[1])
            ui.asterisk_color_selector_3.addItem(row[1])

        ui.asterisk_color_preview_1.setPixmap(PySide6.QtGui.QPixmap(str(COLOR_IMAGE_PATH)))
        ui.asterisk_color_preview_2.setPixmap(PySide6.QtGui.QPixmap(str(COLOR_IMAGE_PATH)))
        ui.asterisk_color_preview_3.setPixmap(PySide6.QtGui.QPixmap(str(COLOR_IMAGE_PATH)))

        transforms = self.connection.execute("""
        SELECT * FROM Transforms;
        """).fetchall()

        for row in transforms:
            ui.text_transform_selector.addItem(row[1])

    def hide_universes_edit(self, ui: Ui_MainWindow):
        ui.edit_universe.hide()

    def hide_characters_edit(self, ui: Ui_MainWindow):
        ui.edit_character.hide()

    def hide_expressions_edit(self, ui: Ui_MainWindow):
        ui.edit_expression.hide()
