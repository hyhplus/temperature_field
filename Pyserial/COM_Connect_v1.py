# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'COM_Connect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 346)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(130, 70, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 130, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 70, 54, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(130, 190, 54, 12))
        self.label_4.setObjectName("label_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 210, 231, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 280, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(400, 190, 54, 12))
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(310, 210, 231, 61))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "COM connect"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "19200"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "38400"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "115200"))
        self.pushButton.setText(_translate("Form", "connect"))
        self.pushButton_2.setText(_translate("Form", "close"))
        self.label.setText(_translate("Form", "串口"))
        self.label_2.setText(_translate("Form", "波特率"))
        self.label_4.setText(_translate("Form", "发送数据"))
        self.pushButton_3.setText(_translate("Form", "send"))
        self.label_5.setText(_translate("Form", "接收数据"))

