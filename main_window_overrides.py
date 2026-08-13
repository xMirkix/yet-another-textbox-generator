import shutil
import zipfile
from pathlib import Path

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMessageBox

from configs.paths import DYNAMIC_DB
from running.connection.welcome import save_file_without_ui, open_logic
from services.change_service import Changes
from services.database_service import DBDynamicConnection
from services.selection_manager import left_manager


db_path = DYNAMIC_DB

def _unzip_db_from(path: str):
    with zipfile.ZipFile(path, "r") as zf:
        with zf.open("data.db") as src, open(db_path, "wb") as dst:
            shutil.copyfileobj(src, dst)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = None


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and urls[0].toLocalFile().lower().endswith(".yatg"):
                event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        path = event.mimeData().urls()[0].toLocalFile()
        if path and self.ui is not None:
            open_logic(self.ui, path)
            return True
        event.acceptProposedAction()

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
                if save_file_without_ui():
                    db = DBDynamicConnection.get_instance()
                    db.delete_all_tables()
                    db.connection.close()

                    QApplication.quit()
                else:
                    event.ignore()
            elif reply == QMessageBox.StandardButton.Discard:
                db = DBDynamicConnection.get_instance()
                db.delete_all_tables()
                db.connection.close()

                QApplication.quit()
            elif reply == QMessageBox.StandardButton.Cancel:
                event.ignore()
        else:
            db = DBDynamicConnection.get_instance()
            db.delete_all_tables()
            db.connection.close()

            event.accept()