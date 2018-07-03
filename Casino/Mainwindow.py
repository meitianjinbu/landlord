# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.resize(800, 400)
        Mainwindow.setMinimumSize(QtCore.QSize(800, 400))
        Mainwindow.setMaximumSize(QtCore.QSize(800, 400))
        self.Button_quickgame = QtWidgets.QPushButton(Mainwindow)
        # self.Button_quickgame.setGeometry(QtCore.QRect(50, 160, 200, 100))
        # self.Button_quickgame.setGeometry(QtCore.QRect(550, 160, 200, 100))
        self.Button_quickgame.setGeometry(QtCore.QRect(320, 235, 200, 100))
        self.Button_quickgame.setIconSize(self.Button_quickgame.size())
        self.Button_quickgame.setIcon(QtGui.QIcon("pic/gui/game_start2.png"))
        self.Button_quickgame.setStyleSheet("background: transparent;border: none;")
        # font = QtGui.QFont()
        # font.setPointSize(30)
        # self.Button_quickgame.setFont(font)
        self.Button_quickgame.setObjectName("Button_quickgame")

        # self.Button_firendsgame = QtWidgets.QPushButton(Mainwindow)
        # self.Button_firendsgame.setGeometry(QtCore.QRect(300, 160, 200, 100))
        # font = QtGui.QFont()
        # font.setPointSize(30)
        # self.Button_firendsgame.setFont(font)
        # self.Button_firendsgame.setObjectName("Button_firendsgame")
        self.frame = QtWidgets.QFrame(Mainwindow)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 802, 60))
        # self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Button_playerinfo = QtWidgets.QPushButton(self.frame)
        self.Button_playerinfo.setGeometry(QtCore.QRect(15, 12, 45, 45))
        self.Button_playerinfo.setObjectName("Button_playerinfo")
        self.Button_playerinfo.setIconSize(self.Button_playerinfo.size())
        self.Button_playerinfo.setIcon(QtGui.QIcon("pic/gui/info.png"))
        self.Button_playerinfo.setStyleSheet("background: transparent;")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(75, 12, 68, 45))
        self.label.setMouseTracking(False)
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.friends = QtWidgets.QTabWidget(Mainwindow)
        # self.friends.setStyleSheet("QTabWidget:pane{border: 1px solid blue;}")
        self.friends.setGeometry(QtCore.QRect(15, 70, 200, 306))
        self.friends.setMinimumSize(QtCore.QSize(200, 200))
        self.friends.setMaximumSize(QtCore.QSize(300, 16777215))
        self.friends.setObjectName("friends")
        self.friends_info = QtWidgets.QWidget()
        self.friends_info.setObjectName("friends_info")
        self.listWidget = QtWidgets.QListWidget(self.friends_info)
        # self.listWidget.setFrameShape(QtWidgets.QListWidget.NoFrame)
        self.listWidget.setStyleSheet("background-color:rgba(250,255,255,0.6)")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # 隐藏垂直滚动条
        self.listWidget.setGeometry(QtCore.QRect(-2, -1, 200, 280))
        self.listWidget.setObjectName("listWidget")
        self.friends.addTab(self.friends_info, "")
        self.friends_request = QtWidgets.QWidget()
        self.friends_request.setObjectName("friends_request")
        self.listWidget_2 = QtWidgets.QListWidget(self.friends_request)
        # self.listWidget_2.setFrameShape(QtWidgets.QListWidget.NoFrame)
        self.listWidget_2.setStyleSheet("background-color:rgba(250,255,255,0.6)")
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # 隐藏垂直滚动条
        self.listWidget_2.setGeometry(QtCore.QRect(-2, -1, 200, 280))
        self.listWidget_2.setObjectName("listWidget_2")
        self.friends.addTab(self.friends_request, "")
        # self.tab = QtWidgets.QWidget()
        # self.tab.setObjectName("tab")
        # self.listWidget_3 = QtWidgets.QListWidget(self.tab)
        # self.listWidget_3.setGeometry(QtCore.QRect(-2, -1, 249, 315))
        # self.listWidget_3.setObjectName("listWidget_3")
        # self.friends.addTab(self.tab, "")

        self.retranslateUi(Mainwindow)
        self.friends.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "斗地主"))
        # self.Button_quickgame.setText(_translate("Mainwindow", "快速游戏"))
        # self.Button_firendsgame.setText(_translate("Mainwindow", "邀请好友"))
        # self.Button_playerinfo.setText(_translate("Mainwindow", "个人信息"))
        # self.label.setText(_translate("Mainwindow", "coin:xxx"))
        self.friends.setTabText(self.friends.indexOf(self.friends_info), _translate("Mainwindow", "积分排行榜"))
        self.friends.setTabText(self.friends.indexOf(self.friends_request), _translate("Mainwindow", "胜率排行榜"))
        # self.friends.setTabText(self.friends.indexOf(self.tab), _translate("Mainwindow", "消息(10)"))
