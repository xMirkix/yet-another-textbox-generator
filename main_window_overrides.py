from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMessageBox
from pathlib import Path

from running.connection.welcome import save_file
from static.change_service import Changes

BASE_DIR = Path(__file__).parent
db_path = BASE_DIR / "assets" / "temp_dynamic_data" / "temp_data.sqlite3"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = None

    def closeEvent(self, event: QCloseEvent):
        if Changes.get_state():
            reply = QMessageBox.question(
                self,
                "Warning!",
                "There are unsaved changes, quit anyway?",
                QMessageBox.StandardButton.Save |
                QMessageBox.StandardButton.Discard |
                QMessageBox.StandardButton.Cancel
            )
            if reply == QMessageBox.StandardButton.Save:
                if save_file():
                    db_path.unlink(missing_ok=True)
                    QApplication.quit()
                else:
                    event.ignore()
            elif reply == QMessageBox.StandardButton.Discard:
                db_path.unlink(missing_ok=True)
                QApplication.quit()
            elif reply == QMessageBox.StandardButton.Cancel:
                event.ignore()
        else:
            db_path.unlink(missing_ok=True)
            event.accept()