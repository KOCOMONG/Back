

from flask import Flask,request
from database import database




def createAPP():
    app=Flask(__name__)

    db=database() #database class instance 생성

    #해당 유저의 계정이 존재하는지 확인
    def judUserExists(userid):
        db.connect()
        
        
        
        
        
        
        db.connect_out()
        
    
    
    #회원가입 
    @app.route("/register",methods=['POST'])
    def register():
        
        username=request.form['name']
        userid=request.form['id']
        userpw=request.form['pw']
        
        db.connect()
        db.register(username,userid,userpw)
        db.connect_out()

        return "insert complete"

    
    
    @app.route("/getUserInformation",methods=['GET'])
    def getUserInformation():
        db.connect()
        username=request.args.get('name')
        information=db.get_user_information(username)
        db.connect_out()

        return information

    return app