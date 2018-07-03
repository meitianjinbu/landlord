from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_video(object):
    def __init__(self):
        super(Ui_video, self).__init__()
        self.setupUi(self)

    def setupUi(self, Video):
        Video.setObjectName("Video")
        Video.resize(480, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Video.sizePolicy().hasHeightForWidth())
        Video.setSizePolicy(sizePolicy)
        Video.setMinimumSize(QtCore.QSize(480, 320))
        Video.setMaximumSize(QtCore.QSize(480, 320))
        Video.setSizeIncrement(QtCore.QSize(0, 0))
        self.label = QtWidgets.QLabel(Video)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 320))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(480, 320))
        self.label.setMaximumSize(QtCore.QSize(480, 320))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pic/gui/login2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Video)
        QtCore.QMetaObject.connectSlotsByName(Video)

    def retranslateUi(self, Video):
        _translate = QtCore.QCoreApplication.translate
        Video.setWindowTitle(_translate("Video", "Video"))
