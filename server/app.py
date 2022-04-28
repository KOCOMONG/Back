
from flask import Flask,request
from database import database




def createAPP():
    app=Flask(__name__)

    db=database() #database class instance 생성


    
    #회원가입 
    @app.route("/register",methods=['POST'])
    def register():
        
        name=request.form['name']
        userid=request.form['id']
        pw=request.form['pw']
        
        db.connect()
        db.register(name,userid,pw)
        db.connect_out()

        return "insert complete"

    #기초 문진 data 저장
    @app.route("/updateUserBasicPaperweightData",methods=['PUT'])
    def updateUserBasicPaperweightData():
        
        name=request.form['name']
        sex=request.form['sex']
        age=request.form['age']
        height=request.form['height']
        weight=request.form['weight']
        event=request.form['event']
        history=request.form['history']
        pregnant=request.form['pregnant']
        
        db.connect()
        db.update_basic_paperweight(name,sex,age,height,weight,event,history,pregnant)
        db.connect_out()
        
        return "update complete"
    
    
    
    
    #기초 문진 data 받기 
    @app.route("/getUserBasicPaperweightData",methods=['GET'])
    def getUserBasicPaperweightData():
        db.connect()
        
        name=request.form['name']
        
        data=db.get_basic_papaerweight(name)
        
        
        db.connect_out()

        return data

    return app