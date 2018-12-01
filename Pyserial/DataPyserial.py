#!/usr/bin/python3
# -*- coding: utf-8 -*-
import binascii
import logging
import re
import sys
import threading

import serial
import serial.tools.list_ports
from PyQt5 import QtGui

from PyQt5.QtWidgets import QMainWindow, QApplication

import DataToMySQL
from Pyserial.COM_Connect import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):                # 初始化
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.create_serial()
        self.port_check()
        self.pushButton.clicked.connect(self.port_open)
        self.pushButton_2.clicked.connect(self.port_close)

        self.serial_thread = "init_thread"
        self.threadFlag = False
        self.alive = False
        self.read_data = b""

    @classmethod
    def create_serial(cls):                         # 创建并实例化串口
        cls.my_serial = serial.Serial()
        cls.set_data = DataToMySQL.save_data("", "set", count=2)
        print(cls.set_data)

    def port_check(self):                           # 检测串口，自动识别
        com_list = []
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox.clear()
        for port in port_list:
            com_list.append(port[0])
            self.comboBox.addItem(port[0])

        if len(com_list) == 0:
            pass

    def port_open(self):                            # 打开串口
        if self.comboBox.currentText() == "":
            self.port_check()

        else:
            self.my_serial.port = self.comboBox.currentText()
            self.my_serial.baudrate = int(self.comboBox_2.currentText())

            self.my_serial.open()
            if self.my_serial.isOpen():
                self.alive = True
                self.comboBox.setEnabled(False)
                self.comboBox_2.setEnabled(False)
                self.pushButton.setEnabled(False)
                self.pushButton_2.setEnabled(True)

                self.write_data(self.set_data, is_hex=False)  # data="FA 01 A0 01 D8 FC"

                # 开启接收数据线程
                self.serial_thread = threading.Thread(target=self.receive_data)
                self.serial_thread.setDaemon(True)
                self.serial_thread.start()

    def port_close(self):                           # 关闭串口
        self.alive = False
        if self.my_serial.isOpen():
            self.my_serial.close()
            self.comboBox.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)

    def write_data(self, data, is_hex=False):       # 写数据到串口
        data = bytearray.fromhex(data)              # 16进制字符串转为字节数组
        if self.alive:
            if self.my_serial.isOpen():
                if is_hex:
                    data = binascii.unhexlify(data)
                    print(data)
            self.my_serial.write(data)
            print(data)

    def receive_data(self):                         # 串口接收数据，并输出到接收区
        self.threadFlag = True
        print("receive data threading is start")
        num = 0
        while self.alive:
            try:
                size = self.my_serial.inWaiting()
                # rec_data = ''
                # rec_data = rec_data.encode("utf-8")
                # print(size)
                # print(type(size))

                if size:
                    # self.my_serial.read(size).replace(binascii.unhexlify("00"), "")
                    self.read_data += self.my_serial.read(size)
                    print(self.read_data)
                    # print(type(rec_data))

                    data = str(binascii.b2a_hex(self.read_data))[2:-1].upper()

                    print(data)
                    p = re.compile('.{1,2}')
                    data = " ".join(p.findall(data))
                    print(type(data))

                    # 把数据保存到数据库中
                    DataToMySQL.save_data(data, "save", count=0)

                    # data = self.read_data
                    self.textBrowser.append(data)
                    self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                    self.my_serial.flushInput()

                    num += 1
            except Exception as e:
                logging.error(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    # ui.write_data("other write", is_hex=False)
    ui.show()
    sys.exit(app.exec_())


