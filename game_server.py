from socket import *
from threading import Condition, current_thread
import sys
import pickle
import my_thread
from setting import *


class GameServer(object):
    def __init__(self, addr):
        self.addr = addr
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(addr)
        self.sockfd.listen(5)
        self.serverName = addr[0]
        self.serverPort = addr[1]
        self.queue = []
        self.room = {}
        self.online = {}
        self.rid = [0]
        self.tmp_rid = 0
        self.con = Condition()

    def serverForever(self):
        '''
            服务器启动函数，接收客户端请求，创建新的线程
        '''
        while True:
            print('waiting for a connection...')
            print(self.queue, '匹配等待中')
            connfd, clientAddr = self.sockfd.accept()
            clientThread = my_thread.MyThread(self.handleRequest, (connfd,clientAddr))
            clientThread.setDaemon(True)
            clientThread.start()

    def handleRequest(self, connfd, addr):
            try:
                data = connfd.recv(BUFFERSIZE).decode()
            except OSError:
                data = ''
            if not data:
                for i in self.online:
                    if self.online[i] == addr:
                        del self.online[i]
                        break
                connfd.close()
                current_thread().stoped = True
                return
            data = data.split(OPS_DELIMITER)
            if len(data) > 2:
                module = data[0]
                app = data[1]
                params = data[2].split(PARAM_DELIMITER)
            else:
                module = data[0]
                app = data[1]
                params = []
            if app == 'match_room':
                self.con.acquire()
                if addr not in self.queue:
                    self.queue.append(addr)
                if len(self.queue) >= 3:
                    self.con.notify(3)
                    self.tmp_rid = self.generate_rid()
                    self.room[self.tmp_rid] = self.queue[:3]
                else:
                    self.con.wait()
                connfd.send(pickle.dumps((self.tmp_rid, self.room[self.tmp_rid])))
                self.queue = self.queue[3:]
                self.con.release()
                return
            elif app == 'login' or app == 'player_info':
                params.append(self.online)
            elif app == 'update_score':
                # 设置此对应的房间号空了，让地主来设置
                if int(params[3]):
                    # 提交结算，移除对应的房间信息
                    self.room.pop(int(params[1]))
                    self.rid[int(params[1]) - 1] = 0
            # 将HDL_ROOT加入到环境变量(搜索路径)
            sys.path.insert(0, HDL_ROOT)
            # 导入module模块
            m = __import__(module)
            # 获取module下的app，赋给一个变量绑定
            application = getattr(m, app)
            if not params:
                application(connfd)
            else:
                application(connfd, params)

    def generate_rid(self):
        # 生成的self.rid 是一个顺序排列的数字，所以只需要判断tmp_lst和self.rid是否相等即可
        tmp_lst = [x for x in range(len(self.rid))]
        if self.rid == tmp_lst:
            rid = self.rid[-1] + 1
            self.rid.append(rid)
        else:
            print(self.rid)
            print(tmp_lst)
            # 异或并过滤得到目前空着的第一位置
            rid = list(filter(None, map(lambda x, y: x ^ y, self.rid, tmp_lst)))[0]
            self.rid[rid - 1] = rid
        return rid


# 控制服务器启动
def main():
    httpd = GameServer(ADDR)
    print('Serving HTTP on port', PORT)
    httpd.serverForever()


if __name__ == '__main__':
    main()
