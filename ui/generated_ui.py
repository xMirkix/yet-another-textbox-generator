# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiabgclh.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1066, 797)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionLast_Opened = QAction(MainWindow)
        self.actionLast_Opened.setObjectName(u"actionLast_Opened")
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.setPriority(QAction.Priority.HighPriority)
        self.actionImport_yatg_File = QAction(MainWindow)
        self.actionImport_yatg_File.setObjectName(u"actionImport_yatg_File")
        self.actionNew_File = QAction(MainWindow)
        self.actionNew_File.setObjectName(u"actionNew_File")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy1)
        self.tabs.setBaseSize(QSize(0, 0))
        self.tabs.setTabPosition(QTabWidget.TabPosition.West)
        self.tabs.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabs.setIconSize(QSize(24, 24))
        self.tabs.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(False)
        self.tabs.setTabBarAutoHide(False)
        self.welcome = QWidget()
        self.welcome.setObjectName(u"welcome")
        self.verticalLayout_36 = QVBoxLayout(self.welcome)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_2)

        self.logo = QLabel(self.welcome)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"title_transparent.png"))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.logo)

        self.verticalSpacer_3 = QSpacerItem(14, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_3)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_3)

        self.open_file = QPushButton(self.welcome)
        self.open_file.setObjectName(u"open_file")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.open_file.sizePolicy().hasHeightForWidth())
        self.open_file.setSizePolicy(sizePolicy2)

        self.horizontalLayout_48.addWidget(self.open_file)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_7)


        self.verticalLayout_36.addLayout(self.horizontalLayout_48)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_4)

        self.tabs.addTab(self.welcome, "")
        self.generator = QWidget()
        self.generator.setObjectName(u"generator")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.generator.sizePolicy().hasHeightForWidth())
        self.generator.setSizePolicy(sizePolicy3)
        self.verticalLayout_37 = QVBoxLayout(self.generator)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.scrollArea_4 = QScrollArea(self.generator)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy3.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy3)
        self.scrollArea_4.setMinimumSize(QSize(1000, 600))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 561, 1400))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bordersettings = QGroupBox(self.scrollAreaWidgetContents_2)
        self.bordersettings.setObjectName(u"bordersettings")
        self.horizontalLayout_5 = QHBoxLayout(self.bordersettings)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.border_style_label = QLabel(self.bordersettings)
        self.border_style_label.setObjectName(u"border_style_label")

        self.horizontalLayout_3.addWidget(self.border_style_label)

        self.border_style_selector = QComboBox(self.bordersettings)
        self.border_style_selector.setObjectName(u"border_style_selector")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.border_style_selector.sizePolicy().hasHeightForWidth())
        self.border_style_selector.setSizePolicy(sizePolicy4)
        self.border_style_selector.setMinimumSize(QSize(49, 0))

        self.horizontalLayout_3.addWidget(self.border_style_selector)

        self.horizontalSpacer_10 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.border_style_preview = QLabel(self.bordersettings)
        self.border_style_preview.setObjectName(u"border_style_preview")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.border_style_preview.sizePolicy().hasHeightForWidth())
        self.border_style_preview.setSizePolicy(sizePolicy5)
        self.border_style_preview.setMinimumSize(QSize(0, 0))
        self.border_style_preview.setMaximumSize(QSize(100, 100))
        self.border_style_preview.setAutoFillBackground(True)
        self.border_style_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.border_style_preview)

        self.horizontalSpacer_9 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line_6 = QFrame(self.bordersettings)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.border_color_label = QLabel(self.bordersettings)
        self.border_color_label.setObjectName(u"border_color_label")

        self.horizontalLayout_4.addWidget(self.border_color_label)

        self.border_color_selector = QComboBox(self.bordersettings)
        self.border_color_selector.setObjectName(u"border_color_selector")

        self.horizontalLayout_4.addWidget(self.border_color_selector)

        self.border_color_preview = QLabel(self.bordersettings)
        self.border_color_preview.setObjectName(u"border_color_preview")
        sizePolicy5.setHeightForWidth(self.border_color_preview.sizePolicy().hasHeightForWidth())
        self.border_color_preview.setSizePolicy(sizePolicy5)
        self.border_color_preview.setMinimumSize(QSize(200, 30))
        self.border_color_preview.setMaximumSize(QSize(200, 30))
        self.border_color_preview.setAutoFillBackground(True)
        self.border_color_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.border_color_preview)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.bordersettings)

        self.spritesettings = QGroupBox(self.scrollAreaWidgetContents_2)
        self.spritesettings.setObjectName(u"spritesettings")
        self.horizontalLayout_12 = QHBoxLayout(self.spritesettings)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.universe_label = QLabel(self.spritesettings)
        self.universe_label.setObjectName(u"universe_label")

        self.horizontalLayout_10.addWidget(self.universe_label)

        self.universe_selector = QComboBox(self.spritesettings)
        self.universe_selector.setObjectName(u"universe_selector")

        self.horizontalLayout_10.addWidget(self.universe_selector)

        self.horizontalSpacer_12 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.universe_preview = QLabel(self.spritesettings)
        self.universe_preview.setObjectName(u"universe_preview")
        sizePolicy5.setHeightForWidth(self.universe_preview.sizePolicy().hasHeightForWidth())
        self.universe_preview.setSizePolicy(sizePolicy5)
        self.universe_preview.setMinimumSize(QSize(0, 0))
        self.universe_preview.setMaximumSize(QSize(100, 100))
        self.universe_preview.setAutoFillBackground(True)
        self.universe_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.universe_preview)

        self.horizontalSpacer_11 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.line_5 = QFrame(self.spritesettings)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.character_label = QLabel(self.spritesettings)
        self.character_label.setObjectName(u"character_label")

        self.horizontalLayout_13.addWidget(self.character_label)

        self.character_selector = QComboBox(self.spritesettings)
        self.character_selector.setObjectName(u"character_selector")

        self.horizontalLayout_13.addWidget(self.character_selector)

        self.horizontalSpacer_14 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.character_preview = QLabel(self.spritesettings)
        self.character_preview.setObjectName(u"character_preview")
        sizePolicy5.setHeightForWidth(self.character_preview.sizePolicy().hasHeightForWidth())
        self.character_preview.setSizePolicy(sizePolicy5)
        self.character_preview.setMinimumSize(QSize(0, 0))
        self.character_preview.setMaximumSize(QSize(100, 100))
        self.character_preview.setAutoFillBackground(True)
        self.character_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.character_preview)

        self.horizontalSpacer_13 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.line_4 = QFrame(self.spritesettings)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.expression_label = QLabel(self.spritesettings)
        self.expression_label.setObjectName(u"expression_label")

        self.horizontalLayout_15.addWidget(self.expression_label)

        self.expression_selector = QComboBox(self.spritesettings)
        self.expression_selector.setObjectName(u"expression_selector")

        self.horizontalLayout_15.addWidget(self.expression_selector)

        self.horizontalSpacer_16 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.expression_preview = QLabel(self.spritesettings)
        self.expression_preview.setObjectName(u"expression_preview")
        sizePolicy5.setHeightForWidth(self.expression_preview.sizePolicy().hasHeightForWidth())
        self.expression_preview.setSizePolicy(sizePolicy5)
        self.expression_preview.setMinimumSize(QSize(0, 0))
        self.expression_preview.setMaximumSize(QSize(100, 100))
        self.expression_preview.setAutoFillBackground(True)
        self.expression_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.expression_preview)

        self.horizontalSpacer_15 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.line_3 = QFrame(self.spritesettings)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.expression_color_label = QLabel(self.spritesettings)
        self.expression_color_label.setObjectName(u"expression_color_label")

        self.horizontalLayout_11.addWidget(self.expression_color_label)

        self.expression_color_selector = QComboBox(self.spritesettings)
        self.expression_color_selector.setObjectName(u"expression_color_selector")

        self.horizontalLayout_11.addWidget(self.expression_color_selector)

        self.expression_color_preview = QLabel(self.spritesettings)
        self.expression_color_preview.setObjectName(u"expression_color_preview")
        sizePolicy5.setHeightForWidth(self.expression_color_preview.sizePolicy().hasHeightForWidth())
        self.expression_color_preview.setSizePolicy(sizePolicy5)
        self.expression_color_preview.setMinimumSize(QSize(200, 30))
        self.expression_color_preview.setMaximumSize(QSize(200, 30))
        self.expression_color_preview.setAutoFillBackground(True)
        self.expression_color_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.expression_color_preview)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.spritesettings)

        self.fontsettings = QGroupBox(self.scrollAreaWidgetContents_2)
        self.fontsettings.setObjectName(u"fontsettings")
        self.horizontalLayout_20 = QHBoxLayout(self.fontsettings)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.font_label = QLabel(self.fontsettings)
        self.font_label.setObjectName(u"font_label")

        self.horizontalLayout_16.addWidget(self.font_label)

        self.font_selector = QComboBox(self.fontsettings)
        self.font_selector.setObjectName(u"font_selector")

        self.horizontalLayout_16.addWidget(self.font_selector)

        self.horizontalSpacer_18 = QSpacerItem(245, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_18)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.line_7 = QFrame(self.fontsettings)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_7)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.asterisk_label = QLabel(self.fontsettings)
        self.asterisk_label.setObjectName(u"asterisk_label")

        self.horizontalLayout_17.addWidget(self.asterisk_label)

        self.asterisk_checkbox = QCheckBox(self.fontsettings)
        self.asterisk_checkbox.setObjectName(u"asterisk_checkbox")
        self.asterisk_checkbox.setChecked(True)

        self.horizontalLayout_17.addWidget(self.asterisk_checkbox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.asterisk_color = QLabel(self.fontsettings)
        self.asterisk_color.setObjectName(u"asterisk_color")

        self.horizontalLayout_18.addWidget(self.asterisk_color)

        self.asterisk_color_selector_1 = QComboBox(self.fontsettings)
        self.asterisk_color_selector_1.setObjectName(u"asterisk_color_selector_1")

        self.horizontalLayout_18.addWidget(self.asterisk_color_selector_1)

        self.asterisk_color_selector_2 = QComboBox(self.fontsettings)
        self.asterisk_color_selector_2.setObjectName(u"asterisk_color_selector_2")

        self.horizontalLayout_18.addWidget(self.asterisk_color_selector_2)

        self.asterisk_color_selector_3 = QComboBox(self.fontsettings)
        self.asterisk_color_selector_3.setObjectName(u"asterisk_color_selector_3")

        self.horizontalLayout_18.addWidget(self.asterisk_color_selector_3)

        self.horizontalSpacer_19 = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_19)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.asterisk_color_values = QLabel(self.fontsettings)
        self.asterisk_color_values.setObjectName(u"asterisk_color_values")

        self.horizontalLayout_52.addWidget(self.asterisk_color_values)

        self.asterisk_color_preview_1 = QLabel(self.fontsettings)
        self.asterisk_color_preview_1.setObjectName(u"asterisk_color_preview_1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.asterisk_color_preview_1.sizePolicy().hasHeightForWidth())
        self.asterisk_color_preview_1.setSizePolicy(sizePolicy6)
        self.asterisk_color_preview_1.setMinimumSize(QSize(90, 30))
        self.asterisk_color_preview_1.setMaximumSize(QSize(191, 30))
        self.asterisk_color_preview_1.setAutoFillBackground(True)
        self.asterisk_color_preview_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_52.addWidget(self.asterisk_color_preview_1)

        self.asterisk_color_preview_2 = QLabel(self.fontsettings)
        self.asterisk_color_preview_2.setObjectName(u"asterisk_color_preview_2")
        sizePolicy6.setHeightForWidth(self.asterisk_color_preview_2.sizePolicy().hasHeightForWidth())
        self.asterisk_color_preview_2.setSizePolicy(sizePolicy6)
        self.asterisk_color_preview_2.setMinimumSize(QSize(90, 30))
        self.asterisk_color_preview_2.setMaximumSize(QSize(191, 30))
        self.asterisk_color_preview_2.setAutoFillBackground(True)
        self.asterisk_color_preview_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_52.addWidget(self.asterisk_color_preview_2)

        self.asterisk_color_preview_3 = QLabel(self.fontsettings)
        self.asterisk_color_preview_3.setObjectName(u"asterisk_color_preview_3")
        sizePolicy6.setHeightForWidth(self.asterisk_color_preview_3.sizePolicy().hasHeightForWidth())
        self.asterisk_color_preview_3.setSizePolicy(sizePolicy6)
        self.asterisk_color_preview_3.setMinimumSize(QSize(90, 30))
        self.asterisk_color_preview_3.setMaximumSize(QSize(191, 30))
        self.asterisk_color_preview_3.setAutoFillBackground(True)
        self.asterisk_color_preview_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_52.addWidget(self.asterisk_color_preview_3)

        self.horizontalSpacer_20 = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_20)


        self.verticalLayout_5.addLayout(self.horizontalLayout_52)

        self.line_9 = QFrame(self.fontsettings)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_9)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.text_style_label = QLabel(self.fontsettings)
        self.text_style_label.setObjectName(u"text_style_label")

        self.horizontalLayout_19.addWidget(self.text_style_label)

        self.text_style_regular_option = QRadioButton(self.fontsettings)
        self.text_style_regular_option.setObjectName(u"text_style_regular_option")
        self.text_style_regular_option.setChecked(True)

        self.horizontalLayout_19.addWidget(self.text_style_regular_option)

        self.text_style_dark_world_option = QRadioButton(self.fontsettings)
        self.text_style_dark_world_option.setObjectName(u"text_style_dark_world_option")

        self.horizontalLayout_19.addWidget(self.text_style_dark_world_option)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.text_transform_label = QLabel(self.fontsettings)
        self.text_transform_label.setObjectName(u"text_transform_label")

        self.horizontalLayout_21.addWidget(self.text_transform_label)

        self.text_transform_selector = QComboBox(self.fontsettings)
        self.text_transform_selector.setObjectName(u"text_transform_selector")

        self.horizontalLayout_21.addWidget(self.text_transform_selector)

        self.horizontalSpacer_21 = QSpacerItem(245, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)


        self.verticalLayout_5.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_20.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.fontsettings)

        self.exportsettings = QGroupBox(self.scrollAreaWidgetContents_2)
        self.exportsettings.setObjectName(u"exportsettings")
        self.horizontalLayout_8 = QHBoxLayout(self.exportsettings)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.format_label = QLabel(self.exportsettings)
        self.format_label.setObjectName(u"format_label")

        self.horizontalLayout_6.addWidget(self.format_label)

        self.widget = QWidget(self.exportsettings)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_22 = QHBoxLayout(self.widget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.format_png_option = QRadioButton(self.widget)
        self.format_png_option.setObjectName(u"format_png_option")
        self.format_png_option.setChecked(True)

        self.horizontalLayout_22.addWidget(self.format_png_option)

        self.format_gif_option = QRadioButton(self.widget)
        self.format_gif_option.setObjectName(u"format_gif_option")

        self.horizontalLayout_22.addWidget(self.format_gif_option)


        self.horizontalLayout_6.addWidget(self.widget)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.line = QFrame(self.exportsettings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.margin_label = QLabel(self.exportsettings)
        self.margin_label.setObjectName(u"margin_label")

        self.horizontalLayout_9.addWidget(self.margin_label)

        self.margin_checkbox = QCheckBox(self.exportsettings)
        self.margin_checkbox.setObjectName(u"margin_checkbox")
        self.margin_checkbox.setChecked(True)

        self.horizontalLayout_9.addWidget(self.margin_checkbox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.line_2 = QFrame(self.exportsettings)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.size_label = QLabel(self.exportsettings)
        self.size_label.setObjectName(u"size_label")

        self.horizontalLayout_7.addWidget(self.size_label)

        self.widget_2 = QWidget(self.exportsettings)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.size_small_option = QRadioButton(self.widget_2)
        self.size_small_option.setObjectName(u"size_small_option")

        self.horizontalLayout_14.addWidget(self.size_small_option)

        self.size_medium_option = QRadioButton(self.widget_2)
        self.size_medium_option.setObjectName(u"size_medium_option")
        self.size_medium_option.setChecked(True)

        self.horizontalLayout_14.addWidget(self.size_medium_option)

        self.size_big_option = QRadioButton(self.widget_2)
        self.size_big_option.setObjectName(u"size_big_option")

        self.horizontalLayout_14.addWidget(self.size_big_option)


        self.horizontalLayout_7.addWidget(self.widget_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.exportsettings)


        self.verticalLayout_35.addLayout(self.verticalLayout)

        self.input_preview = QGroupBox(self.scrollAreaWidgetContents_2)
        self.input_preview.setObjectName(u"input_preview")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.input_preview.sizePolicy().hasHeightForWidth())
        self.input_preview.setSizePolicy(sizePolicy7)
        self.input_preview.setMinimumSize(QSize(400, 600))
        self.verticalLayout_6 = QVBoxLayout(self.input_preview)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.input_label = QLabel(self.input_preview)
        self.input_label.setObjectName(u"input_label")

        self.verticalLayout_6.addWidget(self.input_label)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.input = QTextEdit(self.input_preview)
        self.input.setObjectName(u"input")
        sizePolicy6.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy6)
        self.input.setMinimumSize(QSize(500, 75))
        self.input.setMaximumSize(QSize(400, 75))

        self.horizontalLayout_45.addWidget(self.input)


        self.verticalLayout_6.addLayout(self.horizontalLayout_45)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.line_8 = QFrame(self.input_preview)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_8)

        self.output_label = QLabel(self.input_preview)
        self.output_label.setObjectName(u"output_label")

        self.verticalLayout_6.addWidget(self.output_label)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.output = QLabel(self.input_preview)
        self.output.setObjectName(u"output")
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setMinimumSize(QSize(289, 76))
        self.output.setMaximumSize(QSize(885, 246))
        self.output.setAutoFillBackground(True)
        self.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_56.addWidget(self.output)


        self.verticalLayout_6.addLayout(self.horizontalLayout_56)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.line_10 = QFrame(self.input_preview)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_10)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.download = QPushButton(self.input_preview)
        self.download.setObjectName(u"download")
        sizePolicy5.setHeightForWidth(self.download.sizePolicy().hasHeightForWidth())
        self.download.setSizePolicy(sizePolicy5)
        self.download.setMinimumSize(QSize(0, 0))
        self.download.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_51.addWidget(self.download)


        self.verticalLayout_6.addLayout(self.horizontalLayout_51)


        self.verticalLayout_35.addWidget(self.input_preview)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_37.addWidget(self.scrollArea_4)

        self.tabs.addTab(self.generator, "")
        self.universes = QWidget()
        self.universes.setObjectName(u"universes")
        self.gridLayout_3 = QGridLayout(self.universes)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.existing = QGroupBox(self.universes)
        self.existing.setObjectName(u"existing")
        self.verticalLayout_12 = QVBoxLayout(self.existing)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.universe_filter_label = QLabel(self.existing)
        self.universe_filter_label.setObjectName(u"universe_filter_label")

        self.horizontalLayout.addWidget(self.universe_filter_label)

        self.universe_filter_input = QLineEdit(self.existing)
        self.universe_filter_input.setObjectName(u"universe_filter_input")

        self.horizontalLayout.addWidget(self.universe_filter_input)

        self.universe_filter_button = QPushButton(self.existing)
        self.universe_filter_button.setObjectName(u"universe_filter_button")

        self.horizontalLayout.addWidget(self.universe_filter_button)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.line_11 = QFrame(self.existing)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_11)

        self.scrollArea = QScrollArea(self.existing)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.universe_grid = QWidget()
        self.universe_grid.setObjectName(u"universe_grid")
        self.universe_grid.setGeometry(QRect(0, 0, 780, 630))
        self.gridLayout_2 = QGridLayout(self.universe_grid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.groupBox_10 = QGroupBox(self.universe_grid)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy5.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy5)
        self.groupBox_10.setMinimumSize(QSize(250, 200))
        self.groupBox_10.setMaximumSize(QSize(250, 200))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_45 = QLabel(self.groupBox_10)
        self.label_45.setObjectName(u"label_45")
        sizePolicy5.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy5)
        self.label_45.setMinimumSize(QSize(0, 0))
        self.label_45.setMaximumSize(QSize(100, 100))
        self.label_45.setAutoFillBackground(True)
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_45)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.pushButton_18 = QPushButton(self.groupBox_10)
        self.pushButton_18.setObjectName(u"pushButton_18")
        icon1 = QIcon()
        icon1.addFile(u"arrow-left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_18.setIcon(icon1)

        self.horizontalLayout_30.addWidget(self.pushButton_18)

        self.pushButton_16 = QPushButton(self.groupBox_10)
        self.pushButton_16.setObjectName(u"pushButton_16")
        icon2 = QIcon()
        icon2.addFile(u"primary-line-line-arrow-end.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_16.setIcon(icon2)

        self.horizontalLayout_30.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.groupBox_10)
        self.pushButton_17.setObjectName(u"pushButton_17")
        icon3 = QIcon()
        icon3.addFile(u"mono-editor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_17.setIcon(icon3)

        self.horizontalLayout_30.addWidget(self.pushButton_17)

        self.pushButton_19 = QPushButton(self.groupBox_10)
        self.pushButton_19.setObjectName(u"pushButton_19")
        icon4 = QIcon()
        icon4.addFile(u"trash_correct_resolution.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_19.setIcon(icon4)

        self.horizontalLayout_30.addWidget(self.pushButton_19)


        self.verticalLayout_9.addLayout(self.horizontalLayout_30)


        self.gridLayout_2.addWidget(self.groupBox_10, 0, 2, 1, 1)

        self.groupBox_9 = QGroupBox(self.universe_grid)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy5.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy5)
        self.groupBox_9.setMinimumSize(QSize(250, 200))
        self.groupBox_9.setMaximumSize(QSize(250, 200))
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_44 = QLabel(self.groupBox_9)
        self.label_44.setObjectName(u"label_44")
        sizePolicy5.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy5)
        self.label_44.setMinimumSize(QSize(0, 0))
        self.label_44.setMaximumSize(QSize(100, 100))
        self.label_44.setAutoFillBackground(True)
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_44)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pushButton_12 = QPushButton(self.groupBox_9)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon1)

        self.horizontalLayout_29.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.groupBox_9)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setIcon(icon2)

        self.horizontalLayout_29.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.groupBox_9)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setIcon(icon3)

        self.horizontalLayout_29.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.groupBox_9)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setIcon(icon4)

        self.horizontalLayout_29.addWidget(self.pushButton_15)


        self.verticalLayout_23.addLayout(self.horizontalLayout_29)


        self.gridLayout_2.addWidget(self.groupBox_9, 0, 1, 1, 1)

        self.groupBox_14 = QGroupBox(self.universe_grid)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy5.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy5)
        self.groupBox_14.setMinimumSize(QSize(250, 200))
        self.groupBox_14.setMaximumSize(QSize(250, 200))
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_49 = QLabel(self.groupBox_14)
        self.label_49.setObjectName(u"label_49")
        sizePolicy5.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy5)
        self.label_49.setMinimumSize(QSize(0, 0))
        self.label_49.setMaximumSize(QSize(100, 100))
        self.label_49.setAutoFillBackground(True)
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_49)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.pushButton_33 = QPushButton(self.groupBox_14)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setIcon(icon1)

        self.horizontalLayout_40.addWidget(self.pushButton_33)

        self.pushButton_35 = QPushButton(self.groupBox_14)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setIcon(icon2)

        self.horizontalLayout_40.addWidget(self.pushButton_35)

        self.pushButton_32 = QPushButton(self.groupBox_14)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setIcon(icon3)

        self.horizontalLayout_40.addWidget(self.pushButton_32)

        self.pushButton_34 = QPushButton(self.groupBox_14)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setIcon(icon4)

        self.horizontalLayout_40.addWidget(self.pushButton_34)


        self.verticalLayout_28.addLayout(self.horizontalLayout_40)


        self.gridLayout_2.addWidget(self.groupBox_14, 2, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.universe_grid)
        self.groupBox_15.setObjectName(u"groupBox_15")
        sizePolicy5.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy5)
        self.groupBox_15.setMinimumSize(QSize(250, 200))
        self.groupBox_15.setMaximumSize(QSize(250, 200))
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_50 = QLabel(self.groupBox_15)
        self.label_50.setObjectName(u"label_50")
        sizePolicy5.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy5)
        self.label_50.setMinimumSize(QSize(0, 0))
        self.label_50.setMaximumSize(QSize(100, 100))
        self.label_50.setAutoFillBackground(True)
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_50)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.pushButton_37 = QPushButton(self.groupBox_15)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setIcon(icon1)

        self.horizontalLayout_41.addWidget(self.pushButton_37)

        self.pushButton_39 = QPushButton(self.groupBox_15)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setIcon(icon2)

        self.horizontalLayout_41.addWidget(self.pushButton_39)

        self.pushButton_36 = QPushButton(self.groupBox_15)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setIcon(icon3)

        self.horizontalLayout_41.addWidget(self.pushButton_36)

        self.pushButton_38 = QPushButton(self.groupBox_15)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setIcon(icon4)

        self.horizontalLayout_41.addWidget(self.pushButton_38)


        self.verticalLayout_29.addLayout(self.horizontalLayout_41)


        self.gridLayout_2.addWidget(self.groupBox_15, 2, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.universe_grid)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy5.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy5)
        self.groupBox_11.setMinimumSize(QSize(250, 200))
        self.groupBox_11.setMaximumSize(QSize(250, 200))
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_46 = QLabel(self.groupBox_11)
        self.label_46.setObjectName(u"label_46")
        sizePolicy5.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy5)
        self.label_46.setMinimumSize(QSize(0, 0))
        self.label_46.setMaximumSize(QSize(100, 100))
        self.label_46.setAutoFillBackground(True)
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_46)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pushButton_22 = QPushButton(self.groupBox_11)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setIcon(icon1)

        self.horizontalLayout_31.addWidget(self.pushButton_22)

        self.pushButton_20 = QPushButton(self.groupBox_11)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setIcon(icon2)

        self.horizontalLayout_31.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.groupBox_11)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setIcon(icon3)

        self.horizontalLayout_31.addWidget(self.pushButton_21)

        self.pushButton_23 = QPushButton(self.groupBox_11)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setIcon(icon4)

        self.horizontalLayout_31.addWidget(self.pushButton_23)


        self.verticalLayout_25.addLayout(self.horizontalLayout_31)


        self.gridLayout_2.addWidget(self.groupBox_11, 1, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.universe_grid)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy5.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy5)
        self.groupBox_13.setMinimumSize(QSize(250, 200))
        self.groupBox_13.setMaximumSize(QSize(250, 200))
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_48 = QLabel(self.groupBox_13)
        self.label_48.setObjectName(u"label_48")
        sizePolicy5.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy5)
        self.label_48.setMinimumSize(QSize(0, 0))
        self.label_48.setMaximumSize(QSize(100, 100))
        self.label_48.setAutoFillBackground(True)
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_48)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.pushButton_30 = QPushButton(self.groupBox_13)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setIcon(icon1)

        self.horizontalLayout_39.addWidget(self.pushButton_30)

        self.pushButton_28 = QPushButton(self.groupBox_13)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setIcon(icon2)

        self.horizontalLayout_39.addWidget(self.pushButton_28)

        self.pushButton_29 = QPushButton(self.groupBox_13)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setIcon(icon3)

        self.horizontalLayout_39.addWidget(self.pushButton_29)

        self.pushButton_31 = QPushButton(self.groupBox_13)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setIcon(icon4)

        self.horizontalLayout_39.addWidget(self.pushButton_31)


        self.verticalLayout_27.addLayout(self.horizontalLayout_39)


        self.gridLayout_2.addWidget(self.groupBox_13, 1, 2, 1, 1)

        self.universe_test1 = QGroupBox(self.universe_grid)
        self.universe_test1.setObjectName(u"universe_test1")
        sizePolicy5.setHeightForWidth(self.universe_test1.sizePolicy().hasHeightForWidth())
        self.universe_test1.setSizePolicy(sizePolicy5)
        self.universe_test1.setMinimumSize(QSize(250, 200))
        self.universe_test1.setMaximumSize(QSize(250, 200))
        self.verticalLayout_24 = QVBoxLayout(self.universe_test1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.universe_test1_preview_image = QLabel(self.universe_test1)
        self.universe_test1_preview_image.setObjectName(u"universe_test1_preview_image")
        sizePolicy5.setHeightForWidth(self.universe_test1_preview_image.sizePolicy().hasHeightForWidth())
        self.universe_test1_preview_image.setSizePolicy(sizePolicy5)
        self.universe_test1_preview_image.setMinimumSize(QSize(0, 0))
        self.universe_test1_preview_image.setMaximumSize(QSize(100, 100))
        self.universe_test1_preview_image.setAutoFillBackground(True)
        self.universe_test1_preview_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.universe_test1_preview_image)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.universe_test1_left = QPushButton(self.universe_test1)
        self.universe_test1_left.setObjectName(u"universe_test1_left")
        self.universe_test1_left.setIcon(icon1)

        self.horizontalLayout_27.addWidget(self.universe_test1_left)

        self.universe_test1_right = QPushButton(self.universe_test1)
        self.universe_test1_right.setObjectName(u"universe_test1_right")
        self.universe_test1_right.setIcon(icon2)

        self.horizontalLayout_27.addWidget(self.universe_test1_right)

        self.universe_test1_edit = QPushButton(self.universe_test1)
        self.universe_test1_edit.setObjectName(u"universe_test1_edit")
        self.universe_test1_edit.setIcon(icon3)

        self.horizontalLayout_27.addWidget(self.universe_test1_edit)

        self.universe_test1_delete = QPushButton(self.universe_test1)
        self.universe_test1_delete.setObjectName(u"universe_test1_delete")
        self.universe_test1_delete.setIcon(icon4)

        self.horizontalLayout_27.addWidget(self.universe_test1_delete)


        self.verticalLayout_24.addLayout(self.horizontalLayout_27)


        self.gridLayout_2.addWidget(self.universe_test1, 0, 0, 1, 1)

        self.groupBox_16 = QGroupBox(self.universe_grid)
        self.groupBox_16.setObjectName(u"groupBox_16")
        sizePolicy5.setHeightForWidth(self.groupBox_16.sizePolicy().hasHeightForWidth())
        self.groupBox_16.setSizePolicy(sizePolicy5)
        self.groupBox_16.setMinimumSize(QSize(250, 200))
        self.groupBox_16.setMaximumSize(QSize(250, 200))
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_51 = QLabel(self.groupBox_16)
        self.label_51.setObjectName(u"label_51")
        sizePolicy5.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy5)
        self.label_51.setMinimumSize(QSize(0, 0))
        self.label_51.setMaximumSize(QSize(100, 100))
        self.label_51.setAutoFillBackground(True)
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_51)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.pushButton_41 = QPushButton(self.groupBox_16)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setIcon(icon1)

        self.horizontalLayout_42.addWidget(self.pushButton_41)

        self.pushButton_43 = QPushButton(self.groupBox_16)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setIcon(icon2)

        self.horizontalLayout_42.addWidget(self.pushButton_43)

        self.pushButton_40 = QPushButton(self.groupBox_16)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setIcon(icon3)

        self.horizontalLayout_42.addWidget(self.pushButton_40)

        self.pushButton_42 = QPushButton(self.groupBox_16)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setIcon(icon4)

        self.horizontalLayout_42.addWidget(self.pushButton_42)


        self.verticalLayout_30.addLayout(self.horizontalLayout_42)


        self.gridLayout_2.addWidget(self.groupBox_16, 2, 2, 1, 1)

        self.groupBox_12 = QGroupBox(self.universe_grid)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy5.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy5)
        self.groupBox_12.setMinimumSize(QSize(250, 200))
        self.groupBox_12.setMaximumSize(QSize(250, 200))
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_47 = QLabel(self.groupBox_12)
        self.label_47.setObjectName(u"label_47")
        sizePolicy5.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy5)
        self.label_47.setMinimumSize(QSize(0, 0))
        self.label_47.setMaximumSize(QSize(100, 100))
        self.label_47.setAutoFillBackground(True)
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_47)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pushButton_26 = QPushButton(self.groupBox_12)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setIcon(icon1)

        self.horizontalLayout_38.addWidget(self.pushButton_26)

        self.pushButton_24 = QPushButton(self.groupBox_12)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setIcon(icon2)

        self.horizontalLayout_38.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.groupBox_12)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setIcon(icon3)

        self.horizontalLayout_38.addWidget(self.pushButton_25)

        self.pushButton_27 = QPushButton(self.groupBox_12)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setIcon(icon4)

        self.horizontalLayout_38.addWidget(self.pushButton_27)


        self.verticalLayout_26.addLayout(self.horizontalLayout_38)


        self.gridLayout_2.addWidget(self.groupBox_12, 1, 1, 1, 1)

        self.scrollArea.setWidget(self.universe_grid)

        self.verticalLayout_10.addWidget(self.scrollArea)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)


        self.gridLayout_3.addWidget(self.existing, 1, 0, 1, 1)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.create_universe = QGroupBox(self.universes)
        self.create_universe.setObjectName(u"create_universe")
        sizePolicy6.setHeightForWidth(self.create_universe.sizePolicy().hasHeightForWidth())
        self.create_universe.setSizePolicy(sizePolicy6)
        self.create_universe.setMinimumSize(QSize(354, 226))
        self.create_universe.setMaximumSize(QSize(354, 226))
        self.verticalLayout_11 = QVBoxLayout(self.create_universe)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.universe_create_name_label = QLabel(self.create_universe)
        self.universe_create_name_label.setObjectName(u"universe_create_name_label")

        self.horizontalLayout_23.addWidget(self.universe_create_name_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_4)

        self.universe_create_name_input = QLineEdit(self.create_universe)
        self.universe_create_name_input.setObjectName(u"universe_create_name_input")

        self.horizontalLayout_23.addWidget(self.universe_create_name_input)


        self.verticalLayout_7.addLayout(self.horizontalLayout_23)

        self.line_12 = QFrame(self.create_universe)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_12)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.universe_create_preview_label = QLabel(self.create_universe)
        self.universe_create_preview_label.setObjectName(u"universe_create_preview_label")

        self.horizontalLayout_24.addWidget(self.universe_create_preview_label)

        self.universe_create_image_button = QPushButton(self.create_universe)
        self.universe_create_image_button.setObjectName(u"universe_create_image_button")

        self.horizontalLayout_24.addWidget(self.universe_create_image_button)

        self.universe_create_image_preview = QLabel(self.create_universe)
        self.universe_create_image_preview.setObjectName(u"universe_create_image_preview")
        sizePolicy5.setHeightForWidth(self.universe_create_image_preview.sizePolicy().hasHeightForWidth())
        self.universe_create_image_preview.setSizePolicy(sizePolicy5)
        self.universe_create_image_preview.setMinimumSize(QSize(0, 0))
        self.universe_create_image_preview.setMaximumSize(QSize(100, 100))
        self.universe_create_image_preview.setAutoFillBackground(True)
        self.universe_create_image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.universe_create_image_preview)


        self.verticalLayout_7.addLayout(self.horizontalLayout_24)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)

        self.line_13 = QFrame(self.create_universe)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_13)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.universe_create_confirm_button = QPushButton(self.create_universe)
        self.universe_create_confirm_button.setObjectName(u"universe_create_confirm_button")

        self.horizontalLayout_57.addWidget(self.universe_create_confirm_button)


        self.verticalLayout_11.addLayout(self.horizontalLayout_57)


        self.horizontalLayout_53.addWidget(self.create_universe)

        self.edit_universe = QGroupBox(self.universes)
        self.edit_universe.setObjectName(u"edit_universe")
        sizePolicy6.setHeightForWidth(self.edit_universe.sizePolicy().hasHeightForWidth())
        self.edit_universe.setSizePolicy(sizePolicy6)
        self.edit_universe.setMinimumSize(QSize(354, 226))
        self.edit_universe.setMaximumSize(QSize(354, 226))
        self.verticalLayout_33 = QVBoxLayout(self.edit_universe)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.universe_edit_name_label = QLabel(self.edit_universe)
        self.universe_edit_name_label.setObjectName(u"universe_edit_name_label")

        self.horizontalLayout_61.addWidget(self.universe_edit_name_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer)

        self.universe_edit_name_input = QLineEdit(self.edit_universe)
        self.universe_edit_name_input.setObjectName(u"universe_edit_name_input")

        self.horizontalLayout_61.addWidget(self.universe_edit_name_input)


        self.verticalLayout_33.addLayout(self.horizontalLayout_61)

        self.line_21 = QFrame(self.edit_universe)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_33.addWidget(self.line_21)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.universe_edit_preview_label = QLabel(self.edit_universe)
        self.universe_edit_preview_label.setObjectName(u"universe_edit_preview_label")

        self.horizontalLayout_62.addWidget(self.universe_edit_preview_label)

        self.universe_edit_image_button = QPushButton(self.edit_universe)
        self.universe_edit_image_button.setObjectName(u"universe_edit_image_button")
        sizePolicy6.setHeightForWidth(self.universe_edit_image_button.sizePolicy().hasHeightForWidth())
        self.universe_edit_image_button.setSizePolicy(sizePolicy6)
        self.universe_edit_image_button.setMinimumSize(QSize(109, 0))
        self.universe_edit_image_button.setMaximumSize(QSize(109, 16777215))

        self.horizontalLayout_62.addWidget(self.universe_edit_image_button)

        self.universe_edit_image_preview = QLabel(self.edit_universe)
        self.universe_edit_image_preview.setObjectName(u"universe_edit_image_preview")
        sizePolicy5.setHeightForWidth(self.universe_edit_image_preview.sizePolicy().hasHeightForWidth())
        self.universe_edit_image_preview.setSizePolicy(sizePolicy5)
        self.universe_edit_image_preview.setMinimumSize(QSize(0, 0))
        self.universe_edit_image_preview.setMaximumSize(QSize(100, 100))
        self.universe_edit_image_preview.setAutoFillBackground(True)
        self.universe_edit_image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_62.addWidget(self.universe_edit_image_preview)


        self.verticalLayout_33.addLayout(self.horizontalLayout_62)

        self.line_22 = QFrame(self.edit_universe)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_33.addWidget(self.line_22)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.universe_edit_confirm_button = QPushButton(self.edit_universe)
        self.universe_edit_confirm_button.setObjectName(u"universe_edit_confirm_button")

        self.horizontalLayout_63.addWidget(self.universe_edit_confirm_button)


        self.verticalLayout_33.addLayout(self.horizontalLayout_63)


        self.horizontalLayout_53.addWidget(self.edit_universe)


        self.gridLayout_3.addLayout(self.horizontalLayout_53, 0, 0, 1, 1)

        self.tabs.addTab(self.universes, "")
        self.characters = QWidget()
        self.characters.setObjectName(u"characters")
        self.verticalLayout_8 = QVBoxLayout(self.characters)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.create_character = QGroupBox(self.characters)
        self.create_character.setObjectName(u"create_character")
        sizePolicy6.setHeightForWidth(self.create_character.sizePolicy().hasHeightForWidth())
        self.create_character.setSizePolicy(sizePolicy6)
        self.create_character.setMinimumSize(QSize(354, 335))
        self.create_character.setMaximumSize(QSize(354, 335))
        self.verticalLayout_16 = QVBoxLayout(self.create_character)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.characters_create_name_label = QLabel(self.create_character)
        self.characters_create_name_label.setObjectName(u"characters_create_name_label")

        self.horizontalLayout_26.addWidget(self.characters_create_name_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_5)

        self.characters_create_name_input = QLineEdit(self.create_character)
        self.characters_create_name_input.setObjectName(u"characters_create_name_input")

        self.horizontalLayout_26.addWidget(self.characters_create_name_input)


        self.verticalLayout_15.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.characters_create_universe_label = QLabel(self.create_character)
        self.characters_create_universe_label.setObjectName(u"characters_create_universe_label")

        self.horizontalLayout_32.addWidget(self.characters_create_universe_label)

        self.characters_create_universe_selector = QComboBox(self.create_character)
        self.characters_create_universe_selector.setObjectName(u"characters_create_universe_selector")

        self.horizontalLayout_32.addWidget(self.characters_create_universe_selector)


        self.verticalLayout_15.addLayout(self.horizontalLayout_32)

        self.line_20 = QFrame(self.create_character)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.line_20)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.characters_create_style_label = QLabel(self.create_character)
        self.characters_create_style_label.setObjectName(u"characters_create_style_label")

        self.horizontalLayout_46.addWidget(self.characters_create_style_label)

        self.characters_create_style_regular_option = QRadioButton(self.create_character)
        self.characters_create_style_regular_option.setObjectName(u"characters_create_style_regular_option")
        self.characters_create_style_regular_option.setChecked(True)

        self.horizontalLayout_46.addWidget(self.characters_create_style_regular_option)

        self.characters_create_style_dark_world_option = QRadioButton(self.create_character)
        self.characters_create_style_dark_world_option.setObjectName(u"characters_create_style_dark_world_option")

        self.horizontalLayout_46.addWidget(self.characters_create_style_dark_world_option)


        self.verticalLayout_15.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.characters_create_transform_label = QLabel(self.create_character)
        self.characters_create_transform_label.setObjectName(u"characters_create_transform_label")

        self.horizontalLayout_47.addWidget(self.characters_create_transform_label)

        self.characters_create_transform_selector = QComboBox(self.create_character)
        self.characters_create_transform_selector.setObjectName(u"characters_create_transform_selector")

        self.horizontalLayout_47.addWidget(self.characters_create_transform_selector)


        self.verticalLayout_15.addLayout(self.horizontalLayout_47)

        self.line_14 = QFrame(self.create_character)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.line_14)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.characters_create_preview_label = QLabel(self.create_character)
        self.characters_create_preview_label.setObjectName(u"characters_create_preview_label")

        self.horizontalLayout_28.addWidget(self.characters_create_preview_label)

        self.characters_create_image_button = QPushButton(self.create_character)
        self.characters_create_image_button.setObjectName(u"characters_create_image_button")

        self.horizontalLayout_28.addWidget(self.characters_create_image_button)

        self.characters_create_image_preview = QLabel(self.create_character)
        self.characters_create_image_preview.setObjectName(u"characters_create_image_preview")
        sizePolicy5.setHeightForWidth(self.characters_create_image_preview.sizePolicy().hasHeightForWidth())
        self.characters_create_image_preview.setSizePolicy(sizePolicy5)
        self.characters_create_image_preview.setMinimumSize(QSize(0, 0))
        self.characters_create_image_preview.setMaximumSize(QSize(100, 100))
        self.characters_create_image_preview.setAutoFillBackground(True)
        self.characters_create_image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_28.addWidget(self.characters_create_image_preview)


        self.verticalLayout_15.addLayout(self.horizontalLayout_28)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.line_15 = QFrame(self.create_character)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.line_15)

        self.characters_create_confirm_button = QPushButton(self.create_character)
        self.characters_create_confirm_button.setObjectName(u"characters_create_confirm_button")

        self.verticalLayout_16.addWidget(self.characters_create_confirm_button)


        self.horizontalLayout_58.addWidget(self.create_character)

        self.edit_character = QGroupBox(self.characters)
        self.edit_character.setObjectName(u"edit_character")
        sizePolicy6.setHeightForWidth(self.edit_character.sizePolicy().hasHeightForWidth())
        self.edit_character.setSizePolicy(sizePolicy6)
        self.edit_character.setMinimumSize(QSize(354, 335))
        self.edit_character.setMaximumSize(QSize(354, 335))
        self.verticalLayout_34 = QVBoxLayout(self.edit_character)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.characters_edit_name_label = QLabel(self.edit_character)
        self.characters_edit_name_label.setObjectName(u"characters_edit_name_label")

        self.horizontalLayout_2.addWidget(self.characters_edit_name_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.characters_edit_name_input = QLineEdit(self.edit_character)
        self.characters_edit_name_input.setObjectName(u"characters_edit_name_input")

        self.horizontalLayout_2.addWidget(self.characters_edit_name_input)


        self.verticalLayout_39.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.characters_edit_universe_label = QLabel(self.edit_character)
        self.characters_edit_universe_label.setObjectName(u"characters_edit_universe_label")

        self.horizontalLayout_49.addWidget(self.characters_edit_universe_label)

        self.characters_edit_universe_selector = QComboBox(self.edit_character)
        self.characters_edit_universe_selector.setObjectName(u"characters_edit_universe_selector")

        self.horizontalLayout_49.addWidget(self.characters_edit_universe_selector)


        self.verticalLayout_39.addLayout(self.horizontalLayout_49)

        self.line_25 = QFrame(self.edit_character)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.HLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_39.addWidget(self.line_25)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.characters_edit_style_label = QLabel(self.edit_character)
        self.characters_edit_style_label.setObjectName(u"characters_edit_style_label")

        self.horizontalLayout_55.addWidget(self.characters_edit_style_label)

        self.characters_edit_style_regular_option = QRadioButton(self.edit_character)
        self.characters_edit_style_regular_option.setObjectName(u"characters_edit_style_regular_option")

        self.horizontalLayout_55.addWidget(self.characters_edit_style_regular_option)

        self.characters_edit_style_dark_world_option = QRadioButton(self.edit_character)
        self.characters_edit_style_dark_world_option.setObjectName(u"characters_edit_style_dark_world_option")

        self.horizontalLayout_55.addWidget(self.characters_edit_style_dark_world_option)


        self.verticalLayout_39.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.characters_edit_transform_label = QLabel(self.edit_character)
        self.characters_edit_transform_label.setObjectName(u"characters_edit_transform_label")

        self.horizontalLayout_50.addWidget(self.characters_edit_transform_label)

        self.characters_edit_transform_selector = QComboBox(self.edit_character)
        self.characters_edit_transform_selector.setObjectName(u"characters_edit_transform_selector")

        self.horizontalLayout_50.addWidget(self.characters_edit_transform_selector)


        self.verticalLayout_39.addLayout(self.horizontalLayout_50)

        self.line_24 = QFrame(self.edit_character)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.HLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_39.addWidget(self.line_24)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.characters_edit_preview_label = QLabel(self.edit_character)
        self.characters_edit_preview_label.setObjectName(u"characters_edit_preview_label")

        self.horizontalLayout_54.addWidget(self.characters_edit_preview_label)

        self.characters_edit_image_button = QPushButton(self.edit_character)
        self.characters_edit_image_button.setObjectName(u"characters_edit_image_button")

        self.horizontalLayout_54.addWidget(self.characters_edit_image_button)

        self.characters_edit_image_preview = QLabel(self.edit_character)
        self.characters_edit_image_preview.setObjectName(u"characters_edit_image_preview")
        sizePolicy5.setHeightForWidth(self.characters_edit_image_preview.sizePolicy().hasHeightForWidth())
        self.characters_edit_image_preview.setSizePolicy(sizePolicy5)
        self.characters_edit_image_preview.setMinimumSize(QSize(0, 0))
        self.characters_edit_image_preview.setMaximumSize(QSize(100, 100))
        self.characters_edit_image_preview.setAutoFillBackground(True)
        self.characters_edit_image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_54.addWidget(self.characters_edit_image_preview)


        self.verticalLayout_39.addLayout(self.horizontalLayout_54)


        self.verticalLayout_34.addLayout(self.verticalLayout_39)

        self.line_23 = QFrame(self.edit_character)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_34.addWidget(self.line_23)

        self.characters_edit_confirm_button = QPushButton(self.edit_character)
        self.characters_edit_confirm_button.setObjectName(u"characters_edit_confirm_button")

        self.verticalLayout_34.addWidget(self.characters_edit_confirm_button)


        self.horizontalLayout_58.addWidget(self.edit_character)


        self.verticalLayout_13.addLayout(self.horizontalLayout_58)

        self.groupBox_5 = QGroupBox(self.characters)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.characters_filter_label = QLabel(self.groupBox_5)
        self.characters_filter_label.setObjectName(u"characters_filter_label")

        self.horizontalLayout_25.addWidget(self.characters_filter_label)

        self.characters_filter_input = QLineEdit(self.groupBox_5)
        self.characters_filter_input.setObjectName(u"characters_filter_input")

        self.horizontalLayout_25.addWidget(self.characters_filter_input)

        self.characters_filter_button = QPushButton(self.groupBox_5)
        self.characters_filter_button.setObjectName(u"characters_filter_button")

        self.horizontalLayout_25.addWidget(self.characters_filter_button)


        self.verticalLayout_14.addLayout(self.horizontalLayout_25)

        self.line_18 = QFrame(self.groupBox_5)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line_18)

        self.scrollArea_2 = QScrollArea(self.groupBox_5)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.characters_grid = QWidget()
        self.characters_grid.setObjectName(u"characters_grid")
        self.characters_grid.setGeometry(QRect(0, 0, 780, 218))
        self.gridLayout = QGridLayout(self.characters_grid)
        self.gridLayout.setObjectName(u"gridLayout")
        self.characters_test1 = QGroupBox(self.characters_grid)
        self.characters_test1.setObjectName(u"characters_test1")
        sizePolicy6.setHeightForWidth(self.characters_test1.sizePolicy().hasHeightForWidth())
        self.characters_test1.setSizePolicy(sizePolicy6)
        self.characters_test1.setMinimumSize(QSize(250, 200))
        self.characters_test1.setMaximumSize(QSize(250, 200))
        self.verticalLayout_31 = QVBoxLayout(self.characters_test1)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.characters_test1_preview_image = QLabel(self.characters_test1)
        self.characters_test1_preview_image.setObjectName(u"characters_test1_preview_image")
        sizePolicy5.setHeightForWidth(self.characters_test1_preview_image.sizePolicy().hasHeightForWidth())
        self.characters_test1_preview_image.setSizePolicy(sizePolicy5)
        self.characters_test1_preview_image.setMinimumSize(QSize(0, 0))
        self.characters_test1_preview_image.setMaximumSize(QSize(100, 100))
        self.characters_test1_preview_image.setAutoFillBackground(True)
        self.characters_test1_preview_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.characters_test1_preview_image)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.characters_test1_left = QPushButton(self.characters_test1)
        self.characters_test1_left.setObjectName(u"characters_test1_left")
        self.characters_test1_left.setIcon(icon1)

        self.horizontalLayout_43.addWidget(self.characters_test1_left)

        self.characters_test1_right = QPushButton(self.characters_test1)
        self.characters_test1_right.setObjectName(u"characters_test1_right")
        self.characters_test1_right.setIcon(icon2)

        self.horizontalLayout_43.addWidget(self.characters_test1_right)

        self.characters_test1_edit = QPushButton(self.characters_test1)
        self.characters_test1_edit.setObjectName(u"characters_test1_edit")
        self.characters_test1_edit.setIcon(icon3)

        self.horizontalLayout_43.addWidget(self.characters_test1_edit)

        self.characters_test1_delete = QPushButton(self.characters_test1)
        self.characters_test1_delete.setObjectName(u"characters_test1_delete")
        self.characters_test1_delete.setIcon(icon4)

        self.horizontalLayout_43.addWidget(self.characters_test1_delete)


        self.verticalLayout_31.addLayout(self.horizontalLayout_43)


        self.gridLayout.addWidget(self.characters_test1, 0, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.characters_grid)
        self.groupBox_18.setObjectName(u"groupBox_18")
        sizePolicy5.setHeightForWidth(self.groupBox_18.sizePolicy().hasHeightForWidth())
        self.groupBox_18.setSizePolicy(sizePolicy5)
        self.groupBox_18.setMinimumSize(QSize(250, 200))
        self.groupBox_18.setMaximumSize(QSize(250, 200))
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_53 = QLabel(self.groupBox_18)
        self.label_53.setObjectName(u"label_53")
        sizePolicy5.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy5)
        self.label_53.setMinimumSize(QSize(0, 0))
        self.label_53.setMaximumSize(QSize(100, 100))
        self.label_53.setAutoFillBackground(True)
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_53)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.pushButton_48 = QPushButton(self.groupBox_18)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setIcon(icon1)

        self.horizontalLayout_44.addWidget(self.pushButton_48)

        self.pushButton_49 = QPushButton(self.groupBox_18)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setIcon(icon2)

        self.horizontalLayout_44.addWidget(self.pushButton_49)

        self.pushButton_50 = QPushButton(self.groupBox_18)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setIcon(icon3)

        self.horizontalLayout_44.addWidget(self.pushButton_50)

        self.pushButton_51 = QPushButton(self.groupBox_18)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setIcon(icon4)

        self.horizontalLayout_44.addWidget(self.pushButton_51)


        self.verticalLayout_32.addLayout(self.horizontalLayout_44)


        self.gridLayout.addWidget(self.groupBox_18, 0, 1, 1, 1)

        self.groupBox_23 = QGroupBox(self.characters_grid)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setMinimumSize(QSize(250, 200))
        self.groupBox_23.setMaximumSize(QSize(250, 200))
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_23)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_54 = QLabel(self.groupBox_23)
        self.label_54.setObjectName(u"label_54")
        sizePolicy5.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy5)
        self.label_54.setMinimumSize(QSize(0, 0))
        self.label_54.setMaximumSize(QSize(100, 100))
        self.label_54.setAutoFillBackground(True)
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_54)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.pushButton_60 = QPushButton(self.groupBox_23)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setIcon(icon1)

        self.horizontalLayout_60.addWidget(self.pushButton_60)

        self.pushButton_61 = QPushButton(self.groupBox_23)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setIcon(icon2)

        self.horizontalLayout_60.addWidget(self.pushButton_61)

        self.pushButton_62 = QPushButton(self.groupBox_23)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setIcon(icon3)

        self.horizontalLayout_60.addWidget(self.pushButton_62)

        self.pushButton_63 = QPushButton(self.groupBox_23)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setIcon(icon4)

        self.horizontalLayout_60.addWidget(self.pushButton_63)


        self.verticalLayout_38.addLayout(self.horizontalLayout_60)


        self.gridLayout.addWidget(self.groupBox_23, 0, 2, 1, 1)

        self.scrollArea_2.setWidget(self.characters_grid)

        self.verticalLayout_14.addWidget(self.scrollArea_2)


        self.verticalLayout_17.addLayout(self.verticalLayout_14)


        self.verticalLayout_13.addWidget(self.groupBox_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_13)

        self.tabs.addTab(self.characters, "")
        self.expressions = QWidget()
        self.expressions.setObjectName(u"expressions")
        self.verticalLayout_18 = QVBoxLayout(self.expressions)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.create_expression = QGroupBox(self.expressions)
        self.create_expression.setObjectName(u"create_expression")
        sizePolicy6.setHeightForWidth(self.create_expression.sizePolicy().hasHeightForWidth())
        self.create_expression.setSizePolicy(sizePolicy6)
        self.create_expression.setMinimumSize(QSize(354, 294))
        self.create_expression.setMaximumSize(QSize(354, 294))
        self.verticalLayout_20 = QVBoxLayout(self.create_expression)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.expressions_create_name_label = QLabel(self.create_expression)
        self.expressions_create_name_label.setObjectName(u"expressions_create_name_label")

        self.horizontalLayout_34.addWidget(self.expressions_create_name_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_6)

        self.expressions_create_name_input = QLineEdit(self.create_expression)
        self.expressions_create_name_input.setObjectName(u"expressions_create_name_input")

        self.horizontalLayout_34.addWidget(self.expressions_create_name_input)


        self.verticalLayout_19.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.expressions_create_universe_label = QLabel(self.create_expression)
        self.expressions_create_universe_label.setObjectName(u"expressions_create_universe_label")

        self.horizontalLayout_35.addWidget(self.expressions_create_universe_label)

        self.expressions_create_universe_selector = QComboBox(self.create_expression)
        self.expressions_create_universe_selector.setObjectName(u"expressions_create_universe_selector")

        self.horizontalLayout_35.addWidget(self.expressions_create_universe_selector)


        self.verticalLayout_19.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.expressions_create_character_label = QLabel(self.create_expression)
        self.expressions_create_character_label.setObjectName(u"expressions_create_character_label")

        self.horizontalLayout_36.addWidget(self.expressions_create_character_label)

        self.expressions_create_character_selector = QComboBox(self.create_expression)
        self.expressions_create_character_selector.setObjectName(u"expressions_create_character_selector")

        self.horizontalLayout_36.addWidget(self.expressions_create_character_selector)


        self.verticalLayout_19.addLayout(self.horizontalLayout_36)

        self.line_16 = QFrame(self.create_expression)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_16)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.expressions_create_preview_label = QLabel(self.create_expression)
        self.expressions_create_preview_label.setObjectName(u"expressions_create_preview_label")

        self.horizontalLayout_37.addWidget(self.expressions_create_preview_label)

        self.expressions_create_image_button = QPushButton(self.create_expression)
        self.expressions_create_image_button.setObjectName(u"expressions_create_image_button")

        self.horizontalLayout_37.addWidget(self.expressions_create_image_button)

        self.expressions_create_image_preview = QLabel(self.create_expression)
        self.expressions_create_image_preview.setObjectName(u"expressions_create_image_preview")
        sizePolicy5.setHeightForWidth(self.expressions_create_image_preview.sizePolicy().hasHeightForWidth())
        self.expressions_create_image_preview.setSizePolicy(sizePolicy5)
        self.expressions_create_image_preview.setMinimumSize(QSize(0, 0))
        self.expressions_create_image_preview.setMaximumSize(QSize(100, 100))
        self.expressions_create_image_preview.setAutoFillBackground(True)
        self.expressions_create_image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_37.addWidget(self.expressions_create_image_preview)


        self.verticalLayout_19.addLayout(self.horizontalLayout_37)

        self.line_17 = QFrame(self.create_expression)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_17)

        self.expressions_create_confirm_button = QPushButton(self.create_expression)
        self.expressions_create_confirm_button.setObjectName(u"expressions_create_confirm_button")

        self.verticalLayout_19.addWidget(self.expressions_create_confirm_button)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)


        self.horizontalLayout_59.addWidget(self.create_expression)

        self.edit_expression = QGroupBox(self.expressions)
        self.edit_expression.setObjectName(u"edit_expression")
        sizePolicy6.setHeightForWidth(self.edit_expression.sizePolicy().hasHeightForWidth())
        self.edit_expression.setSizePolicy(sizePolicy6)
        self.edit_expression.setMinimumSize(QSize(354, 294))
        self.edit_expression.setMaximumSize(QSize(354, 294))
        self.verticalLayout_40 = QVBoxLayout(self.edit_expression)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.expressions_edit_name_label = QLabel(self.edit_expression)
        self.expressions_edit_name_label.setObjectName(u"expressions_edit_name_label")

        self.horizontalLayout_64.addWidget(self.expressions_edit_name_label)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_22)

        self.expressions_edit_name_input = QLineEdit(self.edit_expression)
        self.expressions_edit_name_input.setObjectName(u"expressions_edit_name_input")

        self.horizontalLayout_64.addWidget(self.expressions_edit_name_input)


        self.verticalLayout_41.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.expressions_edit_universe_label = QLabel(self.edit_expression)
        self.expressions_edit_universe_label.setObjectName(u"expressions_edit_universe_label")

        self.horizontalLayout_65.addWidget(self.expressions_edit_universe_label)

        self.expressions_edit_universe_selector = QComboBox(self.edit_expression)
        self.expressions_edit_universe_selector.setObjectName(u"expressions_edit_universe_selector")

        self.horizontalLayout_65.addWidget(self.expressions_edit_universe_selector)


        self.verticalLayout_41.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.expressions_edit_character_label = QLabel(self.edit_expression)
        self.expressions_edit_character_label.setObjectName(u"expressions_edit_character_label")

        self.horizontalLayout_66.addWidget(self.expressions_edit_character_label)

        self.expressions_edit_character_selector = QComboBox(self.edit_expression)
        self.expressions_edit_character_selector.setObjectName(u"expressions_edit_character_selector")

        self.horizontalLayout_66.addWidget(self.expressions_edit_character_selector)


        self.verticalLayout_41.addLayout(self.horizontalLayout_66)

        self.line_26 = QFrame(self.edit_expression)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.Shape.HLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_41.addWidget(self.line_26)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.expressions_edit_preview_label = QLabel(self.edit_expression)
        self.expressions_edit_preview_label.setObjectName(u"expressions_edit_preview_label")

        self.horizontalLayout_67.addWidget(self.expressions_edit_preview_label)

        self.expressions_edit_image_button = QPushButton(self.edit_expression)
        self.expressions_edit_image_button.setObjectName(u"expressions_edit_image_button")

        self.horizontalLayout_67.addWidget(self.expressions_edit_image_button)

        self.expressions_edit_image_preview = QLabel(self.edit_expression)
        self.expressions_edit_image_preview.setObjectName(u"expressions_edit_image_preview")
        sizePolicy5.setHeightForWidth(self.expressions_edit_image_preview.sizePolicy().hasHeightForWidth())
        self.expressions_edit_image_preview.setSizePolicy(sizePolicy5)
        self.expressions_edit_image_preview.setMinimumSize(QSize(0, 0))
        self.expressions_edit_image_preview.setMaximumSize(QSize(100, 100))
        self.expressions_edit_image_preview.setAutoFillBackground(True)
        self.expressions_edit_image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_67.addWidget(self.expressions_edit_image_preview)


        self.verticalLayout_41.addLayout(self.horizontalLayout_67)

        self.line_27 = QFrame(self.edit_expression)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.Shape.HLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_41.addWidget(self.line_27)

        self.expressions_edit_confirm_button = QPushButton(self.edit_expression)
        self.expressions_edit_confirm_button.setObjectName(u"expressions_edit_confirm_button")

        self.verticalLayout_41.addWidget(self.expressions_edit_confirm_button)


        self.verticalLayout_40.addLayout(self.verticalLayout_41)


        self.horizontalLayout_59.addWidget(self.edit_expression)


        self.verticalLayout_18.addLayout(self.horizontalLayout_59)

        self.groupBox_7 = QGroupBox(self.expressions)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.expressions_filter_label = QLabel(self.groupBox_7)
        self.expressions_filter_label.setObjectName(u"expressions_filter_label")

        self.horizontalLayout_33.addWidget(self.expressions_filter_label)

        self.expressions_filter_input = QLineEdit(self.groupBox_7)
        self.expressions_filter_input.setObjectName(u"expressions_filter_input")

        self.horizontalLayout_33.addWidget(self.expressions_filter_input)

        self.expressions_filter_button = QPushButton(self.groupBox_7)
        self.expressions_filter_button.setObjectName(u"expressions_filter_button")

        self.horizontalLayout_33.addWidget(self.expressions_filter_button)


        self.verticalLayout_21.addLayout(self.horizontalLayout_33)

        self.line_19 = QFrame(self.groupBox_7)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_21.addWidget(self.line_19)

        self.scrollArea_3 = QScrollArea(self.groupBox_7)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.expressions_grid = QWidget()
        self.expressions_grid.setObjectName(u"expressions_grid")
        self.expressions_grid.setGeometry(QRect(0, 0, 96, 26))
        self.gridLayout_5 = QGridLayout(self.expressions_grid)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea_3.setWidget(self.expressions_grid)

        self.verticalLayout_21.addWidget(self.scrollArea_3)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)


        self.verticalLayout_18.addWidget(self.groupBox_7)

        self.tabs.addTab(self.expressions, "")

        self.gridLayout_4.addWidget(self.tabs, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1066, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)
        self.border_style_selector.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Yet another Texbox Generator", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionLast_Opened.setText(QCoreApplication.translate("MainWindow", u"Last Opened", None))
        self.actionOpen_2.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
