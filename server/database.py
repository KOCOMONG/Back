
import pymysql
from config import db_name,db_user,db_pw,db_host,userTable 


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
        sql="insert into "+userTable+" (username,userid,userpw) values (" + "'"+name+"','"+userid+"','"+userpw+"')"
        self.cursor.execute(sql)
        self.conn.commit() #save

    #회원정보 전송
    def get_user_information(self,username):
        sql="select * from "+userTable+" where username='"+username+"'"
        self.cursor.execute(sql)
        
        rows=self.cursor.fetchall() #result list

        user_information_tuple=rows[0] #user information row, tuple 로 return

        user_information=""
        

        return user_information

        
    