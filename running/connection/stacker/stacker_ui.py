from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QWidget

from configs.paths import ICON_UP, ICON_DELETE, ICON_DOWN
from generation.generation_request import GenerationRequest
from models.entities import Expression
from running.connection.stacker import stacker
from running.connection.stacker.eliding_label import ElidingLabel
from services.color_service import fit_expression_image
from services.selection_manager import stack_manager
from ui.generated_ui import Ui_MainWindow


def blob_to_pixmap(blob: bytes) -> QPixmap:
    pixmap = QPixmap()
    pixmap.loadFromData(blob)
    return pixmap


def create_stack_frame(ui: Ui_MainWindow, expression: Expression | None, text: str) -> QFrame:
    frame = QFrame(ui.scrollAreaWidgetContents)
    frame.setFrameShape(QFrame.Shape.Panel)
    frame.setFrameShadow(QFrame.Shadow.Plain)
    frame.setSizePolicy(QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed))

    frame.setMinimumSize(QSize(450, 230))

    v_layout = QVBoxLayout(frame)
    h_layout = QHBoxLayout()
    h_layout.setContentsMargins(5, -1, 0, -1)

    h_layout.setSpacing(15)

    # Expression preview
    content_label = QLabel(frame)
    content_label.setFixedSize(QSize(69, 70))
    content_label.setAutoFillBackground(True)
    if expression is not None:
        content_label.setPixmap(blob_to_pixmap(fit_expression_image(expression.preview_image)))
    else:
        content_label.setText("Empty")
        content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    h_layout.addWidget(content_label)

    # Text preview
    input_label = ElidingLabel(text, frame)
    input_label.setMinimumHeight(100)
    #input_label.setMinimumSize(QSize(300, 100))
    input_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    input_label.setWordWrap(True)
    input_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

    font = QFont()
    font.setPointSize(14)
    font.setWeight(QFont.Weight.DemiBold)
    input_label.setFont(font)

    h_layout.addWidget(input_label)

    # Up / Delete / Down
    button_layout = QVBoxLayout()
    button_layout.setSpacing(10)
    button_layout.setContentsMargins(0, 50, 0, 50)

    up_button = QPushButton(QIcon(str(ICON_UP)),"", frame)
    up_button.setFixedSize(80, 30)
    up_button.setIconSize(QSize(24, 24))
    delete_button = QPushButton(QIcon(str(ICON_DELETE)), "", frame)
    delete_button.setFixedSize(80, 30)
    delete_button.setIconSize(QSize(24, 24))
    down_button = QPushButton(QIcon(str(ICON_DOWN)), "", frame)
    down_button.setFixedSize(80, 30)
    down_button.setIconSize(QSize(24, 24))

    for btn in (up_button, delete_button, down_button):
        button_layout.addWidget(btn)
    h_layout.addLayout(button_layout)
    v_layout.addLayout(h_layout)

    up_button.clicked.connect(lambda: move_stack_entry(ui, frame, -1))
    down_button.clicked.connect(lambda: move_stack_entry(ui, frame, 1))
    delete_button.clicked.connect(lambda: remove_from_stack(ui, frame))

    return frame


def move_stack_entry(ui: Ui_MainWindow, frame: QFrame, direction: int):
    contents = ui.verticalLayout_30

    position = frame.property("position")

    new_position = position + direction

    if new_position < 0 or new_position >= contents.count():
        return

    other_item = contents.itemAt(new_position)
    other_frame: QWidget | None = other_item.widget() if other_item else None

    if other_frame is None:
        return

    stack_manager.move_item(position, new_position)

    contents.removeWidget(frame)
    contents.insertWidget(new_position, frame)

    frame.setProperty("position", new_position)
    other_frame.setProperty("position", position)

    stacker.try_generate(ui)


def remove_from_stack(ui: Ui_MainWindow, frame: QFrame):
    contents = ui.verticalLayout_30
    position = frame.property("position")

    stack_manager.delete_item(position)

    contents.removeWidget(frame)
    frame.hide()
    frame.deleteLater()

    for i in range(position, contents.count()):
        item = contents.itemAt(i)
        widget: QWidget | None = item.widget() if item else None
        if widget is not None:
            widget.setProperty("position", i)

    stacker.try_generate(ui)


def add_to_stack(ui: Ui_MainWindow, request: GenerationRequest) -> QFrame:
    frame = create_stack_frame(ui, request.sprite_settings.expression, request.text_input)

    frame.setProperty("position", ui.verticalLayout_30.count())

    ui.verticalLayout_30.addWidget(frame)
    stack_manager.insert_new(request)

    return frame
