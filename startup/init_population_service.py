from PySide6.QtWidgets import QComboBox, QLabel

from static.database_service import DBStaticConnection, DBDynamicConnection
from ui.generated_ui import Ui_MainWindow
from PySide6.QtGui import QFontDatabase
import PySide6.QtGui
from configs.paths import UNDERTALE_PREVIEW, WHITE_PREVIEW

IMAGE_PATH = UNDERTALE_PREVIEW
COLOR_IMAGE_PATH = WHITE_PREVIEW



class InitPopulationService:

    def __init__(self):
        self.connection = DBStaticConnection()
        self.dynamic_connection = DBDynamicConnection()

    def init_populate(self, ui: Ui_MainWindow):
        self.populate_border_settings(ui)  # Original/Deltarune/... and Color
        self.populate_sprite_settings(ui)  # Color
        self.populate_font_settings(ui)  # Determination Mono/Comic Sans/..., Asterisk Colors, Uppercase/Lowercase/...
        self.hide_edits(ui)  # Hide edit blocks
        self.create_temporary_data_tables()

    def populate_border_settings(self, ui: Ui_MainWindow):
        self.query_db_and_set_ui("BorderStyles", [ui.border_style_selector], [ui.border_style_preview], IMAGE_PATH)
        self.query_db_and_set_ui("Colors", [ui.border_color_selector], [ui.border_color_preview], COLOR_IMAGE_PATH)

    def populate_sprite_settings(self, ui: Ui_MainWindow):
        self.query_db_and_set_ui("Colors", [ui.expression_color_selector], [ui.expression_color_preview], COLOR_IMAGE_PATH)

    def populate_font_settings(self, ui: Ui_MainWindow):
        self.check_with_system_fonts("Fonts", [ui.font_selector])
        self.query_db_and_set_ui("Colors", [ui.asterisk_color_selector_1, ui.asterisk_color_selector_2, ui.asterisk_color_selector_3],
                                 [ui.asterisk_color_preview_1, ui.asterisk_color_preview_2, ui.asterisk_color_preview_3],
                                 COLOR_IMAGE_PATH)
        self.query_db_and_set_ui("Transforms", [ui.text_transform_selector], [], None)

    def query_db_and_set_ui(self, table_name: str, elements: list[QComboBox], pixmaps: list[QLabel], image_path: Path | None):
        rows = self.connection.select_table(table_name)

        for row in rows:
            for element in elements:
                element.addItem(row[1])

        for pixmap in pixmaps:
            pixmap.setPixmap(PySide6.QtGui.QPixmap(str(image_path)))

    def check_with_system_fonts(self, table_name: str, elements: list[QComboBox]):
        rows = self.connection.select_table(table_name)

        for row in rows:
            if self.is_font_installed(row[1]):
                for element in elements:
                    element.addItem(row[1])

    def is_font_installed(self, font_name: str) -> bool:
        return font_name in QFontDatabase.families()

    def hide_edits(self, ui: Ui_MainWindow):
        ui.edit_universe.hide()
        ui.edit_character.hide()
        ui.edit_expression.hide()

    def create_temporary_data_tables(self):
        self.dynamic_connection.create_all_tables()
