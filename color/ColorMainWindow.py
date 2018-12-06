#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFrame

from ColorWindow import Ui_color_temp
from MyColor import temp_to_color


class ColorMain(QWidget, Ui_color_temp):
    def __init__(self):
        super(ColorMain, self).__init__()
        self.setupUi(self)
        self.change_color()
        self.frm = ""

    def change_color(self):
        color_rgb = temp_to_color(90, 25, 100, -50)
        a, b, c = color_rgb[0], color_rgb[1], color_rgb[2]
        col = QColor(a, b, c)

        # 显示颜色的QFrame背景框
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % (col.name()))
        self.frm.setGeometry(80, 40, 1, 1)

        # self.widget = QWidget(self)
        # self.widget.setGeometry(QtCore.QRect(80, 40, 681, 241))
        self.widget.setStyleSheet(
            # "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
            # "stop:0 rgba(255, 118, 0, 255), stop:1 rgba(208, 222, 255, 255));")
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
            "stop:0 rgba(185, 202, 255, 255), stop:1 rgba(255, 157, 63, 255));")
        # self.widget.setObjectName("widget")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ColorMain()
    # ui.change_color()
    ui.show()
    sys.exit(app.exec_())


