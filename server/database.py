
import pymysql
from config import db_name,db_user,db_pw,db_host


class database:
    

    #기본형태 : cursor.execute("SQL 실행문")

    #connect -> create cursor 까지
    def __init__(self):
        self.db=db_name
        self.user=db_user
        self.pw=db_pw
        self.host=db_host
        

    #db connect
    def connect(self):
        self.conn=pymysql.connect(host=self.host,user=self.user,password=self.pw,db=self.db,charset='utf8')
        self.cursor=self.conn.cursor()

    #db connect out 
    def connect_out(self):
        self.conn.close()

    #id 중복 체크
    def checkid(self,id):
        sql="select id from userlist where id='"+id+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        if not data_tuple:
            return 1 #id 중복 X
        else:
            return 0 #id 중복 

    #회원가입
    def register(self,name,id,pw):
        sql="insert into userlist (name,id,pw) values (" + "'"+name+"','"+id+"','"+pw+"')"
        self.cursor.execute(sql)
        
        sql="insert into userbasicdata (id) values ("+"'"+id+"');"
        self.cursor.execute(sql)
        
        self.conn.commit() #save
        
        
    #기초 문진 데이터 저장
    def update_userbasicdata(self,id,sex,age,height,weight,event,history,pregnant):

        sql="update userbasicdata set sex='"+sex+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        sql="update userbasicdata set age='"+age+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        
        sql="update userbasicdata set height='"+height+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        sql="update userbasicdata set weight='"+weight+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        sql="update userbasicdata set event='"+event+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        sql="update userbasicdata set history='"+history+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        sql="update userbasicdata set pregnant='"+pregnant+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        self.conn.commit() #save
        
        
    #.해당 id의 name,pw 반환
    def get_userdata(self,id):
        sql="select name,pw from "+userlist+" where id='"+id+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        data_dic={} #dictionary
        data_dic['name']=data_tuple[0]
        data_dic['pw']=data_tuple[1]

        return data_dic

    #해당 id의 기초 문진 데이터 반환
    def get_userbasicdata(self,id):
        

        sql="select sex,age,height,weight,event,history,pregnant from userbasicdata where id='"+id+"'"

        self.cursor.execute(sql)
        
        
        data_tuple=self.cursor.fetchone() #tuple
        
        data_dic={} #dictionary
        data_dic['sex']=data_tuple[0]
        data_dic['age']=data_tuple[1]
        data_dic['height']=data_tuple[2]
        data_dic['weight']=data_tuple[3]
        data_dic['event']=data_tuple[4]
        data_dic['history']=data_tuple[5]
        data_dic['pregnant']=data_tuple[6]
        
        
        return data_dic    
    
    #medicine data 찾기 
    def find_keep(self,name):
        sql="select keep from medicine where name='"+name+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        data=data_tuple[0]

        return data
    
    def find_effect(self,name):
        sql="select effect from medicine where name='"+name+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        data=data_tuple[0]

        return data

    
    def find_useage(self,name):
        sql="select useage from medicine where name='"+name+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        data=data_tuple[0]

        return data

    def find_caution(self,name):
        sql="select caution from medicine where name='"+name+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        data=data_tuple[0]
        print(data)
        return data

    def find_information(self,name):
        sql="select information from medicine where name='"+name+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        data=data_tuple[0]

        return data