from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .Mainwindow import Ui_Mainwindow


class mainwindow(QWidget, Ui_Mainwindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(
            QPixmap('pic/gui/hall3.jpg').scaled(self.size())))  # 设置背景图片
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.screen_center()

    def screen_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def show_coins(self, numb):
        _translate = QCoreApplication.translate
        _TEXT = '积分: ' + numb
        self.label.setText(_translate("Mainwindow", _TEXT))
        self.label.setStyleSheet("background-color:rgba(250,255,255,0.3);")

    def friend_list(self, friends):
        lst = []
        for fr in friends.values():
            try:
                if fr[6]:
                    fr_info = fr[0] + ('(在线)')
            except IndexError:
                fr_info = fr[0] + ('(离线)')
            lst.append(fr_info)
        self.listWidget.addItems(lst)

    def rank_list(self, scores, win_rates):
        '''scores和win_rates是两个元组'''
        # lst_score = [('  {}\n  积分:{:d}'.format(*x)) for x in scores]
        # lst_wrate = [('  {}\n  胜率:{:.0f}%'.format(*x)) for x in win_rates]
        # self.listWidget.addItems(lst_score)
        # self.listWidget_2.addItems(lst_wrate)
        self.listWidget.clear()
        self.listWidget_2.clear()
        for i in scores:
            self.listWidget.setIconSize(QSize(29,40))
            item = QListWidgetItem(QIcon("pic/gui/touxiang.png"),
                                   self.tr('  {}\n  积分:{:d}'.format(*i)), self.listWidget)
        for j in win_rates:
            self.listWidget_2.setIconSize(QSize(29,40))
            item = QListWidgetItem(QIcon("pic/gui/touxiang.png"),
                                   self.tr('  {}\n  胜率:{:.0f}%'.format(*j)), self.listWidget_2)
