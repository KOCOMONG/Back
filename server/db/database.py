
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

    #login
    def login(self,id,pw):
        sql="select * from userlist where id='"+id+"' and pw='"+pw+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        if data_tuple:
            return 1 #login 성공
        else:
            return 0 #일치하지 않는 아이디,비번

            
    #회원가입
    def register(self,name,id,pw):
        sql="insert into userlist (name,id,pw) values (" + "'"+name+"','"+id+"','"+pw+"')"
        self.cursor.execute(sql)
        
        sql="insert into userbasicdata (id) values ("+"'"+id+"');" #기초문진데이터 테이블 세팅
        self.cursor.execute(sql)

        sql="insert into diseasedata (id) values ("+"'"+id+"');" #질병진단데이터 테이블 세팅
        self.cursor.execute(sql)
        
        self.conn.commit() #save
        
        
    #기초 문진 데이터 업데이트
    def update_userbasicdata(self,id,sex,age,height,weight,event,past,feminity):

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
        
        sql="update userbasicdata set past='"+past+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        sql="update userbasicdata set feminity='"+feminity +"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        self.conn.commit() #save
        
    #질병 진단 데이터 업데이트
    def update_diseasedata(self,id,chiefcomplaint,onset,location):
        sql="update diseasedata set chiefcomplaint='"+chiefcomplaint+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        sql="update diseasedata set onset='"+onset+"' where id='"+id+"'"
        self.cursor.execute(sql)

        sql="update diseasedata set location='"+location+"' where id='"+id+"'"
        self.cursor.execute(sql)
        
        
        self.conn.commit() #save
    #.해당 id의 name,pw 반환
    def get_userdata(self,id):
        sql="select name,pw from userlist where id='"+id+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        data_dic={} #dictionary
        data_dic['name']=data_tuple[0]
        data_dic['pw']=data_tuple[1]

        return data_dic

    #해당 id의 기초 문진 데이터 반환
    def get_userbasicdata(self,id):
        

        sql="select sex,age,height,weight,event,past,feminity  from userbasicdata where id='"+id+"'"

        self.cursor.execute(sql)
        
        
        data_tuple=self.cursor.fetchone() #tuple
        
        data_dic={} #dictionary
        data_dic['sex']=data_tuple[0]
        data_dic['age']=data_tuple[1]
        data_dic['height']=data_tuple[2]
        data_dic['weight']=data_tuple[3]
        data_dic['event']=data_tuple[4]
        data_dic['past']=data_tuple[5]
        data_dic['feminity']=data_tuple[6]
        

        return data_dic    

    #질병진단 필수 데이터 반환
    def get_diseasedata(self,id):
        sql="select chiefcomplaint,onset,location from diseasedata where id='"+id+"'"

        self.cursor.execute(sql)
        
        
        data_tuple=self.cursor.fetchone() #tuple

        data_dic={} #dictionary
        data_dic['chiefcomplaint']=data_tuple[0]
        data_dic['onset']=data_tuple[1]
        data_dic['location']=data_tuple[2]
        

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
        return data

    def find_information(self,name):
        sql="select information from medicine where name='"+name+"'"
        self.cursor.execute(sql)
        data_tuple=self.cursor.fetchone() #tuple
        data=data_tuple[0]

        return data

    #delete from table
    def deletetable(self,tablename):
        if tablename=="all":
            sql="delete from userlist"
            self.cursor.execute(sql)
            sql="delete from userbasicdata"
            self.cursor.execute(sql)
            sql="delete from diseasedata"
            self.cursor.execute(sql)
        else:
            sql="delete from "+tablename
            self.cursor.execute(sql)
        
        
        self.conn.commit() #save