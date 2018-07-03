from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .reset_passwd import Ui_reset_password


class reset_password(QWidget, Ui_reset_password):
    def __init__(self):
        super(reset_password, self).__init__()
        self.setupUi(self)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(
            QPixmap('pic/gui/reg_fgt_info.png').scaled(self.size())))  # 设置背景图片
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.screen_center()
        self.lineEdit_password.setValidator(QRegExpValidator(
            QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$"), self.lineEdit_password))
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_passwordconfirm.setEchoMode(QLineEdit.Password)
        self.lineEdit_account.setPlaceholderText('请输入账号')
        self.lineEdit_vrifinfo.setPlaceholderText('请填写账号验证信息')
        self.lineEdit_password.setPlaceholderText('仅数字和字母，以字母开头')
        self.lineEdit_passwordconfirm.setPlaceholderText('仅数字和字母，以字母开头')
        self.lineEdit_password.setEnabled(False)
        self.lineEdit_passwordconfirm.setEnabled(False)

        # self.Button_checkaccount.clicked.connect(self.check_vrifinfo)
        self.Button_cancel.clicked.connect(self.close)
        # self.lineEdit_passwordconfirm.editingFinished.connect(self.new_passwd)
        # self.Button_ok.clicked.connect(self.new_passwd)

    def passwd_error(self):
        print('请输入相同的密码')

    def new_passwd(self):
        lineEdit_passwd = self.lineEdit_password.text()
        lineEdit_passwdc = self.lineEdit_passwordconfirm.text()

        if lineEdit_passwd != lineEdit_passwdc:
            self.passwd_error()
        else:
            print(self.lineEdit_password.text())
            print(self.label_passwordconfirm.text())

    def check_vrifinfo(self):
        print(self.lineEdit_account.text())
        print(self.lineEdit_vrifinfo.text())

    def no__vrifinfo(self):
        print('账号或验证信息填写错误')

    def OPEN(self):
        self.Button_ok.setEnabled(False)
        self.lineEdit_account.setText(
            QCoreApplication.translate("reset_password", ''))
        self.lineEdit_vrifinfo.setText(
            QCoreApplication.translate("reset_password", ''))
        self.lineEdit_password.setText(
            QCoreApplication.translate("reset_password", ''))
        self.lineEdit_passwordconfirm.setText(
            QCoreApplication.translate("reset_password", ''))
        self.show()

    def screen_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def confirm_vrifinfo(self):
        self.Button_ok.setEnabled(True)
        self.lineEdit_password.setEnabled(True)
        self.lineEdit_passwordconfirm.setEnabled(True)
