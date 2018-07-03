from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .register import Ui_Register


class register(QWidget, Ui_Register):
    def __init__(self):
        super(register, self).__init__()
        self.setupUi(self)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(
            QPixmap('pic/gui/reg_fgt_info.png').scaled(self.size())))  # 设置背景图片
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.lineEdit_account.setPlaceholderText('请输入账号')
        self.lineEdit_vrifinfo.setPlaceholderText('请填写账号验证信息')
        self.lineEdit_password.setPlaceholderText('仅数字和字母，以字母开头')
        self.lineEdit_passwordconfirm.setPlaceholderText('仅数字和字母，以字母开头')
        self.lineEdit_gamename.setPlaceholderText('请填写游戏昵称')
        self.radioButton_male.toggle()
        self.radioButton_female.toggle()

        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setValidator(QRegExpValidator(
            QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$"), self.lineEdit_password))

        self.lineEdit_passwordconfirm.setEchoMode(QLineEdit.Password)
        self.Button_cancel.clicked.connect(self.close)
        # self.Button_ok.clicked.connect(self.register_info)
        self.screen_center()

    def screen_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    # 判断注册信息是否填写完整
    def register_info(self):
        lineEdit_passwd = self.lineEdit_password.text()
        lineEdit_passwdc = self.lineEdit_passwordconfirm.text()

        if lineEdit_passwd != lineEdit_passwdc:
            self.register_error()
        elif not self.lineEdit_account.text():
            self.register_error()
        elif not self.lineEdit_password.text():
            self.register_error()
        elif not self.lineEdit_vrifinfo.text():
            self.register_error()
        elif not self.lineEdit_gamename.text():
            self.register_error()
        else:
            if self.radioButton_male.isChecked():
                print('male')
            elif self.radioButton_female.isChecked():
                print('female')
            else:
                self.register_error()

            print(self.lineEdit_account.text())
            print(lineEdit_passwd)
            print(self.lineEdit_vrifinfo.text())
            print(self.lineEdit_gamename.text())

    def register_error(self):
        print('register_error')

    def OPEN(self):
        self.lineEdit_account.setText(
            QCoreApplication.translate("Register", ''))
        self.lineEdit_password.setText(
            QCoreApplication.translate("Register", ''))
        self.lineEdit_passwordconfirm.setText(
            QCoreApplication.translate("Register", ''))
        self.lineEdit_gamename.setText(
            QCoreApplication.translate("Register", ''))
        self.lineEdit_vrifinfo.setText(
            QCoreApplication.translate("Register", ''))
        self.show()
