#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtSignal


class SignalClass(QObject):
    # 声明无参数的信号1
    signal1 = pyqtSignal()

    # 声明有参数的信号2
    signal2 = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super(SignalClass, self).__init__(parent)

        self.signal1.connect(self.sin1_call)
        self.signal1.connect(self.sin2_call)

        self.signal2.connect(self.signal1)

        # 发射信号
        self.signal1.emit()
        self.signal2.emit(1, "abc")

        print("-- --- --- --")

        # 断开信号与槽函数的连接
        self.signal1.disconnect(self.sin1_call)
        self.signal1.disconnect(self.sin2_call)
        self.signal2.disconnect(self.signal1)

        self.signal1.connect(self.sin1_call)
        self.signal2.connect(self.sin1_call)

        self.signal1.emit()
        self.signal2.emit(6, "实参")

    @staticmethod
    def sin1_call():
        print("signal-1 emit")

    @staticmethod
    def sin2_call():
        print("signal-2 emit")


if __name__ == "__main__":
    signal = SignalClass()



