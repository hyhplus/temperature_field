#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
测试颜色是否正确显示

"""
import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication

from MyColor import temp_to_color
from TemperatureChange import Temperature


class ColorTest(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        t = Temperature(68, 1, 25, 100, -50)
        color_rgb = t.color_change()
        a, b, c = color_rgb[0], color_rgb[1], color_rgb[2]
        col = QColor(a, b, c)

        t2 = Temperature(79, 2, 25, 100, -50)
        color_rgb = t2.color_change()
        a, b, c = color_rgb[0], color_rgb[1], color_rgb[2]
        col_2 = QColor(a, b, c)

        t3 = Temperature(100, 3, 25, 100, -50)
        color_rgb = t3.color_change()
        a, b, c = color_rgb[0], color_rgb[1], color_rgb[2]
        col_3 = QColor(a, b, c)

        color_rgb = temp_to_color(90, 25, 100, -50)
        a, b, c = color_rgb[0], color_rgb[1], color_rgb[2]
        col_4 = QColor(a, b, c)

        self.btn = QPushButton("改变颜色", self)    # 转换颜色按钮
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.show_color)

        # 显示颜色的QFrame背景框
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % (col.name()))
        self.frm.setGeometry(130, 22, 100, 100)

        # 显示颜色的QFrame背景框
        self.frm_2 = QFrame(self)
        self.frm_2.setStyleSheet("QWidget { background-color: %s }" % (col_2.name()))
        self.frm_2.setGeometry(130, 122, 100, 100)

        # 显示颜色的QFrame背景框
        self.frm_3 = QFrame(self)
        self.frm_3.setStyleSheet("QWidget { background-color: %s }" % (col_3.name()))
        self.frm_3.setGeometry(230, 22, 100, 100)

        # 显示颜色的QFrame背景框
        self.frm_4 = QFrame(self)
        self.frm_4.setStyleSheet("QWidget { background-color: %s }" % (col_4.name()))
        self.frm_4.setGeometry(230, 122, 100, 100)

        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle("RGB转颜色")
        self.show()

    def show_color(self):
        col = QColorDialog.getColor()   # 弹出一个QColorDialog对话框

        # 我们可以预览颜色，如果点击取消按钮，没有颜色值返回，
        # 如果颜色是我们想要的，就从取色框里选择这个颜色
        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % (col.name()))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ColorTest()
    sys.exit(app.exec_())
