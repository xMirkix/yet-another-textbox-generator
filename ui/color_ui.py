# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_configurationNTxNSP.ui'
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
    QGridLayout, QHBoxLayout, QPushButton, QScrollArea,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(531, 392)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_all = QPushButton(Dialog)
        self.select_all.setObjectName(u"select_all")

        self.horizontalLayout_2.addWidget(self.select_all)

        self.invert_selection = QPushButton(Dialog)
        self.invert_selection.setObjectName(u"invert_selection")

        self.horizontalLayout_2.addWidget(self.invert_selection)

        self.simple_recoloring = QCheckBox(Dialog)
        self.simple_recoloring.setObjectName(u"simple_recoloring")
        self.simple_recoloring.setChecked(True)

        self.horizontalLayout_2.addWidget(self.simple_recoloring)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 511, 295))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ok_button = QPushButton(Dialog)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout.addWidget(self.ok_button)

        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.select_all.setText(QCoreApplication.translate("Dialog", u"Select All", None))
        self.invert_selection.setText(QCoreApplication.translate("Dialog", u"Invert Selection", None))
#if QT_CONFIG(tooltip)
        self.simple_recoloring.setToolTip(QCoreApplication.translate("Dialog", u"Controls whether the original color should be considered. Turn off for gradients or colorful Darkners.", None))
#endif // QT_CONFIG(tooltip)
        self.simple_recoloring.setText(QCoreApplication.translate("Dialog", u"Replace existing color", None))
        self.ok_button.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

