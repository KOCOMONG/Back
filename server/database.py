
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

    

    #회원가입 회원정보 저장
    def register(self,name,id,pw):
        sql="insert into "+userTable+" (name,id,pw) values (" + "'"+name+"','"+id+"','"+pw+"')"
        self.cursor.execute(sql)
        self.conn.commit() #save
        
        
    #기초문진 정보 저장
    def update_basic_paperweight(self,name,sex,age,height,weight):
        sql="update "+userTable+" set sex='"+sex+"' where name='"+name+"'"
        self.cursor.execute(sql)
        
        sql="update "+userTable+" set age='"+age+"' where name='"+name+"'"
        self.cursor.execute(sql)
        
        sql="update "+userTable+" set height='"+height+"' where name='"+name+"'"
        self.cursor.execute(sql)
        
        sql="update "+userTable+" set weight='"+weight+"' where name='"+name+"'"
        self.cursor.execute(sql)
        
        self.conn.commit() #save
        
        


    #기초문진 정보 반환
    def get_basic_papaerweight(self,name):
        sql="select sex,age,height,weight from "+userTable+" where name='"+name+"'"

        self.cursor.execute(sql)
        
        
        data_tuple=self.cursor.fetchone() #tuple
        
        data_dic={} #dictionary
        data_dic['sex']=data_tuple[0]
        data_dic['age']=data_tuple[1]
        data_dic['height']=data_tuple[2]
        data_dic['weight']=data_tuple[3]
        
        return data_dic    
    