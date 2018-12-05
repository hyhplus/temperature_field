#!/usr/bin/python3
# -*- coding: utf-8 -*-
import binascii
import logging
import re
import sys
import threading
import time

import serial
import serial.tools.list_ports
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

import DataToMySQL
from Pyserial.COM_Connect import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        """ 初始化 """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.create_serial()

        self.port_check()
        self.pushButton.clicked.connect(self.port_open)
        self.pushButton_2.clicked.connect(self.port_close)

        self.serial_thread = "init-thread"
        self.threadFlag = False
        self.alive = False
        self.read_data = b""

        self.pushButton_3.clicked.connect(self.write_data)
        self.d_data = ""
        self.create_items()

        self.timer = ""
        self.c = True

        self.port_list_new = list(serial.tools.list_ports.comports())
        self.port_c = self.port_list_new     # 启动时检测

    @classmethod
    def create_serial(cls):
        """ 创建并实例化串口 """
        cls.my_serial = serial.Serial()
        # cls.set_data = DataToMySQL.save_data("", "set", count=2)
        # print(cls.set_data)

    def port_check_timer(self):
        """ 实时检测串口 """
        port_list = list(serial.tools.list_ports.comports())
        com_list = []
        for port in port_list:
            com_list.append(port[0])

        if self.port_list_new > port_list:
            QMessageBox.warning(self, "warning", "有串口拔出")
            if self.my_serial.isOpen():
                if self.comboBox.currentText() not in com_list:
                    self.port_close()

            self.port_check()

        if self.port_list_new < port_list:
            self.port_list_new = port_list
            QMessageBox.about(self, "new serial", "有串口接入")

            # if not self.my_serial.isOpen():
            self.port_check()

            # if self.my_serial.isOpen():
            #     self.port_check()

        self.port_c = port_list

        if not self.port_c:         # 仅限启动程序识别串口时调用
            self.port_c = [""]
            QMessageBox.warning(self, "warning", "无串口")

    def port_check(self):
        """ 检测串口，自动识别 """
        com_list = []
        port_list = list(serial.tools.list_ports.comports())

        for port in port_list:
            com_list.append(port[0])

        temp = self.comboBox.currentText()
        if self.my_serial.isOpen() and temp in com_list and self.port_list_new < port_list:
            pass
        else:
            self.comboBox.clear()

            for i in com_list:
                self.comboBox.addItem(i)
                self.pushButton.setText("connect")

            if len(com_list) == 0:
                pass
                # self.pushButton.setText("no serial")
                # QMessageBox.warning(self, "warning", "请检测串口是否正确插入")
            else:
                self.pushButton.setText("connect")

        self.port_list_new = port_list

    def port_open(self):
        """ 打开串口 """
        port_list = list(serial.tools.list_ports.comports())
        com_list = []
        for port in port_list:
            com_list.append(port[0])

        if self.comboBox.currentText() == "":
            self.port_check()
            if self.comboBox.currentText() == "":
                QMessageBox.warning(self, "warning", "请检测串口是否正确插入")

        elif self.comboBox.currentText() in com_list:
            self.my_serial.port = self.comboBox.currentText()
            self.my_serial.baudrate = int(self.comboBox_2.currentText())

            self.my_serial.open()
            if self.my_serial.isOpen():
                self.alive = True
                self.comboBox.setEnabled(False)
                self.comboBox_2.setEnabled(False)
                self.pushButton.setEnabled(False)
                self.pushButton_2.setEnabled(True)

                # self.write_data(self.text_edit_data(), is_hex=False)
                # self.write_data(self.text_edit_data, is_hex=False)  # data="FA 01 A0 01 D8 FC"

        else:
            QMessageBox.warning(self, "warning", "请检测串口是否正确插入")

    def port_close(self):
        """ 关闭串口 """
        self.port_check()
        self.alive = False
        if self.my_serial.isOpen():
            self.my_serial.close()
            self.comboBox.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)

    def write_data(self, is_hex=False):
        """ 写数据到串口 """
        data_ = self.textEdit.toPlainText()
        data = bytearray.fromhex(data_)              # 16进制字符串转为字节数组
        print(data)
        if self.alive:
            if self.my_serial.isOpen():
                if is_hex:
                    data = binascii.unhexlify(data)
                    print(data)
            self.my_serial.write(data)
            print(data)

        # 开启接收数据线程
        self.serial_thread = threading.Thread(target=self.receive_data)
        self.serial_thread.setDaemon(True)
        self.serial_thread.start()

    def receive_data(self):
        """ 串口接收数据，并输出到接收区 """
        self.threadFlag = True
        print("receive data threading is start")
        num = 0
        print(self.alive)
        while self.alive:
            try:
                size = self.my_serial.inWaiting()
                # rec_data = ''
                # rec_data = rec_data.encode("utf-8")
                # print(type(size))

                if size:
                    # self.my_serial.read(size).replace(binascii.unhexlify("00"), "")
                    self.read_data += self.my_serial.read(size)
                    # print(self.read_data)
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

    def create_items(self):
        """ 开启定时器 """
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.timeout.connect(self.port_check_timer)
        self.timer.start(100)

        # self.timer_port = QTimer(self)
        # self.timer_port.timeout.connect(self.set_c)
        # self.timer_port.start(2000)

    def show_time(self):
        """ 显示时间 """
        self.label_6.setText(time.strftime("%Y %m %d, %H:%M:%S", time.localtime()))

    def set_c(self):
        self.c = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    # ui.write_data("other write", is_hex=False)
    ui.show()

    sys.exit(app.exec_())