#if QT_CONFIG(tooltip)
        self.actionOpen_2.setToolTip(QCoreApplication.translate("MainWindow", u"Open a .yatg File", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionOpen_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Open a .yatg File", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionOpen_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save to .yatg File", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(QCoreApplication.translate("MainWindow", u"Save to .yatg File", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(statustip)
        self.actionQuit.setStatusTip(QCoreApplication.translate("MainWindow", u"Close the Application", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionImport_yatg_File.setText(QCoreApplication.translate("MainWindow", u"Import .yatg File", None))
        self.actionNew_File.setText(QCoreApplication.translate("MainWindow", u"New File", None))
#if QT_CONFIG(tooltip)
        self.actionNew_File.setToolTip(QCoreApplication.translate("MainWindow", u"Save changes to different .yatg File", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionNew_File.setStatusTip(QCoreApplication.translate("MainWindow", u"Save changes to different .yatg File", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionNew_File.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.logo.setText("")
        self.open_file.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.tabs.setTabText(self.tabs.indexOf(self.welcome), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.bordersettings.setTitle(QCoreApplication.translate("MainWindow", u"Border Settings", None))
        self.border_style_label.setText(QCoreApplication.translate("MainWindow", u"Border Style", None))
        self.border_style_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.border_color_label.setText(QCoreApplication.translate("MainWindow", u"Border Color", None))
        self.border_color_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.spritesettings.setTitle(QCoreApplication.translate("MainWindow", u"Sprite Settings", None))
        self.universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.universe_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.character_label.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.character_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expression_label.setText(QCoreApplication.translate("MainWindow", u"Expression", None))
        self.expression_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expression_color_label.setText(QCoreApplication.translate("MainWindow", u"Expression Color", None))
        self.expression_color_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.fontsettings.setTitle(QCoreApplication.translate("MainWindow", u"Font Settings", None))
        self.font_label.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.asterisk_label.setText(QCoreApplication.translate("MainWindow", u"Asterisk", None))
        self.asterisk_checkbox.setText("")
        self.asterisk_color.setText(QCoreApplication.translate("MainWindow", u"Asterisk Color", None))
        self.asterisk_color_values.setText(QCoreApplication.translate("MainWindow", u"Values", None))
        self.asterisk_color_preview_1.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.asterisk_color_preview_2.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.asterisk_color_preview_3.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.text_style_label.setText(QCoreApplication.translate("MainWindow", u"Text Style", None))
        self.text_style_regular_option.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.text_style_dark_world_option.setText(QCoreApplication.translate("MainWindow", u"Dark World", None))
        self.text_transform_label.setText(QCoreApplication.translate("MainWindow", u"Text Transform", None))
        self.exportsettings.setTitle(QCoreApplication.translate("MainWindow", u"Export Settings", None))
        self.format_label.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.format_png_option.setText(QCoreApplication.translate("MainWindow", u"PNG", None))
        self.format_gif_option.setText(QCoreApplication.translate("MainWindow", u"GIF", None))
        self.margin_label.setText(QCoreApplication.translate("MainWindow", u"Margin", None))
        self.margin_checkbox.setText("")
        self.size_label.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.size_small_option.setText(QCoreApplication.translate("MainWindow", u"Small", None))
        self.size_medium_option.setText(QCoreApplication.translate("MainWindow", u"Medium", None))
        self.size_big_option.setText(QCoreApplication.translate("MainWindow", u"Big", None))
        self.input_preview.setTitle(QCoreApplication.translate("MainWindow", u"Input/Preview", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write your text here.", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.output.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"Download Textbox", None))
        self.tabs.setTabText(self.tabs.indexOf(self.generator), QCoreApplication.translate("MainWindow", u"Generator", None))
        self.existing.setTitle(QCoreApplication.translate("MainWindow", u"Existing", None))
        self.universe_filter_label.setText(QCoreApplication.translate("MainWindow", u"Filter by name", None))
        self.universe_filter_button.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Test3", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_18.setText("")
        self.pushButton_16.setText("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Test2", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Test7", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_33.setText("")
        self.pushButton_35.setText("")
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Test8", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_37.setText("")
        self.pushButton_39.setText("")
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Test4", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_22.setText("")
        self.pushButton_20.setText("")
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Test6", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_30.setText("")
        self.pushButton_28.setText("")
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.universe_test1.setTitle(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.universe_test1_preview_image.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.universe_test1_left.setText("")
        self.universe_test1_right.setText("")
        self.universe_test1_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.universe_test1_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Test9", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_41.setText("")
        self.pushButton_43.setText("")
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Test5", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_26.setText("")
        self.pushButton_24.setText("")
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.create_universe.setTitle(QCoreApplication.translate("MainWindow", u"Create a new Universe", None))
        self.universe_create_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.universe_create_preview_label.setText(QCoreApplication.translate("MainWindow", u"Preview image (optional)", None))
        self.universe_create_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.universe_create_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.universe_create_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.edit_universe.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.universe_edit_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.universe_edit_preview_label.setText(QCoreApplication.translate("MainWindow", u"Preview image", None))
        self.universe_edit_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.universe_edit_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.universe_edit_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabs.setTabText(self.tabs.indexOf(self.universes), QCoreApplication.translate("MainWindow", u"Universes", None))
        self.create_character.setTitle(QCoreApplication.translate("MainWindow", u"Create a new Character", None))
        self.characters_create_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.characters_create_universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.characters_create_style_label.setText(QCoreApplication.translate("MainWindow", u"Default Style", None))
        self.characters_create_style_regular_option.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.characters_create_style_dark_world_option.setText(QCoreApplication.translate("MainWindow", u"Dark World", None))
        self.characters_create_transform_label.setText(QCoreApplication.translate("MainWindow", u"Default Text Transform", None))
        self.characters_create_preview_label.setText(QCoreApplication.translate("MainWindow", u"Preview image (optional)", None))
        self.characters_create_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.characters_create_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.characters_create_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.edit_character.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.characters_edit_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.characters_edit_universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.characters_edit_style_label.setText(QCoreApplication.translate("MainWindow", u"Default Style", None))
        self.characters_edit_style_regular_option.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.characters_edit_style_dark_world_option.setText(QCoreApplication.translate("MainWindow", u"Dark World", None))
        self.characters_edit_transform_label.setText(QCoreApplication.translate("MainWindow", u"Default Text Transform", None))
        self.characters_edit_preview_label.setText(QCoreApplication.translate("MainWindow", u"Preview image (optional)", None))
        self.characters_edit_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.characters_edit_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.characters_edit_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Existing", None))
        self.characters_filter_label.setText(QCoreApplication.translate("MainWindow", u"Filter by name", None))
        self.characters_filter_button.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.characters_test1.setTitle(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.characters_test1_preview_image.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.characters_test1_left.setText("")
        self.characters_test1_right.setText("")
        self.characters_test1_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.characters_test1_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Test2", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_48.setText("")
        self.pushButton_49.setText("")
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Test3", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.pushButton_60.setText("")
        self.pushButton_61.setText("")
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabs.setTabText(self.tabs.indexOf(self.characters), QCoreApplication.translate("MainWindow", u"Characters", None))
        self.create_expression.setTitle(QCoreApplication.translate("MainWindow", u"Create a new expression", None))
        self.expressions_create_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.expressions_create_universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.expressions_create_character_label.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.expressions_create_preview_label.setText(QCoreApplication.translate("MainWindow", u"Image (required)", None))
        self.expressions_create_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.expressions_create_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expressions_create_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.edit_expression.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.expressions_edit_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.expressions_edit_universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.expressions_edit_character_label.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.expressions_edit_preview_label.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.expressions_edit_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.expressions_edit_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expressions_edit_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Existing", None))
        self.expressions_filter_label.setText(QCoreApplication.translate("MainWindow", u"Filter by name", None))
        self.expressions_filter_button.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.tabs.setTabText(self.tabs.indexOf(self.expressions), QCoreApplication.translate("MainWindow", u"Expressions", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

