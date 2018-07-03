from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .playerinfo_dialog import Ui_playerinfo_dialog


class playerinfo(QDialog, Ui_playerinfo_dialog):
    def __init__(self):
        super(playerinfo, self).__init__()
        self.setupUi(self)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(
            QPixmap('pic/gui/reg_fgt_info.png').scaled(self.size())))  # 设置背景图片
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.pushButton_ok.clicked.connect(self.SHUTDOWN)
        self.screen_center()

    def screen_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def SHUTDOWN(self):
        self.close()

    def OPEN(self):
        self.show()

    def get_gamename(self):
        print(self.lineEdit_gamename.text())

    def set_gamename(self, TEXT):
        self.lineEdit_gamename.setText(
            QCoreApplication.translate("playerinfo_dialog", TEXT))

    def show_winpercent(self, percent):
        self.label_show_winpercent.setText(
            QCoreApplication.translate("playerinfo_dialog", percent))

    def show_lcdnumbs(self, totalgts, dizhugts):
        self.lcdNumber_total_gametimes.display(totalgts)
        self.lcdNumber_dizhu_gametimes.display(dizhugts)
