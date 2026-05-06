import base64

from PySide6.QtCore import QBuffer, QByteArray
from PySide6.QtGui import QPixmap


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


class Changes:
    _changed = False

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

