# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ColorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor


class Ui_color_temp(object):
    def setupUi(self, color_temp):
        color_temp.setObjectName("color_temp")
        color_temp.resize(829, 574)
        color_temp.setToolTip("")
        self.widget = QtWidgets.QWidget(color_temp)
        self.widget.setGeometry(QtCore.QRect(80, 40, 681, 241))
        # self.widget.setStyleSheet("background-color:
        # qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
        # stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")

        # self.widget.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.widget.setObjectName("widget")

        self.retranslateUi(color_temp)
        QtCore.QMetaObject.connectSlotsByName(color_temp)

    def retranslateUi(self, color_temp):
        _translate = QtCore.QCoreApplication.translate
        color_temp.setWindowTitle(_translate("color_temp", "color_temp"))

