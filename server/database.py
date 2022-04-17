
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

    
    #jud user exists
    def jud_user_exists(self,userid):
        sql=""

    #회원가입 회원정보 저장
    def register(self,name,id,pw):
        sql="insert into "+userTable+" (name,id,pw) values (" + "'"+name+"','"+id+"','"+pw+"')"
        self.cursor.execute(sql)
        self.conn.commit() #save
        
        
    #기초문진 정보 저장
    def update_basic_information(self,userid,sex,age,height,weight):
        sql="update "+userTable+" set sex='"+sex+"' where userid='"+userid+"'"
        self.cursor.execute(sql)
        
        sql="update "+userTable+" set age='"+age+"' where userid='"+userid+"'"
        self.cursor.execute(sql)
        
        sql="update "+userTable+" set height='"+height+"' where userid='"+userid+"'"
        self.cursor.execute(sql)
        
        sql="update "+userTable+" set weight='"+weight+"' where userid='"+userid+"'"
        self.cursor.execute(sql)
        
        self.conn.commit() #save
        
        


        
    