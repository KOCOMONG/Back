import pymysql
from config import db_name,db_user,db_pw,db_host,tableName_register 


class database:
    

    #기본형태 : cursor.execute("SQL 실행문")

    #connect -> create cursor 까지
    def __init__(self):
        self.db=db_name
        self.user=db_user
        self.pw=db_pw
        self.host=db_host
        

    #connect
    def connect(self):
        self.conn=pymysql.connect(host=self.host,user=self.user,password=self.pw,db=self.db,charset='utf8')
        self.cursor=self.conn.cursor()

    #connect out 
    def connect_out(self):
        self.conn.close()


    #회원정보 입력
    def register(self,name,userid,userpw):
        sql="insert into "+tableName_register+" values(" + "'"+name+"','"+userid+"','"+userpw+"')"
        self.cursor.execute(sql)
        self.conn.commit() #save


    