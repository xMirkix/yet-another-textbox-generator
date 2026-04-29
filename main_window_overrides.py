from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMessageBox

from running.connection.welcome import save_file
from static.change_service import Changes
from static.database_service import DBDynamicConnection

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
                    db = DBDynamicConnection.get_instance()
                    db.connection.close()

                    db_path = DBDynamicConnection.db_path
                    db_path.unlink(missing_ok=True)
                    QApplication.quit()
                else:
                    event.ignore()
            elif reply == QMessageBox.StandardButton.Discard:
                db = DBDynamicConnection.get_instance()
                db.connection.close()

                db_path = DBDynamicConnection.db_path
                db_path.unlink(missing_ok=True)
                QApplication.quit()
            elif reply == QMessageBox.StandardButton.Cancel:
                event.ignore()
        else:
            db = DBDynamicConnection.get_instance()
            db.connection.close()

            db_path = DBDynamicConnection.db_path
            db_path.unlink(missing_ok=True)
            event.accept()