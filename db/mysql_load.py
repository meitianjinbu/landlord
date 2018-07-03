from .mysql_joker import mysqlpython
import setting
from pymysql import connect
import hashlib


def md5(pwd):
    return hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()

# 注册用户时，用户信息上传数据库
def user_zhuce(username, passwd, nickname, verify, sex):
    conn = connect(**setting.MYSQL_CONFIG)
    cur = conn.cursor()
    passwd = md5(passwd)
    sql_insert = 'insert into user\
        (username,passwd,sex,verify) \
        values("%s","%s","%s","%s");' %\
        (username,passwd,sex,verify)
    sql_insert2 = 'insert into game_info\
        (nickname,user_id) values("%s","%s");'
    try:
        cur.execute(sql_insert)
        user_id = cur.lastrowid
        cur.execute(sql_insert2 % (nickname, user_id))
        conn.commit()
        print('注册成功')
        return True
    except Exception as e:
        print('用户名重复', e)
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()


# 登录时，匹配用户登录信息
def user_login(username, passwd):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    passwd = md5(passwd)
    sql_select = 'select id, username,passwd from user\
                   where username="%s" and passwd="%s";'\
                   % (username, passwd)
    data = user.select_op(sql_select)
    if not data:
        return False
    else:
        print('登录成功')
        return data[0]


# 查看游戏信息
def select_game_info(user_id):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql_select = 'select nickname, score, if(total_games > 0, (win_games / total_games * 100), 0)  as win_rate, total_games, total_landlord from game_info\
                  where user_id="%d"' % int(user_id)
    data = user.select_op(sql_select)
    doc = {'nickname': data[0], 'score': data[1],
           'win_rate': round(data[2]), 'total_games': data[3],
           'total_landlord': data[4]}
    return doc


# 为重置密码操作，验证信息
def check_vrifinfo(username, verify):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql_select = 'select id from user\
                  where username="%s" and verify="%s"' % (username, verify)
    data = user.select_op(sql_select)
    if data:
        return True
    return False


# 完成重置密码
def reset_passwd(username, newpasswd):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    newpasswd = md5(newpasswd)
    sql_update = 'update user set passwd="%s" where username="%s"' % (
        newpasswd, username)
    user.InserUdDel(sql_update)


# 完成一局游戏后，玩家信息的变化
def update_score(user_id, win, score, landlord):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    if score[0] == '_':
      score = -int(score[1:])
    else:
      score = int(score)
    sql_update = 'update game_info set score=if(%d < 0 and score < -%d, 0, score + %d),\
               total_games = total_games+1,\
               total_landlord = total_landlord+%s,\
               win_games = win_games+%s\
               where user_id=%s;' % (score, score, score, landlord, win, user_id)
    try:
        user.InserUdDel(sql_update)
        print('结算成功')
        return True
    except Exception as e:
        return False


# 查看游戏好友以及好友信息
def select_friends(user_id):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql_select = 'select t2.user_id, t2.nickname, t2.score, if(t2.total_games > 0, (t2.win_games / t2.total_games * 100), 0)  as win_rate, t2.total_games, t2.total_landlord\
                  from user_friend as t1 left join game_info as t2 on t1.friend_id = t2.user_id\
                  where t1.user_id = %d' % int(user_id)
    result = user.select_opall(sql_select)
    doc = {}
    for info in result:
        doc[info[0]] = info[1:]
    return doc

# 游戏内积分和胜率排名
def rank_list():
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql_score = 'select nickname,score from game_info where score > 0 order by score desc limit 10;'
    sql_wrate = 'select nickname,win_games / total_games * 100 as win_rate from game_info where total_games > 0 and win_games > 0 order by win_rate desc limit 10;'
    rlt_score = user.select_opall(sql_score)
    rlt_wrate = user.select_opall(sql_wrate)
    return rlt_score, rlt_wrate


# 改昵称
def change_nickname(old_nickname,new_nickname):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql = 'update game_info set nickname = "%s" where \
           nickname = "%s";' % (new_nickname, old_nickname)
    user.InserUdDel(sql)
    print('change nickname succeed')


# 添加好友
def addfrirnd(nickname, friend):
    user = mysqlpython('localhost', 3306, 'root', '123456', 'pokergame')
    sql = 'insert into userfriends(nickname,f_nickname) \
           values("%s","%s");' % (nickname, friend)
    user.InserUdDel(sql)
    print('添加成功')

# 删除用户
def deluser(nickname):
    user = mysqlpython('localhost', 3306, 'root', '123456', 'pokergame')
    sql_login = 'delete from login where\
                l_nickname = "%s";' % nickname
    sql_user = 'delete from userinfo where\
                u_nicakname = "%s";' % nickname
    user.InserUdDel(sql_login+sql_user)


#完成一局游戏后，战绩的改变
def zhanji(nickname,player1,player2,fightinfo):
    user = mysqlpython('localhost', 3306, 'root', '123456', 'pokergame')
    sql = 'insert into zhanji(nickname,player1,player2,fightinfo)\
           values("%s","%s","%s","%s")'%(nickname,player1,player2,fightinfo)
    user.InserUdDel(sql)
    print('ok')

#查看玩家战绩
def select_zhanji(nickname):
    user = mysqlpython('localhost', 3306, 'root', '123456', 'pokergame')
    sql = 'select * from zhanji where nickname = "%s";'%nickname
    result = user.select_opall(sql) 
    if not result:
        return
    lst_zhanji = []
    for res in result:
        lst = []
        for info in res:
            lst.append(info)
        lst[2] = [lst[2],select_userinfo(lst[2])]
        lst[3] = [lst[3],select_userinfo(lst[3])]
        lst_zhanji.append(lst)
    print(lst_zhanji)


if __name__ == '__main__': 
  # user_zhuce("yf123",123456,"xiangcai","abc","boy")
  # user_chushihua("xiangcai","boy")
  # select_userinfo("xiangcai")
  # addfrirnd('xiangcai','wewsd')
  # select_friends("xiangcai")
  # user_login('yf123',123456)
  # rankscore()
  # update_score('xiangcai',600)
  # select_userinfo("xiangcai")
  # changenickname('xiangcai','xc')
  # zhanji('xiangcai','player1','player2','v')
  # user_zhuce("yf1234",12345,"player1","abc","boy")
  # user_chushihua("player1","boy")
  # user_zhuce("yf1235",12346,"player2","abc","boy")
  # user_chushihua("player2","boy")
  select_zhanji('xiangcai')
