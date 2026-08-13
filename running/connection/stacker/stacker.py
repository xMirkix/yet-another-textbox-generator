import shutil
from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap, QGuiApplication
from PySide6.QtWidgets import QFileDialog, QMessageBox, QLabel

from models.form_bindings import ExportFormat
from running.connection.generator.generation_calls import make_request
from running.connection.stacker import stacker_ui
from running.connection.stacker.stacker_proxy import stack_cache
from ui.generated_ui import Ui_MainWindow
from services.selection_manager import stack_manager, make_sides


def connect_stacker(ui: Ui_MainWindow):
    ui.add_textboxes.clicked.connect(lambda: ui.tabs.setCurrentIndex(1))

    def add_current():
        stacker_ui.add_to_stack(ui, ui.add_current_box.property("current_request"))
        ui.download_stack.show()
        ui.actionDownload_Textbox_Stack.setEnabled(True)
        ui.copy_to_clipboard_stack.show()
        ui.actionCopy_Stack_to_Clipboard.setEnabled(True)
        ui.add_textboxes.hide()
        try_generate(ui)

    ui.add_current_box.clicked.connect(lambda: add_current())
    ui.amount_of_columns.valueChanged.connect(lambda: try_generate(ui))
    ui.download_stack.clicked.connect(lambda: download(ui))
    ui.copy_to_clipboard_stack.clicked.connect(lambda: copy_to_clipboard(ui))

    ui.debounce_timer_stack = QTimer()
    ui.debounce_timer_stack.setSingleShot(True)
    ui.debounce_timer_stack.timeout.connect(lambda: generate_stack(ui))


def try_generate(ui):
    if hasattr(ui, "debounce_timer_stack"):
        ui.debounce_timer_stack.start(300)


def generate_stack(ui: Ui_MainWindow):
    column_amount: int = ui.amount_of_columns.value()

    stack = stack_manager.get_stack()

    result = stack_cache.get_stack_image(column_amount, stack, stack_manager.has_deltarune_border())

    if result is None:
        ui.output_stack.clear()
        return

    ui.download_stack.setProperty("path", result)
    ui.output_stack.setPixmap(QPixmap(str(result)))


def reload_ui(ui: Ui_MainWindow):
    ui.add_current_box.hide()
    ui.add_textboxes.hide()
    ui.download_stack.hide()
    ui.actionDownload_Textbox_Stack.setEnabled(False)
    ui.copy_to_clipboard_stack.hide()
    ui.actionCopy_Stack_to_Clipboard.setEnabled(False)
    left, right = make_sides(ui)
    check = make_request(ui, left, right)

    if check is not None and check.export_settings.export_format != ExportFormat.GIF:
        ui.add_current_box.show()
        ui.add_current_box.setProperty("current_request", check)

    if len(stack_manager.get_stack()) == 0:
        ui.add_textboxes.show()
    else:
        ui.download_stack.show()
        ui.actionDownload_Textbox_Stack.setEnabled(True)
        ui.copy_to_clipboard_stack.show()
        ui.actionCopy_Stack_to_Clipboard.setEnabled(True)


def hide_initial(ui: Ui_MainWindow):
    ui.add_current_box.hide()
    ui.download_stack.hide()
    ui.actionDownload_Textbox_Stack.setEnabled(False)
    ui.copy_to_clipboard_stack.hide()
    ui.actionCopy_Stack_to_Clipboard.setEnabled(False)

def on_delete_empty(ui: Ui_MainWindow):
    reload_ui(ui)


def download(ui: Ui_MainWindow):
    source: Path | None = ui.download_stack.property("path")
    if source is None:
        return

    suffix = source.suffix
    path, _ = QFileDialog.getSaveFileName(
        caption="Save",
        filter="PNG (*.png)",
        options=QFileDialog.Option.DontConfirmOverwrite,
    )
    if not path:
        return
    if not path.endswith(suffix):
        path += suffix

    if Path(path).exists():
        reply = QMessageBox.warning(
            None, "Save",
            f'"{Path(path).name}" already exists.\nDo you want to replace it?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

    shutil.copyfile(source, path)

def copy_to_clipboard(ui: Ui_MainWindow):
    worked = copy_to_clipboard_helper(ui.output_stack)
    if not worked:
        return
    ui.copy_to_clipboard_stack.setText("Copied!")
    QTimer.singleShot(1500, lambda: ui.copy_to_clipboard_stack.setText("Copy to Clipboard"))

def copy_to_clipboard_helper(output: QLabel) -> bool:
    pixmap = output.pixmap()
    if pixmap and not pixmap.isNull() and not output.text():
        QGuiApplication.clipboard().setPixmap(pixmap)
        return True
    return False
