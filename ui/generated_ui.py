# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiVkvtmn.ui'
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
        MainWindow.resize(1080, 842)
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

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_7)

        self.kofi = QLabel(self.welcome)
        self.kofi.setObjectName(u"kofi")
        self.kofi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.kofi.setOpenExternalLinks(True)

        self.verticalLayout_36.addWidget(self.kofi)

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
        self.gridLayout_6 = QGridLayout(self.generator)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea_4 = QScrollArea(self.generator)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy3.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy3)
        self.scrollArea_4.setMinimumSize(QSize(1000, 600))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 996, 1124))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 0))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.settings = QGroupBox(self.scrollAreaWidgetContents_2)
        self.settings.setObjectName(u"settings")
        sizePolicy3.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy3)
        self.settings.setMinimumSize(QSize(950, 500))
        self.gridLayout_11 = QGridLayout(self.settings)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tabWidget = QTabWidget(self.settings)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy3.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy3)
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_10 = QFrame(self.tab)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_28 = QFrame(self.tab)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.Shape.VLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_28)

        self.border_style_label = QLabel(self.tab)
        self.border_style_label.setObjectName(u"border_style_label")
        font = QFont()
        font.setPointSize(13)
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.border_style_label.setFont(font)
        self.border_style_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.border_style_label)

        self.border_style_selector = QComboBox(self.tab)
        self.border_style_selector.setObjectName(u"border_style_selector")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.border_style_selector.sizePolicy().hasHeightForWidth())
        self.border_style_selector.setSizePolicy(sizePolicy4)
        self.border_style_selector.setMinimumSize(QSize(49, 0))

        self.horizontalLayout_3.addWidget(self.border_style_selector)

        self.horizontalSpacer_10 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.border_style_preview = QLabel(self.tab)
        self.border_style_preview.setObjectName(u"border_style_preview")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.border_style_preview.sizePolicy().hasHeightForWidth())
        self.border_style_preview.setSizePolicy(sizePolicy5)
        self.border_style_preview.setMinimumSize(QSize(67, 70))
        self.border_style_preview.setMaximumSize(QSize(67, 70))
        self.border_style_preview.setAutoFillBackground(True)
        self.border_style_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.border_style_preview)

        self.horizontalSpacer_9 = QSpacerItem(105, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.line_29 = QFrame(self.tab)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.Shape.VLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_29)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line_6 = QFrame(self.tab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_31 = QFrame(self.tab)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_31)

        self.border_color_label = QLabel(self.tab)
        self.border_color_label.setObjectName(u"border_color_label")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setWeight(QFont.DemiBold)
        self.border_color_label.setFont(font1)
        self.border_color_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.border_color_label)

        self.border_color_selector = QComboBox(self.tab)
        self.border_color_selector.setObjectName(u"border_color_selector")

        self.horizontalLayout_4.addWidget(self.border_color_selector)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_23)

        self.border_color_preview = QLabel(self.tab)
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

        self.line_32 = QFrame(self.tab)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.Shape.VLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_32)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.line_30 = QFrame(self.tab)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.Shape.HLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_30)


        self.gridLayout_8.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_9 = QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line_36 = QFrame(self.tab_2)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.Shape.HLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_36)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.line_33 = QFrame(self.tab_2)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.Shape.VLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_43.addWidget(self.line_33)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_9)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_43.addWidget(self.label_10)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalSpacer_35 = QSpacerItem(195, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_35)

        self.include_checkbox = QCheckBox(self.tab_2)
        self.include_checkbox.setObjectName(u"include_checkbox")
        sizePolicy5.setHeightForWidth(self.include_checkbox.sizePolicy().hasHeightForWidth())
        self.include_checkbox.setSizePolicy(sizePolicy5)
        self.include_checkbox.setChecked(True)

        self.horizontalLayout_69.addWidget(self.include_checkbox)

        self.horizontalSpacer_36 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_36)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_69)

        self.line_66 = QFrame(self.tab_2)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setFrameShape(QFrame.Shape.VLine)
        self.line_66.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_43.addWidget(self.line_66)


        self.verticalLayout_4.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.line_34 = QFrame(self.tab_2)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.Shape.VLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_34)

        self.universe_label = QLabel(self.tab_2)
        self.universe_label.setObjectName(u"universe_label")
        self.universe_label.setFont(font1)
        self.universe_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.universe_label)

        self.universe_selector = QComboBox(self.tab_2)
        self.universe_selector.setObjectName(u"universe_selector")

        self.horizontalLayout_10.addWidget(self.universe_selector)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalSpacer_12 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_12)

        self.universe_preview = QLabel(self.tab_2)
        self.universe_preview.setObjectName(u"universe_preview")
        sizePolicy5.setHeightForWidth(self.universe_preview.sizePolicy().hasHeightForWidth())
        self.universe_preview.setSizePolicy(sizePolicy5)
        self.universe_preview.setMinimumSize(QSize(230, 100))
        self.universe_preview.setMaximumSize(QSize(230, 100))
        self.universe_preview.setAutoFillBackground(True)
        self.universe_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_68.addWidget(self.universe_preview)

        self.horizontalSpacer_11 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_68)

        self.line_35 = QFrame(self.tab_2)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.Shape.VLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_35)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.line_5 = QFrame(self.tab_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.line_38 = QFrame(self.tab_2)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_13.addWidget(self.line_38)

        self.character_label = QLabel(self.tab_2)
        self.character_label.setObjectName(u"character_label")
        self.character_label.setFont(font1)
        self.character_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.character_label)

        self.character_selector = QComboBox(self.tab_2)
        self.character_selector.setObjectName(u"character_selector")

        self.horizontalLayout_13.addWidget(self.character_selector)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalSpacer_14 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_14)

        self.character_preview = QLabel(self.tab_2)
        self.character_preview.setObjectName(u"character_preview")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(230)
        sizePolicy6.setVerticalStretch(100)
        sizePolicy6.setHeightForWidth(self.character_preview.sizePolicy().hasHeightForWidth())
        self.character_preview.setSizePolicy(sizePolicy6)
        self.character_preview.setMinimumSize(QSize(230, 100))
        self.character_preview.setMaximumSize(QSize(100, 100))
        self.character_preview.setAutoFillBackground(True)
        self.character_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_60.addWidget(self.character_preview)

        self.horizontalSpacer_13 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_13)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_60)

        self.line_43 = QFrame(self.tab_2)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_13.addWidget(self.line_43)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.line_4 = QFrame(self.tab_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.line_39 = QFrame(self.tab_2)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.Shape.VLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_39)

        self.expression_label = QLabel(self.tab_2)
        self.expression_label.setObjectName(u"expression_label")
        self.expression_label.setFont(font1)
        self.expression_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.expression_label)

        self.expression_selector = QComboBox(self.tab_2)
        self.expression_selector.setObjectName(u"expression_selector")
        self.expression_selector.setMaxVisibleItems(10)

        self.horizontalLayout_15.addWidget(self.expression_selector)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalSpacer_16 = QSpacerItem(170, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_16)

        self.expression_preview = QLabel(self.tab_2)
        self.expression_preview.setObjectName(u"expression_preview")
        sizePolicy5.setHeightForWidth(self.expression_preview.sizePolicy().hasHeightForWidth())
        self.expression_preview.setSizePolicy(sizePolicy5)
        self.expression_preview.setMinimumSize(QSize(69, 70))
        self.expression_preview.setMaximumSize(QSize(69, 70))
        self.expression_preview.setSizeIncrement(QSize(69, 70))
        self.expression_preview.setAutoFillBackground(True)
        self.expression_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.expression_preview)

        self.horizontalSpacer_15 = QSpacerItem(170, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_15)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_44)

        self.line_42 = QFrame(self.tab_2)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.Shape.VLine)
        self.line_42.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_42)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.line_3 = QFrame(self.tab_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.line_40 = QFrame(self.tab_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.Shape.VLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_40)

        self.expression_color_label = QLabel(self.tab_2)
        self.expression_color_label.setObjectName(u"expression_color_label")
        self.expression_color_label.setFont(font1)
        self.expression_color_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.expression_color_label)

        self.expression_color_selector = QComboBox(self.tab_2)
        self.expression_color_selector.setObjectName(u"expression_color_selector")

        self.horizontalLayout_11.addWidget(self.expression_color_selector)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalSpacer_24 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_24)

        self.expression_color_preview = QLabel(self.tab_2)
        self.expression_color_preview.setObjectName(u"expression_color_preview")
        sizePolicy5.setHeightForWidth(self.expression_color_preview.sizePolicy().hasHeightForWidth())
        self.expression_color_preview.setSizePolicy(sizePolicy5)
        self.expression_color_preview.setMinimumSize(QSize(200, 30))
        self.expression_color_preview.setMaximumSize(QSize(200, 30))
        self.expression_color_preview.setAutoFillBackground(True)
        self.expression_color_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_70.addWidget(self.expression_color_preview)

        self.horizontalSpacer_17 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_17)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_70)

        self.line_41 = QFrame(self.tab_2)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.Shape.VLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_41)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.line_37 = QFrame(self.tab_2)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.Shape.HLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_37)


        self.gridLayout_9.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_14 = QGridLayout(self.tab_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.line_83 = QFrame(self.tab_5)
        self.line_83.setObjectName(u"line_83")
        self.line_83.setFrameShape(QFrame.Shape.HLine)
        self.line_83.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_23.addWidget(self.line_83)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.line_84 = QFrame(self.tab_5)
        self.line_84.setObjectName(u"line_84")
        self.line_84.setFrameShape(QFrame.Shape.VLine)
        self.line_84.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_90.addWidget(self.line_84)

        self.label_16 = QLabel(self.tab_5)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMinimumSize(QSize(0, 0))
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_90.addWidget(self.label_16)

        self.label_17 = QLabel(self.tab_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_90.addWidget(self.label_17)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalSpacer_49 = QSpacerItem(195, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_49)

        self.include_checkbox_2 = QCheckBox(self.tab_5)
        self.include_checkbox_2.setObjectName(u"include_checkbox_2")
        sizePolicy5.setHeightForWidth(self.include_checkbox_2.sizePolicy().hasHeightForWidth())
        self.include_checkbox_2.setSizePolicy(sizePolicy5)
        self.include_checkbox_2.setChecked(False)

        self.horizontalLayout_91.addWidget(self.include_checkbox_2)

        self.horizontalSpacer_50 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_50)


        self.horizontalLayout_90.addLayout(self.horizontalLayout_91)

        self.line_85 = QFrame(self.tab_5)
        self.line_85.setObjectName(u"line_85")
        self.line_85.setFrameShape(QFrame.Shape.VLine)
        self.line_85.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_90.addWidget(self.line_85)


        self.verticalLayout_23.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.line_86 = QFrame(self.tab_5)
        self.line_86.setObjectName(u"line_86")
        self.line_86.setFrameShape(QFrame.Shape.VLine)
        self.line_86.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_92.addWidget(self.line_86)

        self.universe_label_2 = QLabel(self.tab_5)
        self.universe_label_2.setObjectName(u"universe_label_2")
        self.universe_label_2.setFont(font1)
        self.universe_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_92.addWidget(self.universe_label_2)

        self.universe_selector_2 = QComboBox(self.tab_5)
        self.universe_selector_2.setObjectName(u"universe_selector_2")

        self.horizontalLayout_92.addWidget(self.universe_selector_2)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalSpacer_51 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_51)

        self.universe_preview_2 = QLabel(self.tab_5)
        self.universe_preview_2.setObjectName(u"universe_preview_2")
        sizePolicy5.setHeightForWidth(self.universe_preview_2.sizePolicy().hasHeightForWidth())
        self.universe_preview_2.setSizePolicy(sizePolicy5)
        self.universe_preview_2.setMinimumSize(QSize(230, 100))
        self.universe_preview_2.setMaximumSize(QSize(230, 100))
        self.universe_preview_2.setAutoFillBackground(True)
        self.universe_preview_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_93.addWidget(self.universe_preview_2)

        self.horizontalSpacer_52 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_52)


        self.horizontalLayout_92.addLayout(self.horizontalLayout_93)

        self.line_87 = QFrame(self.tab_5)
        self.line_87.setObjectName(u"line_87")
        self.line_87.setFrameShape(QFrame.Shape.VLine)
        self.line_87.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_92.addWidget(self.line_87)


        self.verticalLayout_23.addLayout(self.horizontalLayout_92)

        self.line_88 = QFrame(self.tab_5)
        self.line_88.setObjectName(u"line_88")
        self.line_88.setFrameShape(QFrame.Shape.HLine)
        self.line_88.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_23.addWidget(self.line_88)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.line_89 = QFrame(self.tab_5)
        self.line_89.setObjectName(u"line_89")
        self.line_89.setFrameShape(QFrame.Shape.VLine)
        self.line_89.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_94.addWidget(self.line_89)

        self.character_label_2 = QLabel(self.tab_5)
        self.character_label_2.setObjectName(u"character_label_2")
        self.character_label_2.setFont(font1)
        self.character_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_94.addWidget(self.character_label_2)

        self.character_selector_2 = QComboBox(self.tab_5)
        self.character_selector_2.setObjectName(u"character_selector_2")

        self.horizontalLayout_94.addWidget(self.character_selector_2)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalSpacer_53 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_53)

        self.character_preview_2 = QLabel(self.tab_5)
        self.character_preview_2.setObjectName(u"character_preview_2")
        sizePolicy6.setHeightForWidth(self.character_preview_2.sizePolicy().hasHeightForWidth())
        self.character_preview_2.setSizePolicy(sizePolicy6)
        self.character_preview_2.setMinimumSize(QSize(230, 100))
        self.character_preview_2.setMaximumSize(QSize(100, 100))
        self.character_preview_2.setAutoFillBackground(True)
        self.character_preview_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_95.addWidget(self.character_preview_2)

        self.horizontalSpacer_54 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_54)


        self.horizontalLayout_94.addLayout(self.horizontalLayout_95)

        self.line_90 = QFrame(self.tab_5)
        self.line_90.setObjectName(u"line_90")
        self.line_90.setFrameShape(QFrame.Shape.VLine)
        self.line_90.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_94.addWidget(self.line_90)


        self.verticalLayout_23.addLayout(self.horizontalLayout_94)

        self.line_91 = QFrame(self.tab_5)
        self.line_91.setObjectName(u"line_91")
        self.line_91.setFrameShape(QFrame.Shape.HLine)
        self.line_91.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_23.addWidget(self.line_91)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.line_92 = QFrame(self.tab_5)
        self.line_92.setObjectName(u"line_92")
        self.line_92.setFrameShape(QFrame.Shape.VLine)
        self.line_92.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_96.addWidget(self.line_92)

        self.expression_label_2 = QLabel(self.tab_5)
        self.expression_label_2.setObjectName(u"expression_label_2")
        self.expression_label_2.setFont(font1)
        self.expression_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_96.addWidget(self.expression_label_2)

        self.expression_selector_2 = QComboBox(self.tab_5)
        self.expression_selector_2.setObjectName(u"expression_selector_2")
        self.expression_selector_2.setMaxVisibleItems(10)

        self.horizontalLayout_96.addWidget(self.expression_selector_2)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalSpacer_55 = QSpacerItem(170, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_55)

        self.expression_preview_2 = QLabel(self.tab_5)
        self.expression_preview_2.setObjectName(u"expression_preview_2")
        sizePolicy5.setHeightForWidth(self.expression_preview_2.sizePolicy().hasHeightForWidth())
        self.expression_preview_2.setSizePolicy(sizePolicy5)
        self.expression_preview_2.setMinimumSize(QSize(69, 70))
        self.expression_preview_2.setMaximumSize(QSize(69, 70))
        self.expression_preview_2.setSizeIncrement(QSize(69, 70))
        self.expression_preview_2.setAutoFillBackground(True)
        self.expression_preview_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_97.addWidget(self.expression_preview_2)

        self.horizontalSpacer_56 = QSpacerItem(170, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_56)


        self.horizontalLayout_96.addLayout(self.horizontalLayout_97)

        self.line_93 = QFrame(self.tab_5)
        self.line_93.setObjectName(u"line_93")
        self.line_93.setFrameShape(QFrame.Shape.VLine)
        self.line_93.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_96.addWidget(self.line_93)


        self.verticalLayout_23.addLayout(self.horizontalLayout_96)

        self.line_94 = QFrame(self.tab_5)
        self.line_94.setObjectName(u"line_94")
        self.line_94.setFrameShape(QFrame.Shape.HLine)
        self.line_94.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_23.addWidget(self.line_94)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.line_95 = QFrame(self.tab_5)
        self.line_95.setObjectName(u"line_95")
        self.line_95.setFrameShape(QFrame.Shape.VLine)
        self.line_95.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_98.addWidget(self.line_95)

        self.expression_color_label_2 = QLabel(self.tab_5)
        self.expression_color_label_2.setObjectName(u"expression_color_label_2")
        self.expression_color_label_2.setFont(font1)
        self.expression_color_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_98.addWidget(self.expression_color_label_2)

        self.expression_color_selector_2 = QComboBox(self.tab_5)
        self.expression_color_selector_2.setObjectName(u"expression_color_selector_2")

        self.horizontalLayout_98.addWidget(self.expression_color_selector_2)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalSpacer_57 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_57)

        self.expression_color_preview_2 = QLabel(self.tab_5)
        self.expression_color_preview_2.setObjectName(u"expression_color_preview_2")
        sizePolicy5.setHeightForWidth(self.expression_color_preview_2.sizePolicy().hasHeightForWidth())
        self.expression_color_preview_2.setSizePolicy(sizePolicy5)
        self.expression_color_preview_2.setMinimumSize(QSize(200, 30))
        self.expression_color_preview_2.setMaximumSize(QSize(200, 30))
        self.expression_color_preview_2.setAutoFillBackground(True)
        self.expression_color_preview_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_99.addWidget(self.expression_color_preview_2)

        self.horizontalSpacer_58 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_58)


        self.horizontalLayout_98.addLayout(self.horizontalLayout_99)

        self.line_96 = QFrame(self.tab_5)
        self.line_96.setObjectName(u"line_96")
        self.line_96.setFrameShape(QFrame.Shape.VLine)
        self.line_96.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_98.addWidget(self.line_96)


        self.verticalLayout_23.addLayout(self.horizontalLayout_98)

        self.line_97 = QFrame(self.tab_5)
        self.line_97.setObjectName(u"line_97")
        self.line_97.setFrameShape(QFrame.Shape.HLine)
        self.line_97.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_23.addWidget(self.line_97)


        self.gridLayout_14.addLayout(self.verticalLayout_23, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_10 = QGridLayout(self.tab_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.line_46 = QFrame(self.tab_3)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShape(QFrame.Shape.HLine)
        self.line_46.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_46)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.line_44 = QFrame(self.tab_3)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.Shape.VLine)
        self.line_44.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_16.addWidget(self.line_44)

        self.font_label = QLabel(self.tab_3)
        self.font_label.setObjectName(u"font_label")
        self.font_label.setMinimumSize(QSize(300, 0))
        self.font_label.setFont(font1)
        self.font_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.font_label)

        self.font_selector = QComboBox(self.tab_3)
        self.font_selector.setObjectName(u"font_selector")

        self.horizontalLayout_16.addWidget(self.font_selector)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_26)

        self.horizontalSpacer_25 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_25)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_18)

        self.line_45 = QFrame(self.tab_3)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.Shape.VLine)
        self.line_45.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_16.addWidget(self.line_45)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.line_7 = QFrame(self.tab_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_7)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.line_52 = QFrame(self.tab_3)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setFrameShape(QFrame.Shape.VLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_17.addWidget(self.line_52)

        self.asterisk_label = QLabel(self.tab_3)
        self.asterisk_label.setObjectName(u"asterisk_label")
        self.asterisk_label.setMinimumSize(QSize(300, 0))
        self.asterisk_label.setFont(font1)
        self.asterisk_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.asterisk_label)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_20.addWidget(self.label)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_20.addWidget(self.label_4)

        self.asterisk_checkbox = QCheckBox(self.tab_3)
        self.asterisk_checkbox.setObjectName(u"asterisk_checkbox")
        self.asterisk_checkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.asterisk_checkbox.setChecked(True)

        self.horizontalLayout_20.addWidget(self.asterisk_checkbox)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_20.addWidget(self.label_2)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_20)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_43)

        self.horizontalSpacer_42 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_42)

        self.horizontalSpacer_29 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_29)

        self.line_57 = QFrame(self.tab_3)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShape(QFrame.Shape.VLine)
        self.line_57.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_17.addWidget(self.line_57)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.line_51 = QFrame(self.tab_3)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.Shape.VLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_18.addWidget(self.line_51)

        self.asterisk_color_everything = QWidget(self.tab_3)
        self.asterisk_color_everything.setObjectName(u"asterisk_color_everything")
        self.horizontalLayout_41 = QHBoxLayout(self.asterisk_color_everything)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.asterisk_color = QLabel(self.asterisk_color_everything)
        self.asterisk_color.setObjectName(u"asterisk_color")
        self.asterisk_color.setMinimumSize(QSize(300, 0))
        self.asterisk_color.setFont(font1)
        self.asterisk_color.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_41.addWidget(self.asterisk_color)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.asterisk_color_selector_1 = QComboBox(self.asterisk_color_everything)
        self.asterisk_color_selector_1.setObjectName(u"asterisk_color_selector_1")

        self.horizontalLayout_5.addWidget(self.asterisk_color_selector_1)

        self.asterisk_color_selector_2 = QComboBox(self.asterisk_color_everything)
        self.asterisk_color_selector_2.setObjectName(u"asterisk_color_selector_2")

        self.horizontalLayout_5.addWidget(self.asterisk_color_selector_2)

        self.asterisk_color_selector_3 = QComboBox(self.asterisk_color_everything)
        self.asterisk_color_selector_3.setObjectName(u"asterisk_color_selector_3")

        self.horizontalLayout_5.addWidget(self.asterisk_color_selector_3)


        self.horizontalLayout_41.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_32)

        self.horizontalSpacer_19 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_19)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_31)


        self.horizontalLayout_18.addWidget(self.asterisk_color_everything)

        self.line_56 = QFrame(self.tab_3)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.Shape.VLine)
        self.line_56.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_18.addWidget(self.line_56)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.line_50 = QFrame(self.tab_3)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.Shape.VLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_52.addWidget(self.line_50)

        self.asterisk_color_values_everything = QWidget(self.tab_3)
        self.asterisk_color_values_everything.setObjectName(u"asterisk_color_values_everything")
        self.horizontalLayout_42 = QHBoxLayout(self.asterisk_color_values_everything)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.asterisk_color_values = QLabel(self.asterisk_color_values_everything)
        self.asterisk_color_values.setObjectName(u"asterisk_color_values")
        self.asterisk_color_values.setMinimumSize(QSize(300, 0))
        self.asterisk_color_values.setFont(font1)
        self.asterisk_color_values.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_42.addWidget(self.asterisk_color_values)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.asterisk_color_preview_1 = QLabel(self.asterisk_color_values_everything)
        self.asterisk_color_preview_1.setObjectName(u"asterisk_color_preview_1")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.asterisk_color_preview_1.sizePolicy().hasHeightForWidth())
        self.asterisk_color_preview_1.setSizePolicy(sizePolicy7)
        self.asterisk_color_preview_1.setMinimumSize(QSize(0, 30))
        self.asterisk_color_preview_1.setMaximumSize(QSize(16777215, 30))
        self.asterisk_color_preview_1.setAutoFillBackground(True)
        self.asterisk_color_preview_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.asterisk_color_preview_1)

        self.asterisk_color_preview_2 = QLabel(self.asterisk_color_values_everything)
        self.asterisk_color_preview_2.setObjectName(u"asterisk_color_preview_2")
        sizePolicy7.setHeightForWidth(self.asterisk_color_preview_2.sizePolicy().hasHeightForWidth())
        self.asterisk_color_preview_2.setSizePolicy(sizePolicy7)
        self.asterisk_color_preview_2.setMinimumSize(QSize(0, 30))
        self.asterisk_color_preview_2.setMaximumSize(QSize(16777215, 30))
        self.asterisk_color_preview_2.setAutoFillBackground(True)
        self.asterisk_color_preview_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.asterisk_color_preview_2)

        self.asterisk_color_preview_3 = QLabel(self.asterisk_color_values_everything)
        self.asterisk_color_preview_3.setObjectName(u"asterisk_color_preview_3")
        sizePolicy7.setHeightForWidth(self.asterisk_color_preview_3.sizePolicy().hasHeightForWidth())
        self.asterisk_color_preview_3.setSizePolicy(sizePolicy7)
        self.asterisk_color_preview_3.setMinimumSize(QSize(0, 30))
        self.asterisk_color_preview_3.setMaximumSize(QSize(16777215, 30))
        self.asterisk_color_preview_3.setAutoFillBackground(True)
        self.asterisk_color_preview_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.asterisk_color_preview_3)


        self.horizontalLayout_42.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_34)

        self.horizontalSpacer_20 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_20)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_33)


        self.horizontalLayout_52.addWidget(self.asterisk_color_values_everything)

        self.line_55 = QFrame(self.tab_3)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.Shape.VLine)
        self.line_55.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_52.addWidget(self.line_55)


        self.verticalLayout_5.addLayout(self.horizontalLayout_52)

        self.line_9 = QFrame(self.tab_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_9)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.line_49 = QFrame(self.tab_3)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.Shape.VLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_19.addWidget(self.line_49)

        self.text_style_label = QLabel(self.tab_3)
        self.text_style_label.setObjectName(u"text_style_label")
        self.text_style_label.setMinimumSize(QSize(300, 0))
        self.text_style_label.setFont(font1)
        self.text_style_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.text_style_label)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.text_style_regular_option = QRadioButton(self.tab_3)
        self.text_style_regular_option.setObjectName(u"text_style_regular_option")
        sizePolicy7.setHeightForWidth(self.text_style_regular_option.sizePolicy().hasHeightForWidth())
        self.text_style_regular_option.setSizePolicy(sizePolicy7)
        self.text_style_regular_option.setChecked(True)

        self.horizontalLayout_12.addWidget(self.text_style_regular_option)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_12.addWidget(self.label_3)

        self.text_style_dark_world_option = QRadioButton(self.tab_3)
        self.text_style_dark_world_option.setObjectName(u"text_style_dark_world_option")
        sizePolicy7.setHeightForWidth(self.text_style_dark_world_option.sizePolicy().hasHeightForWidth())
        self.text_style_dark_world_option.setSizePolicy(sizePolicy7)

        self.horizontalLayout_12.addWidget(self.text_style_dark_world_option)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_12)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_38)

        self.horizontalSpacer_37 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_37)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_39)

        self.line_54 = QFrame(self.tab_3)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShape(QFrame.Shape.VLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_19.addWidget(self.line_54)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.line_48 = QFrame(self.tab_3)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShape(QFrame.Shape.VLine)
        self.line_48.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_21.addWidget(self.line_48)

        self.text_transform_label = QLabel(self.tab_3)
        self.text_transform_label.setObjectName(u"text_transform_label")
        self.text_transform_label.setMinimumSize(QSize(300, 0))
        self.text_transform_label.setFont(font1)
        self.text_transform_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.text_transform_label)

        self.text_transform_selector = QComboBox(self.tab_3)
        self.text_transform_selector.setObjectName(u"text_transform_selector")

        self.horizontalLayout_21.addWidget(self.text_transform_selector)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_28)

        self.horizontalSpacer_21 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)

        self.line_53 = QFrame(self.tab_3)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setFrameShape(QFrame.Shape.VLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_21.addWidget(self.line_53)


        self.verticalLayout_5.addLayout(self.horizontalLayout_21)


        self.gridLayout_10.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.line_47 = QFrame(self.tab_3)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.Shape.HLine)
        self.line_47.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_47, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_12 = QGridLayout(self.tab_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line_60 = QFrame(self.tab_4)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setFrameShape(QFrame.Shape.HLine)
        self.line_60.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_60)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.line_58 = QFrame(self.tab_4)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.Shape.VLine)
        self.line_58.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_58)

        self.format_label = QLabel(self.tab_4)
        self.format_label.setObjectName(u"format_label")
        self.format_label.setFont(font1)
        self.format_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.format_label)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.widget_4 = QWidget(self.tab_4)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.format_png_option = QRadioButton(self.widget_4)
        self.format_png_option.setObjectName(u"format_png_option")
        self.format_png_option.setChecked(True)

        self.horizontalLayout_39.addWidget(self.format_png_option)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_39.addWidget(self.label_6)

        self.format_gif_option = QRadioButton(self.widget_4)
        self.format_gif_option.setObjectName(u"format_gif_option")

        self.horizontalLayout_39.addWidget(self.format_gif_option)


        self.horizontalLayout_30.addWidget(self.widget_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_30)

        self.widget = QWidget(self.tab_4)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_22 = QHBoxLayout(self.widget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")

        self.horizontalLayout_6.addWidget(self.widget)

        self.line_65 = QFrame(self.tab_4)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setFrameShape(QFrame.Shape.VLine)
        self.line_65.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_65)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.line_69 = QFrame(self.tab_4)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setFrameShape(QFrame.Shape.HLine)
        self.line_69.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_69)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.line_67 = QFrame(self.tab_4)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setFrameShape(QFrame.Shape.VLine)
        self.line_67.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_74.addWidget(self.line_67)

        self.alternating_everything = QWidget(self.tab_4)
        self.alternating_everything.setObjectName(u"alternating_everything")
        self.horizontalLayout_76 = QHBoxLayout(self.alternating_everything)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.alternating_label = QLabel(self.alternating_everything)
        self.alternating_label.setObjectName(u"alternating_label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.alternating_label.sizePolicy().hasHeightForWidth())
        self.alternating_label.setSizePolicy(sizePolicy8)
        self.alternating_label.setMinimumSize(QSize(300, 0))
        self.alternating_label.setFont(font1)
        self.alternating_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_76.addWidget(self.alternating_label)

        self.alternating_selector = QComboBox(self.alternating_everything)
        self.alternating_selector.setObjectName(u"alternating_selector")

        self.horizontalLayout_76.addWidget(self.alternating_selector)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalSpacer_44 = QSpacerItem(170, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_44)

        self.alternating_preview = QLabel(self.alternating_everything)
        self.alternating_preview.setObjectName(u"alternating_preview")
        self.alternating_preview.setMinimumSize(QSize(69, 70))
        self.alternating_preview.setMaximumSize(QSize(69, 70))
        self.alternating_preview.setAutoFillBackground(True)
        self.alternating_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_75.addWidget(self.alternating_preview)

        self.horizontalSpacer_45 = QSpacerItem(170, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_45)


        self.horizontalLayout_76.addLayout(self.horizontalLayout_75)


        self.horizontalLayout_74.addWidget(self.alternating_everything)

        self.line_68 = QFrame(self.tab_4)
        self.line_68.setObjectName(u"line_68")
        self.line_68.setFrameShape(QFrame.Shape.VLine)
        self.line_68.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_74.addWidget(self.line_68)


        self.verticalLayout_3.addLayout(self.horizontalLayout_74)

        self.line = QFrame(self.tab_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.line_72 = QFrame(self.tab_4)
        self.line_72.setObjectName(u"line_72")
        self.line_72.setFrameShape(QFrame.Shape.VLine)
        self.line_72.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_77.addWidget(self.line_72)

        self.alternating_everything_right = QWidget(self.tab_4)
        self.alternating_everything_right.setObjectName(u"alternating_everything_right")
        self.horizontalLayout_79 = QHBoxLayout(self.alternating_everything_right)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.alternating_right_label = QLabel(self.alternating_everything_right)
        self.alternating_right_label.setObjectName(u"alternating_right_label")
        self.alternating_right_label.setMinimumSize(QSize(300, 0))
        self.alternating_right_label.setFont(font1)
        self.alternating_right_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_79.addWidget(self.alternating_right_label)

        self.alternating_right_selector = QComboBox(self.alternating_everything_right)
        self.alternating_right_selector.setObjectName(u"alternating_right_selector")

        self.horizontalLayout_79.addWidget(self.alternating_right_selector)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalSpacer_46 = QSpacerItem(170, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_46)

        self.alternating_right_preview = QLabel(self.alternating_everything_right)
        self.alternating_right_preview.setObjectName(u"alternating_right_preview")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.alternating_right_preview.sizePolicy().hasHeightForWidth())
        self.alternating_right_preview.setSizePolicy(sizePolicy9)
        self.alternating_right_preview.setMinimumSize(QSize(69, 70))
        self.alternating_right_preview.setMaximumSize(QSize(69, 70))
        self.alternating_right_preview.setAutoFillBackground(True)
        self.alternating_right_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_78.addWidget(self.alternating_right_preview)

        self.horizontalSpacer_47 = QSpacerItem(170, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_47)


        self.horizontalLayout_79.addLayout(self.horizontalLayout_78)


        self.horizontalLayout_77.addWidget(self.alternating_everything_right)

        self.line_71 = QFrame(self.tab_4)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setFrameShape(QFrame.Shape.VLine)
        self.line_71.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_77.addWidget(self.line_71)


        self.verticalLayout_3.addLayout(self.horizontalLayout_77)

        self.line_70 = QFrame(self.tab_4)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setFrameShape(QFrame.Shape.HLine)
        self.line_70.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_70)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.line_63 = QFrame(self.tab_4)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.Shape.VLine)
        self.line_63.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_63)

        self.margin_label = QLabel(self.tab_4)
        self.margin_label.setObjectName(u"margin_label")
        self.margin_label.setFont(font1)
        self.margin_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.margin_label)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_7 = QLabel(self.tab_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_38.addWidget(self.label_7)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_40)

        self.margin_checkbox = QCheckBox(self.tab_4)
        self.margin_checkbox.setObjectName(u"margin_checkbox")
        self.margin_checkbox.setChecked(False)

        self.horizontalLayout_38.addWidget(self.margin_checkbox)

        self.label_8 = QLabel(self.tab_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_38.addWidget(self.label_8)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_38)

        self.widget_3 = QWidget(self.tab_4)
        self.widget_3.setObjectName(u"widget_3")

        self.horizontalLayout_9.addWidget(self.widget_3)

        self.line_64 = QFrame(self.tab_4)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setFrameShape(QFrame.Shape.VLine)
        self.line_64.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_64)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.line_2 = QFrame(self.tab_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line_62 = QFrame(self.tab_4)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.Shape.VLine)
        self.line_62.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_62)

        self.size_label = QLabel(self.tab_4)
        self.size_label.setObjectName(u"size_label")
        self.size_label.setFont(font1)
        self.size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.size_label)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.widget_5 = QWidget(self.tab_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.size_small_option = QRadioButton(self.widget_5)
        self.size_small_option.setObjectName(u"size_small_option")

        self.horizontalLayout_40.addWidget(self.size_small_option)

        self.size_medium_option = QRadioButton(self.widget_5)
        self.size_medium_option.setObjectName(u"size_medium_option")
        self.size_medium_option.setChecked(True)

        self.horizontalLayout_40.addWidget(self.size_medium_option)

        self.size_big_option = QRadioButton(self.widget_5)
        self.size_big_option.setObjectName(u"size_big_option")

        self.horizontalLayout_40.addWidget(self.size_big_option)


        self.horizontalLayout_31.addWidget(self.widget_5)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_31)

        self.widget_2 = QWidget(self.tab_4)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")

        self.horizontalLayout_7.addWidget(self.widget_2)

        self.line_59 = QFrame(self.tab_4)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setFrameShape(QFrame.Shape.VLine)
        self.line_59.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_59)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.line_61 = QFrame(self.tab_4)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.Shape.HLine)
        self.line_61.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_61)


        self.gridLayout_12.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_11.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.settings, 0, 0, 1, 1)

        self.input_preview = QGroupBox(self.scrollAreaWidgetContents_2)
        self.input_preview.setObjectName(u"input_preview")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(1)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.input_preview.sizePolicy().hasHeightForWidth())
        self.input_preview.setSizePolicy(sizePolicy10)
        self.input_preview.setMinimumSize(QSize(400, 600))
        self.verticalLayout_6 = QVBoxLayout(self.input_preview)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_9)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_12 = QLabel(self.input_preview)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_72.addWidget(self.label_12)

        self.default_color_selector = QComboBox(self.input_preview)
        self.default_color_selector.setObjectName(u"default_color_selector")

        self.horizontalLayout_72.addWidget(self.default_color_selector)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_30)

        self.default_color_preview = QLabel(self.input_preview)
        self.default_color_preview.setObjectName(u"default_color_preview")
        sizePolicy9.setHeightForWidth(self.default_color_preview.sizePolicy().hasHeightForWidth())
        self.default_color_preview.setSizePolicy(sizePolicy9)
        self.default_color_preview.setMinimumSize(QSize(200, 30))
        self.default_color_preview.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_73.addWidget(self.default_color_preview)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_41)


        self.horizontalLayout_72.addLayout(self.horizontalLayout_73)


        self.verticalLayout_6.addLayout(self.horizontalLayout_72)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.input = QTextEdit(self.input_preview)
        self.input.setObjectName(u"input")
        sizePolicy9.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy9)
        self.input.setMinimumSize(QSize(500, 75))
        self.input.setMaximumSize(QSize(400, 75))
        self.input.setStyleSheet(u"border: 2px solid white")

        self.horizontalLayout_45.addWidget(self.input)


        self.verticalLayout_6.addLayout(self.horizontalLayout_45)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_11 = QLabel(self.input_preview)
        self.label_11.setObjectName(u"label_11")
        sizePolicy9.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy9)
        font2 = QFont()
        font2.setPointSize(8)
        self.label_11.setFont(font2)
        self.label_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_11.setTextFormat(Qt.TextFormat.AutoText)

        self.horizontalLayout_71.addWidget(self.label_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_71)

        self.line_8 = QFrame(self.input_preview)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_8)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.output = QLabel(self.input_preview)
        self.output.setObjectName(u"output")
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setMinimumSize(QSize(289, 76))
        self.output.setMaximumSize(QSize(909, 270))
        self.output.setAutoFillBackground(True)
        self.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_56.addWidget(self.output)


        self.verticalLayout_6.addLayout(self.horizontalLayout_56)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

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


        self.gridLayout_7.addWidget(self.input_preview, 1, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_6.addWidget(self.scrollArea_4, 0, 0, 1, 1)

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
        self.universe_grid.setGeometry(QRect(0, 0, 984, 430))
        self.gridLayout_2 = QGridLayout(self.universe_grid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.scrollArea.setWidget(self.universe_grid)

        self.verticalLayout_10.addWidget(self.scrollArea)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)


        self.gridLayout_3.addWidget(self.existing, 1, 0, 1, 1)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.create_universe = QGroupBox(self.universes)
        self.create_universe.setObjectName(u"create_universe")
        sizePolicy9.setHeightForWidth(self.create_universe.sizePolicy().hasHeightForWidth())
        self.create_universe.setSizePolicy(sizePolicy9)
        self.create_universe.setMinimumSize(QSize(500, 226))
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

        self.universe_create_image_remove_button = QPushButton(self.create_universe)
        self.universe_create_image_remove_button.setObjectName(u"universe_create_image_remove_button")

        self.horizontalLayout_24.addWidget(self.universe_create_image_remove_button)

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
        sizePolicy9.setHeightForWidth(self.edit_universe.sizePolicy().hasHeightForWidth())
        self.edit_universe.setSizePolicy(sizePolicy9)
        self.edit_universe.setMinimumSize(QSize(500, 226))
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
        sizePolicy9.setHeightForWidth(self.universe_edit_image_button.sizePolicy().hasHeightForWidth())
        self.universe_edit_image_button.setSizePolicy(sizePolicy9)
        self.universe_edit_image_button.setMinimumSize(QSize(109, 0))
        self.universe_edit_image_button.setMaximumSize(QSize(109, 16777215))

        self.horizontalLayout_62.addWidget(self.universe_edit_image_button)

        self.universe_edit_image_remove_button = QPushButton(self.edit_universe)
        self.universe_edit_image_remove_button.setObjectName(u"universe_edit_image_remove_button")

        self.horizontalLayout_62.addWidget(self.universe_edit_image_remove_button)

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
        sizePolicy9.setHeightForWidth(self.create_character.sizePolicy().hasHeightForWidth())
        self.create_character.setSizePolicy(sizePolicy9)
        self.create_character.setMinimumSize(QSize(500, 335))
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

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.characters_create_font_label = QLabel(self.create_character)
        self.characters_create_font_label.setObjectName(u"characters_create_font_label")

        self.horizontalLayout_27.addWidget(self.characters_create_font_label)

        self.characters_create_font_selector = QComboBox(self.create_character)
        self.characters_create_font_selector.setObjectName(u"characters_create_font_selector")

        self.horizontalLayout_27.addWidget(self.characters_create_font_selector)


        self.verticalLayout_15.addLayout(self.horizontalLayout_27)

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

        self.characters_create_image_remove_button = QPushButton(self.create_character)
        self.characters_create_image_remove_button.setObjectName(u"characters_create_image_remove_button")

        self.horizontalLayout_28.addWidget(self.characters_create_image_remove_button)

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
        sizePolicy9.setHeightForWidth(self.edit_character.sizePolicy().hasHeightForWidth())
        self.edit_character.setSizePolicy(sizePolicy9)
        self.edit_character.setMinimumSize(QSize(500, 335))
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

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.characters_edit_font_label = QLabel(self.edit_character)
        self.characters_edit_font_label.setObjectName(u"characters_edit_font_label")

        self.horizontalLayout_29.addWidget(self.characters_edit_font_label)

        self.characters_edit_font_selector = QComboBox(self.edit_character)
        self.characters_edit_font_selector.setObjectName(u"characters_edit_font_selector")

        self.horizontalLayout_29.addWidget(self.characters_edit_font_selector)


        self.verticalLayout_39.addLayout(self.horizontalLayout_29)

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

        self.characters_edit_image_remove_button = QPushButton(self.edit_character)
        self.characters_edit_image_remove_button.setObjectName(u"characters_edit_image_remove_button")

        self.horizontalLayout_54.addWidget(self.characters_edit_image_remove_button)

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
        self.characters_grid.setGeometry(QRect(0, 0, 982, 319))
        self.gridLayout = QGridLayout(self.characters_grid)
        self.gridLayout.setObjectName(u"gridLayout")
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
        sizePolicy9.setHeightForWidth(self.create_expression.sizePolicy().hasHeightForWidth())
        self.create_expression.setSizePolicy(sizePolicy9)
        self.create_expression.setMinimumSize(QSize(500, 294))
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

        self.expressions_create_image_remove_button = QPushButton(self.create_expression)
        self.expressions_create_image_remove_button.setObjectName(u"expressions_create_image_remove_button")

        self.horizontalLayout_37.addWidget(self.expressions_create_image_remove_button)

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
        sizePolicy9.setHeightForWidth(self.edit_expression.sizePolicy().hasHeightForWidth())
        self.edit_expression.setSizePolicy(sizePolicy9)
        self.edit_expression.setMinimumSize(QSize(500, 294))
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

        self.expressions_edit_image_remove_button = QPushButton(self.edit_expression)
        self.expressions_edit_image_remove_button.setObjectName(u"expressions_edit_image_remove_button")

        self.horizontalLayout_67.addWidget(self.expressions_edit_image_remove_button)

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
        self.expressions_grid.setGeometry(QRect(0, 0, 984, 362))
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
        self.menubar.setGeometry(QRect(0, 0, 1080, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
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
        self.kofi.setText(QCoreApplication.translate("MainWindow", u"<a href='https://ko-fi.com/mirki__'>Support me on Kofi</a>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.welcome), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.settings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.border_style_label.setText(QCoreApplication.translate("MainWindow", u"Border Style", None))
        self.border_style_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.border_color_label.setText(QCoreApplication.translate("MainWindow", u"Border Color", None))
        self.border_color_preview.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Border Settings", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.label_10.setText("")
        self.include_checkbox.setText("")
        self.universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.universe_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.character_label.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.character_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expression_label.setText(QCoreApplication.translate("MainWindow", u"Expression", None))
        self.expression_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expression_color_label.setText(QCoreApplication.translate("MainWindow", u"Expression Color", None))
        self.expression_color_preview.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Sprite Settings (Left)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.label_17.setText("")
        self.include_checkbox_2.setText("")
        self.universe_label_2.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.universe_preview_2.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.character_label_2.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.character_preview_2.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expression_label_2.setText(QCoreApplication.translate("MainWindow", u"Expression", None))
        self.expression_preview_2.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expression_color_label_2.setText(QCoreApplication.translate("MainWindow", u"Expression Color", None))
        self.expression_color_preview_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Sprite Settings (Right)", None))
        self.font_label.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.asterisk_label.setText(QCoreApplication.translate("MainWindow", u"Asterisk", None))
        self.label.setText("")
        self.label_4.setText("")
        self.asterisk_checkbox.setText("")
        self.label_2.setText("")
        self.asterisk_color.setText(QCoreApplication.translate("MainWindow", u"Asterisk Color", None))
        self.asterisk_color_values.setText(QCoreApplication.translate("MainWindow", u"Values", None))
        self.asterisk_color_preview_1.setText("")
        self.asterisk_color_preview_2.setText("")
        self.asterisk_color_preview_3.setText("")
        self.text_style_label.setText(QCoreApplication.translate("MainWindow", u"Text Style", None))
        self.label_5.setText("")
        self.text_style_regular_option.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.label_3.setText("")
        self.text_style_dark_world_option.setText(QCoreApplication.translate("MainWindow", u"Dark World", None))
        self.text_transform_label.setText(QCoreApplication.translate("MainWindow", u"Text Transform", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Font Settings", None))
        self.format_label.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.format_png_option.setText(QCoreApplication.translate("MainWindow", u"PNG", None))
        self.label_6.setText("")
        self.format_gif_option.setText(QCoreApplication.translate("MainWindow", u"GIF", None))
        self.alternating_label.setText(QCoreApplication.translate("MainWindow", u"Alternating Expression (Left)", None))
        self.alternating_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.alternating_right_label.setText(QCoreApplication.translate("MainWindow", u"Alternating Expression (Right)", None))
        self.alternating_right_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.margin_label.setText(QCoreApplication.translate("MainWindow", u"Margin", None))
        self.label_7.setText("")
        self.margin_checkbox.setText("")
        self.label_8.setText("")
        self.size_label.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.size_small_option.setText(QCoreApplication.translate("MainWindow", u"Small", None))
        self.size_medium_option.setText(QCoreApplication.translate("MainWindow", u"Medium", None))
        self.size_big_option.setText(QCoreApplication.translate("MainWindow", u"Big", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Export Settings", None))
        self.input_preview.setTitle(QCoreApplication.translate("MainWindow", u"Input/Preview", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Default Text Color", None))
        self.default_color_preview.setText("")
        self.input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write your text here.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Hint: Use color=<color-name> in text to color the text to the right of the expression.", None))
        self.output.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"Download Textbox", None))
        self.tabs.setTabText(self.tabs.indexOf(self.generator), QCoreApplication.translate("MainWindow", u"Generator", None))
        self.existing.setTitle(QCoreApplication.translate("MainWindow", u"Existing", None))
        self.universe_filter_label.setText(QCoreApplication.translate("MainWindow", u"Filter by name", None))
        self.create_universe.setTitle(QCoreApplication.translate("MainWindow", u"Create a new Universe", None))
        self.universe_create_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.universe_create_preview_label.setText(QCoreApplication.translate("MainWindow", u"Preview image (optional)", None))
        self.universe_create_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.universe_create_image_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.universe_create_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.universe_create_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.edit_universe.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.universe_edit_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.universe_edit_preview_label.setText(QCoreApplication.translate("MainWindow", u"Preview image", None))
        self.universe_edit_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.universe_edit_image_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.universe_edit_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.universe_edit_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabs.setTabText(self.tabs.indexOf(self.universes), QCoreApplication.translate("MainWindow", u"Universes", None))
        self.create_character.setTitle(QCoreApplication.translate("MainWindow", u"Create a new Character", None))
        self.characters_create_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.characters_create_universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.characters_create_style_label.setText(QCoreApplication.translate("MainWindow", u"Default Style", None))
        self.characters_create_style_regular_option.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.characters_create_style_dark_world_option.setText(QCoreApplication.translate("MainWindow", u"Dark World", None))
        self.characters_create_font_label.setText(QCoreApplication.translate("MainWindow", u"Default Font", None))
        self.characters_create_transform_label.setText(QCoreApplication.translate("MainWindow", u"Default Text Transform", None))
        self.characters_create_preview_label.setText(QCoreApplication.translate("MainWindow", u"Preview image (optional)", None))
        self.characters_create_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.characters_create_image_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.characters_create_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.characters_create_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.edit_character.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.characters_edit_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.characters_edit_universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.characters_edit_style_label.setText(QCoreApplication.translate("MainWindow", u"Default Style", None))
        self.characters_edit_style_regular_option.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.characters_edit_style_dark_world_option.setText(QCoreApplication.translate("MainWindow", u"Dark World", None))
        self.characters_edit_font_label.setText(QCoreApplication.translate("MainWindow", u"Default Font", None))
        self.characters_edit_transform_label.setText(QCoreApplication.translate("MainWindow", u"Default Text Transform", None))
        self.characters_edit_preview_label.setText(QCoreApplication.translate("MainWindow", u"Preview image (optional)", None))
        self.characters_edit_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.characters_edit_image_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.characters_edit_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.characters_edit_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Existing", None))
        self.characters_filter_label.setText(QCoreApplication.translate("MainWindow", u"Filter by name", None))
        self.tabs.setTabText(self.tabs.indexOf(self.characters), QCoreApplication.translate("MainWindow", u"Characters", None))
        self.create_expression.setTitle(QCoreApplication.translate("MainWindow", u"Create a new expression", None))
        self.expressions_create_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.expressions_create_universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.expressions_create_character_label.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.expressions_create_preview_label.setText(QCoreApplication.translate("MainWindow", u"Image (required)", None))
        self.expressions_create_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.expressions_create_image_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.expressions_create_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expressions_create_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.edit_expression.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.expressions_edit_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.expressions_edit_universe_label.setText(QCoreApplication.translate("MainWindow", u"Universe", None))
        self.expressions_edit_character_label.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.expressions_edit_preview_label.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.expressions_edit_image_button.setText(QCoreApplication.translate("MainWindow", u"Select image", None))
        self.expressions_edit_image_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.expressions_edit_image_preview.setText(QCoreApplication.translate("MainWindow", u"Nothing...", None))
        self.expressions_edit_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Existing", None))
        self.expressions_filter_label.setText(QCoreApplication.translate("MainWindow", u"Filter by name", None))
        self.tabs.setTabText(self.tabs.indexOf(self.expressions), QCoreApplication.translate("MainWindow", u"Expressions", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

