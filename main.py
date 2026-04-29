from PySide6.QtWidgets import QApplication, QMainWindow
from pathlib import Path

from main_window_overrides import MainWindow
from static.app_memory import Memory
from models.form_bindings import BorderSettings, SpriteSettings, FontSettings, ExportSettings
from running.ui_connection_service import connect_ui
from startup.init_population_service import InitPopulationService
from ui.generated_ui import Ui_MainWindow

BASE_DIR = Path(__file__).parent
db_path = BASE_DIR / "assets" / "temp_dynamic_data" / "temp_data.sqlite3"

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window) # Define UI from generated file
    window.ui = ui

    db_path.unlink(missing_ok=True) # Delete possible existing file from unexpected exit
    db_path.touch() # Create cache file

    # Initialize Memory
    memory = Memory(input_prompt="",
        border_settings=BorderSettings(1, 1), #UT, White
        sprite_settings=SpriteSettings(-1, -1, -1, 1), # Nothing set, only color
        font_settings=FontSettings(1, True, [1,1,1], "Regular", 1), # Has asterisk, white colors and Regular with no transform
        export_settings=ExportSettings("PNG", True, "Medium"), # PNG with medium size and margin)
        ui=window.ui
    )

    p = InitPopulationService()
    p.init_populate(ui) # Initialize/Populate UI with data from Files (e.g. Colors)

    connect_ui(ui) # Connect UI to Logic Code, Respond to input


    window.show()
    app.exec()
