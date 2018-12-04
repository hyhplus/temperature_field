#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
PyQt5 Animation tutorial

This program animates the color of a
widget with QPropertyAnimation.

备注：
1、label没有color动画属性，所以我们得重写label
2、self.anim.setKeyValueAt(0.5, QColor(255, 0, 0, 250))
这里使用了一个关键帧，让动画完成 粉色>红色>米黄的颜色转换

"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyLabel(QLabel):
    def __init__(self, text, para):
        super().__init__(text, para)

    def _set_color(self, col):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), col)
        self.setPalette(palette)

    color = pyqtProperty(QColor, fset=_set_color)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Start", self)
        self.button.clicked.connect(self.doAnim)
        self.button.move(30, 30)

        self.label = MyLabel(" ", self)
        self.label._set_color(QColor(255, 50, 50, 50))
        self.label.setGeometry(150, 30, 200, 130)

        self.setGeometry(300, 300, 380, 300)
        self.setWindowTitle('Animation')
        self.show()

    def doAnim(self):
        self.anim = QPropertyAnimation(self.label, b"color")
        self.anim.setDuration(3000)
        self.anim.setStartValue(QColor(255, 50, 50, 50))      # 粉色
        self.anim.setKeyValueAt(0.5, QColor(255, 0, 0, 250))  # 红色
        self.anim.setEndValue(QColor(255, 250, 50, 50))       # 米黄
        self.anim.start()


if __name__ == "__main__":
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exec_()
