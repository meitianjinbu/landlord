from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .room import Ui_Room

POKER_POS = (70, 328)
POKER_MOVE = 20
POKER_SPACING = 27
POKER_SCALE = 0.22
POKER_TIMER = 20


class MyItem(QGraphicsPixmapItem):
    def __init__(self, name, parent=None):
        super(MyItem, self).__init__(parent)
        self.setAcceptedMouseButtons(self.acceptedMouseButtons())
        self.name = name

    def mousePressEvent(self, event):
        print(self.y())
        if self.y() == POKER_POS[1]:
            self.setPos(self.x(), POKER_POS[1] - POKER_MOVE)
        else:
            self.setPos(self.x(), POKER_POS[1])

    def mouseDoubleClickEvent(self, event):
        print('hover leave')


class room(QWidget, Ui_Room):
    def __init__(self):
        super(room, self).__init__()
        self.setupUi(self)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(
            QPixmap('pic/gui/room.jpg').scaled(self.size())))  # 设置背景图片
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.timer_running = False

        self.screen_center()

    def show_pokers(self, pokers, posX, posY, scale):
        '''添加并显示自己所有牌'''
        if posY != POKER_POS[1]:
            self.remove_pokers(30)
        pos = 0
        for poker in pokers:
            item = MyItem(poker)
            pixmap = QPixmap('pic/%s_of_%s.png' % (poker[0], poker[1:]))
            item.setPixmap(pixmap)
            item.setScale(scale)
            self.graphicsScene.addItem(item)
            # item.setY(10)
            item.setY(posY)
            item.setX(posX + pos)
            pos += POKER_SPACING
            print(item.name)

    def refresh_pokers(self, posX, posY, cover=None, sort_func=None):
        '''出牌后刷新显示自己所有牌'''
        all_pokers = self.graphicsScene.items()
        if cover is not None:
            # 把底牌添加给地主，并且刷新显示
            for poker in cover:
                item = MyItem(poker)
                pixmap = QPixmap('pic/%s_of_%s.png' % (poker[0], poker[1:]))
                item.setPixmap(pixmap)
                item.setScale(POKER_SCALE)
                self.graphicsScene.addItem(item)
                item.setY(posY)
            all_pokers = sort_func(None, self.graphicsScene.items())

        pos = 0
        for i in range(len(all_pokers), 0, -1):
            if (all_pokers[i - 1].y()) == posY:
                all_pokers[i - 1].setX(posX + pos)
                all_pokers[i - 1].setZValue(posX + pos)
                pos += POKER_SPACING

    def remove_pokers(self, posY=0):
        '''重新出牌后，移除上次出的牌，一定更要先移除，再显示新出的牌
           posY如果为0，则删除界面上所有items
        '''
        if not posY:
            self.graphicsScene.clear()
        else:
            for i in self.graphicsScene.items():
                if i.y() == posY:
                    self.graphicsScene.removeItem(i)

    def homing_pokers(self):
        for i in self.graphicsScene.items():
            if i.y() == (POKER_POS[1] - POKER_MOVE):
                i.setY(POKER_POS[1])

    def reshow_pokers(self, lst, posX, posY, scale):
        '''打出的牌指定显示'''
        self.remove_pokers(posY)
        self.remove_pokers(30)
        for i in self.graphicsScene.items():
            # print(i.name)
            if i.name in lst:
                i.setScale(scale)
                i.setX(posX)
                i.setY(posY)
                i.setZValue(posX)
                posX += POKER_SPACING
                i.setAcceptedMouseButtons(Qt.NoButton)
        self.refresh_pokers(85, POKER_POS[1])

    def get_poker_count(self):
        count = 0
        for i in self.graphicsScene.items():
            if i.y() == POKER_POS[1]:
                count += 1
        return count

    def show_rpokers(self, nums, pos):
        self.rpokers_self.display(nums[pos])
        self.rpokers_sj.display(nums[(pos - 1) % 3])
        self.rpokers_xj.display(nums[(pos + 1) % 3])

    def set_timer(self):
        self.seconds = POKER_TIMER
        self.timer_running = True
        self.timer = QTimer()
        self.timer.start(1000)
        # 信号连接到槽
        self.timer.timeout.connect(self.refresh_timer)
        self.label_timer.setText(QCoreApplication.translate("room", str(self.seconds)))

    def refresh_timer(self):
        self.seconds -= 1
        if self.seconds > 0:
            self.label_timer.setText(QCoreApplication.translate("room", str(self.seconds)))
        else:
            self.label_timer.hide()
            self.timer_running = False
            self.timer.stop()
            if self.label_timer.y() == 330:
                self.signal_msg.emit('F-2-' + str(self.pos))

    def show_timer(self, value=1):
        self.label_timer.hide()
        if self.timer_running:
            self.timer_running = False
            self.timer.stop()
        if value == 1:
            self.label_timer.setGeometry(QRect(470, 330, 50, 50))
        elif value == -1:
            self.label_timer.setGeometry(QRect(770, 160, 50, 50))
        else:
            self.label_timer.setGeometry(QRect(150, 150, 50, 50))
        self.set_timer()
        self.label_timer.show()

    def selected_pokers(self, y_axis=POKER_POS[1] - POKER_MOVE):
        item_lst = []
        for i in self.graphicsScene.items():
            if i.y() == y_axis:
                item_lst.append(i)
        return item_lst

    def get_hat(self, value):
        if value == 1:
            self.label_hat.setGeometry(QRect(135, 440, 50, 50))
        elif value == -1:
            self.label_hat.setGeometry(QRect(785, 110, 50, 50))
        else:
            self.label_hat.setGeometry(QRect(135, 100, 50, 50))

    def show_result(self, value):
        if value:
            self.label_result.setPalette(self.win_palette)
            self.label_result.setAutoFillBackground(True)
            self.label_result.setGeometry(QRect(310, 150, 400, 225))
        else:
            self.label_result.setPalette(self.lose_palette)
            self.label_result.setAutoFillBackground(True)
            self.label_result.setGeometry(QRect(310, 150, 400, 225))

    def screen_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def OPEN(self):
        self.show()
