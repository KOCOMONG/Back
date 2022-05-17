

from flask import Flask,request
from database import database
from model.diet import diet
from model.diet.diet import Diet
from ast import literal_eval


def createAPP():
    app=Flask(__name__)

    db=database() #database class instance 생성


    
    #사용자 기본 데이터
    @app.route("/userlist",methods=['GET','POST'])
    def user():

        #get user name,pw 
        if request.method=='GET':
            db.connect()
        
            id=request.args.get('id')
            
            data=db.get_userdata(id)
            
            
            db.connect_out()

            return data

        #회원가입
        if request.method=='POST':
            name=request.form['name']
            id=request.form['id']
            pw=request.form['pw']
            
            db.connect()

            id_exist=db.checkid(id) #id 중복 체크
            
            if id_exist==1:
                db.connect_out()
                return "exists same id"
            else:
                db.register(name,id,pw)
                db.connect_out()

            
            

            return "insert complete"

    #사용자 기초 문진 데이터 
    @app.route("/userbasicdata",methods=['GET','PUT'])
    def userbasicdata():

        #get user basic data
        if request.method=='GET':
            db.connect()
        
            id=request.args.get('id')
            
            data=db.get_userbasicdata(id)
            
            
            db.connect_out()

            return data

        #기초 문진 데이터 업데이트
        if request.method=='PUT':
            id=request.form['id']
            sex=request.form['sex']
            age=request.form['age']
            height=request.form['height']
            weight=request.form['weight']
            event=request.form['event']
            history=request.form['history']
            pregnant=request.form['pregnant']
            
            db.connect()


            db.update_userbasicdata(id,sex,age,height,weight,event,history,pregnant)
            db.connect_out()
            
            return "update complete"

        
    #식단조절
    @app.route("/diet",methods=['GET'])
    def diet():
        if request.method=='GET':

            dietmodel=Diet() #식단추천모델 객체 생성

            id=request.args.get('id')

            db.connect()

            data=db.get_userbasicdata(id) #해당 id의 기초문진 데이터 가져오기 

            db.connect_out()

            height=data['height']
            weight=data['weight']
            age=data['age']
            sex=data['sex']
            want_weight=float(request.args.get('want_weight'))
            want_time=int(request.args.get('want_time'))
            practice=int(request.args.get('practice'))

            dietmodel.input(height,weight,age,sex,want_weight,want_time,practice)
            dietmodel.rec()

            result_str=dietmodel.result   
            
            result_tuple=literal_eval(result_str) #튜플형 문자열을 튜플로 형변환

            result={}
            result['rice']=result_tuple[0] #밥
            result['soup']=result_tuple[1] #국
            result['sidedish']=result_tuple[2] #반찬
            
            return result

    
    
        

    return app