#


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .UI_Mainwindow import mainwindow
from .UI_login import login
from .UI_register import register
from .UI_playerinfo_dialog import playerinfo
from .UI_reset_passwd import reset_password
from .Ui_room import room
from .Ui_video import Video
import sys


class UIreset_password(reset_password):
    def __init__(self):
        super(UIreset_password, self).__init__()


class UIplayerinfo(playerinfo):
    def __init__(self):
        super(UIplayerinfo, self).__init__()


class UImainwindow(mainwindow):
    signal_msg = pyqtSignal(str)
    signal_video = pyqtSignal(str)
    def __init__(self):
        super(UImainwindow, self).__init__()


class UIregister(register):
    def __init__(self):
        super(UIregister, self).__init__()


class UIlogin(login):
    def __init__(self):
        super(UIlogin, self).__init__()


class UIroom(room):
    def __init__(self):
        super(UIroom, self).__init__()


class UIvideo(Video):
    def __init__(self, title):
        super(UIvideo, self).__init__()
        self.setWindowTitle(QCoreApplication.translate("Video", title))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = UImainwindow()
    login = UIlogin()
    register = UIregister()
    playerinfo = UIplayerinfo()
    reset_passwd = UIreset_password()
    login.show()
    main.show()
    # 显示金币数量
    numb = '500'
    main.show_coins(numb)
    # 主界面个人信息按钮弹窗
    login.Button_forgot.clicked.connect(reset_passwd.OPEN)
    main.Button_playerinfo.clicked.connect(playerinfo.OPEN)
    # 设定昵称n，获取昵称n
    n = "888"
    playerinfo.get_gamename()
    playerinfo.set_gamename(n)
    s = '90%'
    playerinfo.show_winpercent(s)
    playerinfo.show_lcdnumbs('10005', '2031')
    # 登录界面注册按钮弹窗
    login.Button_register.clicked.connect(register.OPEN)
    sys.exit(app.exec_())
