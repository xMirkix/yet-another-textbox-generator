from pathlib import Path

from PySide6.QtWidgets import QDialog, QFileDialog

from services.selection_manager import sound_manager
from ui.audio_ui import Ui_Dialog
from ui.generated_ui import Ui_MainWindow


class AudioSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Audio Settings")

        self.ui.mono_option.setChecked(sound_manager.get_mono()) # IF ONE SIDE IS NOT ENOUGH, SET STEREO OPTION TOO!!
        self.ui.stereo_option.setChecked(not sound_manager.get_mono())
        for w in (self.ui.volume_left_frame, self.ui.volume_right_frame):
            w.setVisible(not self.ui.mono_option.isChecked())

        self.ui.overlap_clips_left.setChecked(sound_manager.get_left_overlap())
        self.ui.overlap_clips_right.setChecked(sound_manager.get_right_overlap())
        self.ui.volume_slider.setValue(int(sound_manager.get_master_volume()))
        self.ui.volume_slider_left.setValue(int(sound_manager.get_left_volume()))
        self.ui.volume_slider_right.setValue(int(sound_manager.get_right_volume()))

        self.left: list[Path] = list(sound_manager.get_left_sound_files())
        self.right: list[Path] = list(sound_manager.get_right_sound_files())

        if len(self.left) > 0:
            self.ui.add_voice_clips_left.setText("Remove voice clip(s)")
        if len(self.right) > 0:
            self.ui.add_voice_clips_right.setText("Remove voice clip(s)")

        self.ui.add_voice_clips_left.clicked.connect(lambda: add_remove_voice_clips(self.ui, self.left, "left"))
        self.ui.add_voice_clips_right.clicked.connect(lambda: add_remove_voice_clips(self.ui, self.right, "right"))


        self.ui.ok_button.clicked.connect(lambda: self.accept())
        self.ui.cancel_button.clicked.connect(lambda: self.reject())

        self.ui.mono_option.toggled.connect(self._on_mono_toggled)
        self._on_mono_toggled(self.ui.mono_option.isChecked())

    def _on_mono_toggled(self, mono: bool):
        if mono:
            self.ui.volume_slider_left.setValue(100)
            self.ui.volume_slider_right.setValue(100)
        for w in (self.ui.volume_left_frame, self.ui.volume_right_frame):
            w.setVisible(not mono)




def create_audio_settings_window(ui: Ui_MainWindow) -> bool:
    dialog = AudioSettingsDialog(parent=ui.centralwidget.window())
    if dialog.exec() != QDialog.DialogCode.Accepted:
        return False

    d = dialog.ui
    mono = d.mono_option.isChecked()
    sound_manager.set_values(
        mono=mono,
        master_volume=d.volume_slider.value(),
        left_sound_files=list(dialog.left),
        right_sound_files=list(dialog.right),
        left_overlap=d.overlap_clips_left.isChecked(),
        right_overlap=d.overlap_clips_right.isChecked(),
        left_volume=100 if mono else d.volume_slider_left.value(),
        right_volume=100 if mono else d.volume_slider_right.value(),
    )
    return True

def add_remove_voice_clips(ui: Ui_Dialog, side: list[Path], indicator: str):
    button = ui.add_voice_clips_left if indicator == "left" else ui.add_voice_clips_right
    if side:
        side.clear()
        button.setText("Add voice clip(s)")
        return

    files, _ = QFileDialog.getOpenFileNames(
        button, "Select voice clip(s)", "",
        "Audio files (*.wav *.mp3 *.ogg *.flac *.m4a *.aac *.opus);;All files (*)"
    )
    if files:
        side.extend(Path(f) for f in files)
        button.setText("Remove voice clip(s)")
