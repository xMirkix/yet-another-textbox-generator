import shutil
from io import BytesIO
from pathlib import Path

from PIL import Image
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QTextEdit, QFileDialog, QMessageBox

from configs.paths import PREVIEWS_DIR
from models.entities import Universe, Character, Expression
from services.color_service import fit_expression_image
from services.selection_manager import SideSelectors, set_preview
from startup.in_memory.static_classes import Color, BorderStyle
from ui.generated_ui import Ui_MainWindow


def darken(r: int, g: int, b: int, factor: float = 0.3) -> tuple[int, int, int]:
    return int(r * factor), int(g * factor), int(b * factor)


def set_color(color: Color | None, preview: QLabel):
    if color is None:
        preview.setStyleSheet("")
        return
    border = darken(color.r, color.g, color.b)
    if color.a == 0:
        preview.setStyleSheet("background-color: transparent; border: 2px dashed gray;")
    else:
        preview.setStyleSheet(
            f"background-color: rgb({color.r}, {color.g}, {color.b});"
            f"border: 2px solid rgb({border[0]}, {border[1]}, {border[2]});"
        )


def set_stylesheet(selector):
    selector.setStyleSheet("""
        QComboBox { combobox-popup: 0; }
        QComboBox QAbstractItemView { max-height: 320px; min-height: 100px; }
        QComboBox QAbstractItemView::item { min-height: 30px; padding: 4px; }
    """)


def set_border_style(style: BorderStyle, border_style_preview):
    path = PREVIEWS_DIR / f"{style.preview_file_name}.png"
    border_style_preview.setPixmap(QPixmap(str(path)))


def set_border_color(text_input: QTextEdit, color: Color, preview: QLabel):
    if color.a == 0:
        text_input.setStyleSheet("border: 2px dashed gray;")
    else:
        text_input.setStyleSheet(f"border: 2px solid rgb({color.r}, {color.g}, {color.b});")
    set_color(color, preview)


def set_preview_generator_version(entity: Universe | Character | Expression | None,
                                   preview: QLabel):
    if entity:
        formatter = fit_expression_image if isinstance(entity, Expression) else None
        set_preview(entity.preview_image, preview, entity, formatter)


def set_defaults(character, ui: Ui_MainWindow):
    if character is None:
        return
    ui.text_style_regular_option.setChecked(character.default_style == 1)
    ui.text_style_dark_world_option.setChecked(character.default_style == 2)
    ui.text_transform_selector.setCurrentIndex(character.default_text_transform - 1)
    ui.font_selector.setCurrentIndex(character.default_font - 1)


def show_alternating(side: SideSelectors):
    side.alternating_container.show()
    for line in side.alternating_lines:
        line.show()


def hide_alternating(side: SideSelectors):
    side.alternating_container.hide()
    for line in side.alternating_lines:
        line.hide()


def hide_or_show(ui: Ui_MainWindow):
    if ui.asterisk_checkbox.isChecked():
        ui.asterisk_color_everything.show()
        ui.asterisk_color_values_everything.show()
        ui.line_51.show(); ui.line_56.show()
        ui.line_50.show(); ui.line_55.show()
    else:
        ui.asterisk_color_everything.hide()
        ui.asterisk_color_values_everything.hide()
        ui.line_51.hide(); ui.line_56.hide()
        ui.line_50.hide(); ui.line_55.hide()


def download(ui: Ui_MainWindow):
    source: Path | None = ui.download.property("path")
    if source is None:
        return

    suffix = source.suffix
    path, _ = QFileDialog.getSaveFileName(
        caption="Save",
        filter="PNG (*.png)" if suffix == ".png" else "GIF (*.gif)",
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