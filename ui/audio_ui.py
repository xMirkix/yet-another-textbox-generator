# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audio_settingsIDGhTn.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(784, 443)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.mono_option = QRadioButton(self.groupBox)
        self.mono_option.setObjectName(u"mono_option")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mono_option.sizePolicy().hasHeightForWidth())
        self.mono_option.setSizePolicy(sizePolicy1)
        self.mono_option.setChecked(True)

        self.horizontalLayout_6.addWidget(self.mono_option)

        self.stereo_option = QRadioButton(self.groupBox)
        self.stereo_option.setObjectName(u"stereo_option")
        sizePolicy1.setHeightForWidth(self.stereo_option.sizePolicy().hasHeightForWidth())
        self.stereo_option.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.stereo_option)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_23)

        self.volume_slider = QSlider(self.frame_3)
        self.volume_slider.setObjectName(u"volume_slider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.volume_slider.sizePolicy().hasHeightForWidth())
        self.volume_slider.setSizePolicy(sizePolicy3)
        self.volume_slider.setMinimumSize(QSize(150, 0))
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(100)
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)
        self.volume_slider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.volume_slider.setTickInterval(10)

        self.horizontalLayout_2.addWidget(self.volume_slider)


        self.horizontalLayout_7.addWidget(self.frame_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addWidget(self.groupBox)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.left_char = QGroupBox(Dialog)
        self.left_char.setObjectName(u"left_char")
        self.left_char.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.left_char)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.overlap_clips_left = QCheckBox(self.left_char)
        self.overlap_clips_left.setObjectName(u"overlap_clips_left")
        sizePolicy3.setHeightForWidth(self.overlap_clips_left.sizePolicy().hasHeightForWidth())
        self.overlap_clips_left.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.overlap_clips_left)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.volume_left_frame = QFrame(self.left_char)
        self.volume_left_frame.setObjectName(u"volume_left_frame")
        sizePolicy1.setHeightForWidth(self.volume_left_frame.sizePolicy().hasHeightForWidth())
        self.volume_left_frame.setSizePolicy(sizePolicy1)
        self.volume_left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.volume_left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.volume_left_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_24 = QLabel(self.volume_left_frame)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_24)

        self.volume_slider_left = QSlider(self.volume_left_frame)
        self.volume_slider_left.setObjectName(u"volume_slider_left")
        sizePolicy3.setHeightForWidth(self.volume_slider_left.sizePolicy().hasHeightForWidth())
        self.volume_slider_left.setSizePolicy(sizePolicy3)
        self.volume_slider_left.setMinimumSize(QSize(150, 0))
        self.volume_slider_left.setMaximum(100)
        self.volume_slider_left.setValue(100)
        self.volume_slider_left.setOrientation(Qt.Orientation.Horizontal)
        self.volume_slider_left.setTickPosition(QSlider.TickPosition.NoTicks)
        self.volume_slider_left.setTickInterval(10)

        self.horizontalLayout_8.addWidget(self.volume_slider_left)


        self.horizontalLayout_10.addWidget(self.volume_left_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.add_voice_clips_left = QPushButton(self.left_char)
        self.add_voice_clips_left.setObjectName(u"add_voice_clips_left")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.add_voice_clips_left.sizePolicy().hasHeightForWidth())
        self.add_voice_clips_left.setSizePolicy(sizePolicy4)
        self.add_voice_clips_left.setMinimumSize(QSize(250, 0))
        self.add_voice_clips_left.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_12.addWidget(self.add_voice_clips_left)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_3.addWidget(self.left_char)

        self.line_3 = QFrame(Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.right_char = QGroupBox(Dialog)
        self.right_char.setObjectName(u"right_char")
        self.right_char.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.right_char)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.overlap_clips_right = QCheckBox(self.right_char)
        self.overlap_clips_right.setObjectName(u"overlap_clips_right")
        sizePolicy3.setHeightForWidth(self.overlap_clips_right.sizePolicy().hasHeightForWidth())
        self.overlap_clips_right.setSizePolicy(sizePolicy3)

        self.horizontalLayout_13.addWidget(self.overlap_clips_right)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.volume_right_frame = QFrame(self.right_char)
        self.volume_right_frame.setObjectName(u"volume_right_frame")
        sizePolicy1.setHeightForWidth(self.volume_right_frame.sizePolicy().hasHeightForWidth())
        self.volume_right_frame.setSizePolicy(sizePolicy1)
        self.volume_right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.volume_right_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.volume_right_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_25 = QLabel(self.volume_right_frame)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_25)

        self.volume_slider_right = QSlider(self.volume_right_frame)
        self.volume_slider_right.setObjectName(u"volume_slider_right")
        sizePolicy3.setHeightForWidth(self.volume_slider_right.sizePolicy().hasHeightForWidth())
        self.volume_slider_right.setSizePolicy(sizePolicy3)
        self.volume_slider_right.setMinimumSize(QSize(150, 0))
        self.volume_slider_right.setMaximum(100)
        self.volume_slider_right.setValue(100)
        self.volume_slider_right.setOrientation(Qt.Orientation.Horizontal)
        self.volume_slider_right.setTickPosition(QSlider.TickPosition.NoTicks)
        self.volume_slider_right.setTickInterval(10)

        self.horizontalLayout_9.addWidget(self.volume_slider_right)


        self.horizontalLayout_14.addWidget(self.volume_right_frame)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.add_voice_clips_right = QPushButton(self.right_char)
        self.add_voice_clips_right.setObjectName(u"add_voice_clips_right")
        sizePolicy4.setHeightForWidth(self.add_voice_clips_right.sizePolicy().hasHeightForWidth())
        self.add_voice_clips_right.setSizePolicy(sizePolicy4)
        self.add_voice_clips_right.setMinimumSize(QSize(250, 0))
        self.add_voice_clips_right.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_15.addWidget(self.add_voice_clips_right)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_3.addWidget(self.right_char)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ok_button = QPushButton(self.widget)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout.addWidget(self.ok_button)

        self.cancel_button = QPushButton(self.widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout.addWidget(self.cancel_button)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"General Settings", None))
        self.mono_option.setText(QCoreApplication.translate("Dialog", u"Mono", None))
        self.stereo_option.setText(QCoreApplication.translate("Dialog", u"Stereo", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Master Volume", None))
        self.left_char.setTitle(QCoreApplication.translate("Dialog", u"Left character", None))
#if QT_CONFIG(tooltip)
        self.overlap_clips_left.setToolTip(QCoreApplication.translate("Dialog", u"Sets whether the clips should be cut off at a new word or overlap", None))
#endif // QT_CONFIG(tooltip)
        self.overlap_clips_left.setText(QCoreApplication.translate("Dialog", u"Overlap sound effects", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Volume", None))
        self.add_voice_clips_left.setText(QCoreApplication.translate("Dialog", u"Add voice clip(s)", None))
        self.right_char.setTitle(QCoreApplication.translate("Dialog", u"Right character", None))
#if QT_CONFIG(tooltip)
        self.overlap_clips_right.setToolTip(QCoreApplication.translate("Dialog", u"Sets whether the clips should be cut off at a new word or overlap", None))
#endif // QT_CONFIG(tooltip)
        self.overlap_clips_right.setText(QCoreApplication.translate("Dialog", u"Overlap sound effects", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Volume", None))
        self.add_voice_clips_right.setText(QCoreApplication.translate("Dialog", u"Add voice clip(s)", None))
        self.ok_button.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

