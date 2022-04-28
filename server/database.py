
import pymysql
from config import db_name,db_user,db_pw,db_host,userTable,userbasicdata 


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
        sql="insert into "+userTable+" (name,id,password) values (" + "'"+name+"','"+id+"','"+pw+"')"
        self.cursor.execute(sql)
        
        sql="insert into "+userbasicdata+" (id) values ("+"'"+id+"');"
        self.cursor.execute(sql)
        
        self.conn.commit() #save
        
        
    #기초문진 정보 저장
    def update_basic_paperweight(self,name,sex,age,height,weight,event,history,pregnant):
        
        sql="select id from "+userTable+" where name='"+name+"'"
        self.cursor.execute(sql)

        userid=self.cursor.fetchall()[0][0]
        
        sql="update "+userbasicdata +" set sex='"+sex+"' where id='"+userid+"'"
        self.cursor.execute(sql)
        
        sql="update "+userbasicdata +" set age='"+age+"' where id='"+userid+"'"
        self.cursor.execute(sql)
        
        
        sql="update "+userbasicdata +" set height='"+height+"' where id='"+userid+"'"
        self.cursor.execute(sql)
        
        sql="update "+userbasicdata +" set weight='"+weight+"' where id='"+userid+"'"
        self.cursor.execute(sql)
        
        sql="update "+userbasicdata +" set event='"+event+"' where id='"+userid+"'"
        self.cursor.execute(sql)
        
        sql="update "+userbasicdata +" set history='"+history+"' where id='"+userid+"'"
        self.cursor.execute(sql)
        
        sql="update "+userbasicdata +" set pregnant='"+pregnant+"' where id='"+userid+"'"
        self.cursor.execute(sql)
        
        self.conn.commit() #save
        
        


    #기초문진 정보 반환
    def get_basic_papaerweight(self,name):
        
        sql="select id from "+userTable+" where name='"+name+"'"
        self.cursor.execute(sql)

        userid=self.cursor.fetchall()[0][0]
        
        sql="select sex,age,height,weight,event,history,pregnant from "+userbasicdata+" where id='"+userid+"'"

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
    