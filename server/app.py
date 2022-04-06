

from flask import Flask,Request




def createAPP():
    app=Flask(__name__)



    #회원가입 
    @app.route("/register",methods=['POST'])
    def register():
        
        username=Request.form['name']
        userid=Request.form['id']
        userpw=Request.form['pw']
        




    return app