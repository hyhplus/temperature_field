#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyQt5 Animation tutorial

This program animates the size of a
widget with QPropertyAnimation.

Author: Seshigure 401219180@qq.com
Last edited: 2018.03.02
"""

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Start", self)
        self.button.clicked.connect(self.doAnim)
        self.button.move(30, 30)

        self.label = QLabel("changeSize", self)
        self.label.setAutoFillBackground(True)  # 必写,不然调色板不能填充背景
        self.palette = QPalette()  # 创建一个调色板进行背景填充方便看label大小
        self.palette.setColor(self.label.backgroundRole(), QColor(255, 50, 50, 50))
        self.label.setPalette(self.palette)
        self.label.setGeometry(150, 30, 100, 100)

        self.setGeometry(300, 300, 380, 300)
        self.setWindowTitle('Animation')
        self.show()

    def doAnim(self):
        self.anim = QPropertyAnimation(self.label, b"geometry")
        self.anim.setDuration(3000)
        self.anim.setStartValue(QRect(150, 30, 100, 100))  # 大小100*100
        self.anim.setEndValue(QRect(150, 30, 200, 200))    # 大小200*200
        self.anim.start()


if __name__ == "__main__":
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exec_()
