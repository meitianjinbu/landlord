from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .video import Ui_video


class Video(QWidget, Ui_video):
    def __init__(self):
        super(Video, self).__init__()
        self.setupUi(self)

    def refresh_video(self, img):
        self.label.setPixmap(QPixmap.fromImage(img))
