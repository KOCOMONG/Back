

from flask import Blueprint,request
from db.database import database




bp=Blueprint('user',__name__,url_prefix='/user')
db=database() #database class instance 생성

#회원가입
@bp.route("/signup",methods=['POST'])
def signup():
    if request.method=='POST':
        name=request.json['name']
        id=request.json['id']
        pw=request.json['pw']
        
        db.connect()

        id_exist=db.checkid(id) #id 중복 체크
        
        result={}

        if id_exist==0:
            db.connect_out()
            result['result']=0
        else:
            db.register(name,id,pw)
            db.connect_out()
            result['result']=1

        return result


#로그인
@bp.route("/login",methods=['GET','POST'])
def login():
    #get user name,pw 
    if request.method=='GET':
        db.connect()
    
        id=request.args.get('id')
        
        data=db.get_userdata(id)
        
        
        db.connect_out()

        return data
    
    #로그인
    if request.method=='POST':
        
        id=request.json['id']
        pw=request.json['pw']
        
        db.connect()
        login_jud=db.login(id,pw)
        
        
        result={}
        if login_jud==1: 
            
            basicdata_jud=db.checkbasicdata(id)
            data=db.get_userdata(id)
    
            result['login']="succeed"
            result['jud_basicdata']=basicdata_jud #기초문진 1이면 완료, 0이면 필요
            result['name']=data['name']
            
        else: result['login']="fail"

        db.connect_out()
        return result



#사용자 기초 문진 데이터 받기
@bp.route("/basicdata",methods=['GET'])
def userbasicdata():

    if request.method=='GET':
        db.connect()
    
        id=request.args.get('id')
        
        basicdata_jud=db.checkbasicdata(id) #기초문진 1이면 완료, 0이면 필요
        
        if(basicdata_jud==1):
            data=db.get_userbasicdata(id)
        else:
            data="no data"
        
        db.connect_out()

        return data

#해당 id의 basicdata있는지 없는지 알려주는 api
@bp.route("/judbasicdata",methods=['GET'])
def judbasicdata():
    if request.method=='GET':
        db.connect()
        id=request.args.get('id')
        
        basicdata_jud=db.checkbasicdata(id) #기초문진 1이면 완료, 0이면 필요
        data={}
        
        if(basicdata_jud==1):
            data['jud']=1 #data exist
        else:
            data['jud']=0 #data not exist
        
        db.connect_out()

        return data