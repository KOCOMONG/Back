

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
            result['result']="overlap"
        else:
            db.register(name,id,pw)
            db.connect_out()
            result['result']="complete"

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
        db.connect_out()
        result={}
        if login_jud==1: result['login']="succeed"
        else: result['login']="fail"

        return result



#사용자 기초 문진 데이터 받기
@bp.route("/basicdata",methods=['GET'])
def userbasicdata():

    if request.method=='GET':
        db.connect()
    
        id=request.args.get('id')
        
        data=db.get_userbasicdata(id)
        
        
        db.connect_out()

        return data

    