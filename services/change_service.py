import base64

from PySide6.QtCore import QBuffer, QByteArray
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QFileDialog, QLabel, QPushButton, QMessageBox


def pixmap_to_base64(pixmap: QPixmap) -> str:
    buffer = QBuffer()
    buffer.open(QBuffer.OpenModeFlag.WriteOnly)
    pixmap.save(buffer, "PNG")
    return base64.b64encode(buffer.data()).decode("utf-8")


def base64_to_pixmap(base64_str: str) -> QPixmap:
    byte_array = QByteArray.fromBase64(base64_str.encode("utf-8"))
    pixmap = QPixmap()
    pixmap.loadFromData(byte_array)
    return pixmap

def select_image(preview: QLabel, remove_button: QPushButton, width: int = 69, height: int = 70):
    path, _ = QFileDialog.getOpenFileName(
        caption="Choose Image",
        filter="PNG Pictures (*.png)"
    )
    if not path:
        return  # Nothing selected

    image = QImage(path)
    if image.width() > width or image.height() > height:
        QMessageBox.warning(None, "Invalid Picture", f"Picture size cannot exceed the resolution {width}x{height} (current: {image.width()}x{image.height()})")
        return

    preview.setPixmap(QPixmap(image))
    remove_button.show()

def remove_image(preview: QLabel, remove_button: QPushButton):
    preview.clear()
    preview.setText("Nothing...")
    remove_button.hide()

class Changes:
    _changed = False
    current_selected_file = None

    @classmethod
    def saved(cls):
        cls._changed = False

    @classmethod
    def reset(cls):
        cls._changed = False

    @classmethod
    def change(cls):
        cls._changed = True

    @classmethod
    def get_state(cls) -> bool:
        return cls._changed

    @classmethod
    def set_current_selected_file(cls, file_path: str):
        cls.current_selected_file = file_path

    @classmethod
    def get_current_selected_file(cls) -> str | None:
        return cls.current_selected_file