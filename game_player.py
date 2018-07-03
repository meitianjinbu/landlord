from socket import *
import random as R
from poker import *
import pickle
from game_rule import *


class Player(object):
    def __init__(self, sockfd, user_id):
        self.sockfd = sockfd
        self.user_id = user_id
        # 初始化玩家信息
        self.get_player_info()
        self.get_rank_list()

    def get_player_info(self):
        self.sockfd.send(('op_router-player_info-' + self.user_id).encode())
        data = self.sockfd.recv(2048)
        if not data:
            print('lost the connection from server?')
            return
        self.game_info, self.fr_list = pickle.loads(data)

    def get_rank_list(self):
        self.sockfd.send(('op_router-rank_list').encode())
        data = self.sockfd.recv(2048)
        if not data:
            print('lost the connection from server?')
            return
        self.rank_score, self.rank_wrate = pickle.loads(data)

    def update_info(self, score_table):
        if score_table[2][0] == '_':
            tmp_score = self.game_info['score'] - int(score_table[2][1:])
        else:
            tmp_score = self.game_info['score'] + int(score_table[2])
        self.game_info['score'] = tmp_score if tmp_score > 0 else 0
        self.game_info['total_games'] += 1
        self.game_info['win_rate'] = round(self.game_info['win_rate'] + int(score_table[3]) * 100 / self.game_info['total_games'])
        self.game_info['total_landlord'] += int(score_table[0])

    # 出牌
    def send_pokers(self, value, room_obj, connfd, signal_msg=None):
        if value:
            pokers = []
            # 循环获取被选中要出的牌，存到pokers列表中
            for poker in room_obj.selected_pokers():
                pokers.append(poker.name)
            # 检查出的牌是否合法
            chk_result = check(pokers)
            if room_obj.status.count(True) == 3 or (room_obj.status.count(False) == 2 and room_obj.status[self.pos]):  # 你是第一个出牌
                if chk_result:
                    # 可以出的话，把出的牌，显示在指定位置，参数分别是牌列表，x坐标，y坐标，牌的比例大小
                    room_obj.reshow_pokers(pokers, 250, 150, 0.15)
                    # 调用了这个类当中定义的发送给下个玩家消息的函数，参数是定好的操作 字母，牌列表，发送消息的套接字
                    self.next_player('S', repr(pokers) + '-' + chk_result, connfd)
                    room_obj.pass_poker.hide()
                    room_obj.send_poker.hide()
                    if chk_result == 'zd':
                        room_obj.score_table[2] *= 2
                else:
                    room_obj.homing_pokers()
                    return
            else:
                for i in range(len(room_obj.status)):
                    if room_obj.status[i] != True and room_obj.status[i] != False:
                        if chk_result and compare(eval(room_obj.status[i][0]), pokers, room_obj.status[i][1], chk_result):
                            self.next_player('S', repr(pokers) + '-' + chk_result, connfd)
                            room_obj.status[i] = True
                            room_obj.reshow_pokers(pokers, 250, 150, 0.15)
                            room_obj.pass_poker.hide()
                            room_obj.send_poker.hide()
                            if chk_result == 'zd':
                                room_obj.score_table[2] *= 2
                        else:
                            room_obj.homing_pokers()
                            return
            room_obj.poker_num[self.pos] -= len(pokers)
            room_obj.show_rpokers(room_obj.poker_num, self.pos)
            # 牌出完了，结束游戏，重新进入未准备状态
            if room_obj.poker_num[self.pos] == 0:
                self.next_player('F', 0, connfd)
                room_obj.score_table[3] = self.pos
                signal_msg.emit('F-0' + '-' + str(self.pos))  # 告诉自己的窗口也要重新初始化
            room_obj.status[self.pos] = True
        else:
            room_obj.status[self.pos] = False
            self.next_player('S', 0, connfd)
            room_obj.pass_poker.hide()
            room_obj.send_poker.hide()
        room_obj.show_timer(-1)

    # 收到其他玩家出的牌信息，然后显示在指定位置，如果到自己出牌了就显示出牌和不出的按钮，根据进房间的顺序排的出牌顺序
    def confirm_send_pokers(self, msg, room_obj):
        if msg[0] != '0':
            for i in range(len(room_obj.status)):
                if i == int(msg[2]):
                    room_obj.status[i] = msg[:2]
                elif room_obj.status[i] != False:
                    room_obj.status[i] = True
        else:
            room_obj.status[int(msg[1])] = False
        if msg[0] != '0':
            room_obj.poker_num[int(msg[2])] -= len(eval(msg[0]))
            room_obj.show_rpokers(room_obj.poker_num, self.pos)
            if msg[1] == 'zd':
                room_obj.score_table[2] *= 2  # 炸弹翻倍
            if self.pos == (int(msg[2]) + 1) % 3:
                room_obj.show_pokers(eval(msg[0]), 0, 30, 0.15)
                room_obj.remove_pokers(150)
                room_obj.pass_poker.show()
                if (room_obj.status.count(True) == 2 and room_obj.status.count(False) == 1) or \
                    room_obj.status.count(True) == 3 or \
                    (room_obj.status.count(False) == 2 and room_obj.status[self.pos]):
                    # True/True/False的时候并且自己是出牌方，那也是一轮的开始，因为存在一个False是上一圈的
                    room_obj.status = [True, True, True]
                    room_obj.pass_poker.hide()
                room_obj.send_poker.show()
                room_obj.show_timer(1)
            elif self.pos == (int(msg[2]) - 1) % 3:
                room_obj.show_pokers(eval(msg[0]), 550, 30, 0.15)
                room_obj.show_timer(0)
        elif self.pos == (int(msg[1]) + 1) % 3:
                room_obj.remove_pokers(150)
                room_obj.pass_poker.show()
                if (room_obj.status.count(True) == 2 and room_obj.status.count(False) == 1) or \
                    room_obj.status.count(True) == 3 or \
                    (room_obj.status.count(False) == 2 and room_obj.status[self.pos]):
                    # True/True/False的时候并且自己是出牌方，那也是一轮的开始，因为存在一个False是上一圈的
                    room_obj.status = [True, True, True]
                    room_obj.pass_poker.hide()
                room_obj.send_poker.show()
                room_obj.show_timer(1)

    # 发牌
    def deal(self, room_obj, connfd):
        poker = Poker()
        # 由第一个进入房间的玩家主动来给其他人发牌
        if self.pos == 0:
            # 随机一个人来先叫地主
            room_obj.first = R.randint(0, 2)
            if self.pos != room_obj.first:
                room_obj.pass_landlord.hide()
                room_obj.get_landlord.hide()
            # 生成三个玩家的牌和底牌
            p1, p2, p3, room_obj.cover = poker.fa()
            # 显示自己的牌
            room_obj.show_pokers(p1, 70, 328, 0.22)
            room_obj.show_rpokers(room_obj.poker_num, self.pos)
            # 把其他两家的牌发送给对方
            for i in range(len(self.members)):
                connfd.sendto(('D-'+ str(room_obj.first) + '-' + repr(eval('p' + str(i + 2)) + room_obj.cover)).encode(), self.members[i])

    # 刚开始进入房间的时候，获取初始的牌
    def get_pokers(self, msg, room_obj):
        # 随机谁先叫地主
        room_obj.first = int(msg[0])
        if self.pos != room_obj.first:
            room_obj.pass_landlord.hide()
            room_obj.get_landlord.hide()

        # 收到第一个进入房间的玩家发过来的牌，进行和底牌分离，并显示自己的牌
        room_obj.cover = eval(msg[1])[-3:]
        room_obj.show_pokers(eval(msg[1])[:-3], 70, 328, 0.22)
        room_obj.show_rpokers(room_obj.poker_num, self.pos)

    def redeal(self, room_obj, connfd):
        room_obj.status = [True, True, True]  # reset status
        room_obj.remove_pokers()
        self.deal(room_obj, connfd)
        if self.pos == room_obj.first:
            room_obj.pass_landlord.show()
            room_obj.get_landlord.show()

    # 抢地主
    def get_landlord(self, value, room_obj, connfd):
        if room_obj.landlord_num > 3:
            return
        if value == 1:
            room_obj.landlord_num += 1
            room_obj.score_table[2] *= 2  # 加倍
        elif value == 0:
            room_obj.status[self.pos] = False

        room_obj.pass_landlord.hide()
        room_obj.get_landlord.hide()

        if (room_obj.status.count(True) == 1 and room_obj.landlord_num >= 1) or room_obj.landlord_num == 3:
            if room_obj.status[self.pos]:
                room_obj.refresh_pokers(70, 328, room_obj.cover, Poker.mapai)
                room_obj.score_table[0] = self.pos
                room_obj.send_poker.show()
                room_obj.show_timer(1)
                room_obj.get_hat(1)
            else:
                room_obj.show_timer(0)
                if room_obj.status.count(True) == 1:
                    room_obj.score_table[0] = room_obj.status.index(True)
                elif room_obj.status.count(True) == 2:
                    room_obj.score_table[0] = (room_obj.first + 1) % 3
                else:
                    room_obj.score_table[0] = (room_obj.first + 2) % 3
                print(room_obj.status, room_obj.landlord_num)
                if (room_obj.score_table[0] + 1) % 3 == self.pos:
                    room_obj.get_hat(0)
                else:
                    room_obj.get_hat(-1)
            # 显示底牌
            room_obj.show_pokers(room_obj.cover, 270, 30, 0.15)
            room_obj.poker_num[room_obj.score_table[0]] += 3
            room_obj.show_rpokers(room_obj.poker_num, self.pos)
            room_obj.status = [True, True, True]  # reset status
        elif room_obj.status.count(False) == 3:
            self.redeal(room_obj, connfd)

        # L 代表抢地主操作
        self.next_player('L', value, connfd)

    # 确认谁是地主，并更改按钮的绑定函数，可以改成QT里面的发信号修改ui的方式
    def confirm_landlord(self, msg, room_obj, connfd):
        if msg[0] == '1':
            room_obj.landlord_num += 1
            room_obj.score_table[2] *= 2  # 加倍
        elif msg[0] == '0':
            room_obj.status[int(msg[1])] = False
        if (room_obj.status.count(True) == 1 and room_obj.landlord_num >= 1) or room_obj.landlord_num == 3:
            if room_obj.status[self.pos] and not room_obj.status[int(msg[1])]:
                room_obj.refresh_pokers(70, 328, room_obj.cover, Poker.mapai)
                room_obj.score_table[0] = self.pos
                room_obj.send_poker.show()
                room_obj.show_timer(1)
                room_obj.get_hat(1)
            else:
                room_obj.show_timer(0)
                if room_obj.status.count(True) == 1:
                    room_obj.score_table[0] = room_obj.status.index(True)
                elif room_obj.status.count(True) == 2:
                    room_obj.score_table[0] = (room_obj.first + 1) % 3
                else:
                    room_obj.score_table[0] = (room_obj.first + 2) % 3
                if (room_obj.score_table[0] + 1) % 3 == self.pos:
                    room_obj.get_hat(0)
                else:
                    room_obj.get_hat(-1)
            # 显示底牌
            room_obj.show_pokers(room_obj.cover, 270, 30, 0.15)
            room_obj.poker_num[room_obj.score_table[0]] += 3
            room_obj.show_rpokers(room_obj.poker_num, self.pos)
            room_obj.pass_landlord.hide()
            room_obj.get_landlord.hide()
            room_obj.status = [True, True, True]  # reset status
            return
        elif room_obj.status.count(False) == 3:
            self.redeal(room_obj, connfd)
            return

        if self.pos == (int(msg[1]) + 1) % 3:
            if room_obj.status[self.pos]:
                room_obj.pass_landlord.show()
                room_obj.get_landlord.show()
            else:
                self.next_player('L', 0, connfd)

    # 发送给下个玩家消息的接口函数
    def next_player(self, op, value, connfd):
        for addr in self.members:
            if isinstance(value, int) and self.send_msg('%s-%d-%d' % (op, value, self.pos), addr, 3, connfd):
                print('发送ok')
            elif isinstance(value, str) and self.send_msg('%s-%s-%d' % (op, value, self.pos), addr, 3, connfd):
                print('发送ok')
            else:
                print(addr, '掉线了')

    # 实际发送消息的函数，本来是打算设置超时断开连接的功能，目前还没完善好。
    def send_msg(self, content, addr, n, connfd):
        '''超时发送n次'''
        connfd.sendto(content.encode(), addr)
        return True
        # i = 0
        # while i < n:
        #     self.connfd.sendto(content.encode(), addr)
        #     fb, a = self.connfd.recvfrom(2048)
        #     if fb and a == addr:
        #         return True
        #     else:
        #         i += 1
        #         continue
