from pymysql import *

class mysqlpython:
    def __init__(self,host,port,user,passwd,db,charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd =passwd
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host,port=self.port,user=self.user,\
            passwd=self.passwd,db=self.db,charset=self.charset)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def InserUdDel(self,sql):
        self.open()
        self.cur.execute(sql)
        self.conn.commit()
        insert_id = self.cur.lastrowid
        self.close()
        return insert_id

    def select_op(self,sql):
        self.open()
        self.cur.execute(sql)
        result = self.cur.fetchone()
        self.conn.commit()
        self.close()
        return result

    def select_opall(self,sql):
        self.open()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.conn.commit()
        self.close()
        return list(result)


    def delete(self,sql):
        self.open()
        self.cur.execute(sql)
        self.conn.commit()
        self.close()
