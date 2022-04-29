

from flask import Flask,request
from database import database




def createAPP():
    app=Flask(__name__)

    db=database() #database class instance 생성


    
    #user
    @app.route("/userlist",methods=['GET','POST'])
    def user():

        #get user name,pw 
        if request.method=='GET':
            db.connect()
        
            id=request.args.get('id')
            
            data=db.get_userdata(id)
            
            
            db.connect_out()

            return data

        #user register
        if request.method=='POST':
            name=request.form['name']
            userid=request.form['id']
            pw=request.form['pw']
            
            db.connect()
            db.register(name,userid,pw)
            db.connect_out()

            return "insert complete"

    #user 기초 문진 data 
    @app.route("/userbasicdata",methods=['GET','PUT'])
    def userbasicdata():

        #get user basic data
        if request.method=='GET':
            db.connect()
        
            id=request.args.get('id')
            
            data=db.get_userbasicdata(id)
            
            
            db.connect_out()

            return data

        #update user basic data 
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