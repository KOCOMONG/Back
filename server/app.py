

from flask import Flask,request
from database import database




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

        
    
    
    
    
        

    return app