# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(600, 300)
        Login.setMinimumSize(QtCore.QSize(600, 300))
        Login.setMaximumSize(QtCore.QSize(600, 300))
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(30, 30, 530, 230))
        self.widget.setObjectName("widget")
        self.Button_login = QtWidgets.QPushButton(self.widget)
        self.Button_login.setGeometry(QtCore.QRect(220, 140, 150, 40))
        self.Button_login.setMinimumSize(QtCore.QSize(150, 40))
        self.Button_login.setMaximumSize(QtCore.QSize(400, 50))
        self.Button_login.setObjectName("Button_login")
        self.Button_forgot = QtWidgets.QPushButton(self.widget)
        self.Button_forgot.setGeometry(QtCore.QRect(310, 180, 100, 35))
        self.Button_forgot.setMinimumSize(QtCore.QSize(0, 35))
        self.Button_forgot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Button_forgot.setObjectName("Button_forgot")
        self.Button_register = QtWidgets.QPushButton(self.widget)
        self.Button_register.setGeometry(QtCore.QRect(180, 180, 100, 35))
        self.Button_register.setMinimumSize(QtCore.QSize(0, 35))
        self.Button_register.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Button_register.setObjectName("Button_register")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 40, 353, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_account = QtWidgets.QLabel(self.layoutWidget)
        self.label_account.setMinimumSize(QtCore.QSize(45, 30))
        self.label_account.setMaximumSize(QtCore.QSize(45, 30))
        self.label_account.setObjectName("label_account")
        self.label_account.setStyleSheet("color: white;")
        self.horizontalLayout.addWidget(self.label_account)
        self.lineEdit_account = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_account.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_account.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.horizontalLayout.addWidget(self.lineEdit_account)
        self.layoutWidget1 = QtWidgets.QWidget(self.widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 90, 353, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_password = QtWidgets.QLabel(self.layoutWidget1)
        self.label_password.setMinimumSize(QtCore.QSize(45, 30))
        self.label_password.setMaximumSize(QtCore.QSize(45, 30))
        self.label_password.setObjectName("label_password")
        self.label_password.setStyleSheet("color: white;")
        self.horizontalLayout_2.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.register_tips_label = QtWidgets.QLabel(Login)
        self.register_tips_label.setGeometry(QtCore.QRect(230, 40, 175, 16))
        self.register_tips_label.setObjectName("register_tips_label")
        self.register_tips_label.setStyleSheet("color: red;")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录"))
        self.Button_login.setText(_translate("Login", "登录"))
        self.Button_forgot.setText(_translate("Login", "找回密码"))
        self.Button_register.setText(_translate("Login", "注册"))
        self.label_account.setText(_translate("Login", "用户名"))
        self.label_password.setText(_translate("Login", "密    码"))

