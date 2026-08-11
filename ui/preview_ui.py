# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entity_previewVZxWWa.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QScrollArea,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(860, 802)
        Dialog.setMinimumSize(QSize(500, 400))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.entity_grid = QWidget()
        self.entity_grid.setObjectName(u"entity_grid")
        self.entity_grid.setGeometry(QRect(0, 0, 840, 739))
        self.gridLayout_2 = QGridLayout(self.entity_grid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea.setWidget(self.entity_grid)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.filter_name = QLabel(Dialog)
        self.filter_name.setObjectName(u"filter_name")

        self.horizontalLayout_2.addWidget(self.filter_name)

        self.filter_name_input = QLineEdit(Dialog)
        self.filter_name_input.setObjectName(u"filter_name_input")

        self.horizontalLayout_2.addWidget(self.filter_name_input)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.filter_name.setText(QCoreApplication.translate("Dialog", u"Filter by name", None))
    # retranslateUi

