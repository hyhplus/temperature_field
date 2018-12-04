#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyQt5 Animation tutorial
This program will show along curve with QPropertyAnimation.
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Ball(QLabel):
    def __init__(self, parent):
        super(Ball, self).__init__(parent)

        self.pix = QPixmap("../ball.png")  # 加载一个ball的图片
        self.h = self.pix.height()  # ball的高度
        self.w = self.pix.width()  # ball的宽度

        self.setPixmap(self.pix)  # 把ball加载到label上

    def _set_pos(self, pos):
        self.move(pos.x() - self.w / 2, pos.y() - self.h / 2)

    pos = pyqtProperty(QPointF, fset=_set_pos)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initView()
        self.initAnimation()

    def initView(self):
        self.path = QPainterPath()
        self.path.moveTo(30, 30)
        self.path.cubicTo(30, 30, 200, 350, 350, 30)  # 设置弧线的样子

        self.ball = Ball(self)
        self.ball.pos = QPointF(30, 30)  # 设置ball起点位置,这里就是弧线的起点位置

        self.setWindowTitle("Animation along curve")
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.drawPath(self.path)  # 画弧线
        qp.end()

    def initAnimation(self):
        self.anim = QPropertyAnimation(self.ball, b'pos')
        self.anim.setDuration(3000)
        self.anim.setStartValue(QPointF(30, 30))

        vals = [p / 100 for p in range(0, 101)]

        for i in vals:
            self.anim.setKeyValueAt(i, self.path.pointAtPercent(i))  # 设置100个关键帧

        self.anim.setEndValue(QPointF(350, 30))
        self.anim.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
