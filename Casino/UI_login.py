from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .login import Ui_Login


class login(QWidget, Ui_Login):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)

        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(
            QPixmap('pic/gui/login.jpg').scaled(self.size())))  # 设置背景图片
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setValidator(QRegExpValidator(
            QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$"), self.lineEdit_password))
        self.screen_center()
        self.lineEdit_account.setPlaceholderText('请输入账号')
        self.lineEdit_password.setPlaceholderText('密码由数字和字母组成，必须以字母开头')

    def screen_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def OPEN(self):
        self.show()

    def login_error(self, value=0):
        if value == 0:
            self.register_tips_label.setText(QCoreApplication.translate('Login', "账号或密码错误，请重新输入!"))
        elif value == 1:
            self.register_tips_label.setText(QCoreApplication.translate('Login', "账号已登录，请先退出!"))

    def reset_info(self):
        self.lineEdit_account.setText(
            QCoreApplication.translate("Login", ''))
        self.lineEdit_password.setText(
            QCoreApplication.translate("Login", ''))
