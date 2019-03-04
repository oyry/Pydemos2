import pymysql
import warnings
warnings.filterwarnings("ignore")
class Mysql(object):
    def __init__(self, port, db, sql, host='172.17.12.41', user='root', passwd='123'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.sql = sql
        self.conn = self.Dbtest()
    def Dbtest(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        cur = conn.cursor()
        cur.execute(self.sql)
        for i in cur.fetchall():
            print(i)
        return i
        cur.close()
        conn.close()

if __name__=="__main__":
     a=Mysql(3307,'omcaccnt','SELECT GROUP_ID,TYPE_ID,BATCH_ID,CID,ACCNT_NO,BALANCE,`STATUS`,USE_SCOPE,TRANS_ID,SRC_CHANNEL,SRC_CORP,SRC_BUID,SRC_OP FROM accnt_batch WHERE CID=9800000038571 AND TYPE_ID="YE190109000005"')