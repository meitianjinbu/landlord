'''
客户端操作路由类
'''
# import sys
# sys.path.insert(0, '..')
# from db import mysql_load
from db import mysql_load
import pickle


def player_info(connfd, params):
    game_info = mysql_load.select_game_info(*params[:-1])
    fr_list = mysql_load.select_friends(*params[:-1])
    for i in fr_list:
        if i in params[-1]:
            fr_list[i] += params[-1][i]
    info = (game_info, fr_list)
    connfd.send(pickle.dumps(info))


# params第一个为是否为地主，第二个为房间号，第三个为输赢的积分，第四个为是否胜利，第五个为用户id
def update_score(connfd, params):
    ret = mysql_load.update_score(params[-1], params[-2], params[2], params[0])
    if ret:
        connfd.send(b'ok')
    else:
        connfd.send(b'failed')


def login(connfd, params):
    user_id = mysql_load.user_login(*params[:-1])
    addr = params[-1].get(user_id, 'none')
    if user_id and addr == 'none':
        params[-1][user_id] = connfd.getpeername()
        connfd.send(('ok ' + str(user_id)).encode())
    elif addr != 'none':
        connfd.send(b'logged')
    else:
        connfd.send(b'failed')


def register(connfd, params):
    if mysql_load.user_zhuce(*params):
        connfd.send(b'succeed')
    else:
        connfd.send(b'existed')


def change_nickname(connfd, params):
    mysql_load.change_nickname(*params)


def check_vrifinfo(connfd, params):
    if mysql_load.check_vrifinfo(*params):
        connfd.send(b'ok')
    else:
        connfd.send(b'are u kiding me')


def reset_passwd(connfd, params):
    mysql_load.reset_passwd(*params)


def rank_list(connfd):
    connfd.send(pickle.dumps(mysql_load.rank_list()))
