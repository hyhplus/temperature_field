#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys


class CustWidget(QWidget):

    def __init__(self, parent=None):
        super(CustWidget, self).__init__(parent)

        self.okButton = QPushButton("Ok", self)

        # 使用setObjectName设置对象名称
        self.okButton.setObjectName("okButton")

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)

        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSignal
    def okButton_clicked(self):
        print("单击了OK按钮")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CustWidget()
    win.show()
    app.exec_()





