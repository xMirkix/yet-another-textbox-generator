from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMessageBox

from running.connection.welcome import save_file
from static.change_service import Changes


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
                    QApplication.quit()
                else:
                    event.ignore()
            elif reply == QMessageBox.StandardButton.Discard:
                QApplication.quit()
            elif reply == QMessageBox.StandardButton.Cancel:
                event.ignore()
        else:
            event.accept()