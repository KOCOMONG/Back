

from flask import Blueprint,request
from db.database import database

bp=Blueprint('update',__name__,url_prefix="/update")
db=database() #database class instance 생성


#기초 문진 데이터 업데이트
@bp.route("/basicdata",methods=['POST'])
def update_basicdata():
    if request.method=='POST':
        id=request.json['id']
        sex=request.json['sex']
        age=request.json['age']
        height=request.json['height']
        weight=request.json['weight']
        event=request.json['event']
        past=request.json['past']
        feminity=request.json['feminity']
        
        db.connect()


        db.update_userbasicdata(id,sex,age,height,weight,event,past,feminity)
        db.connect_out()
        
        result={}
        result['result']=1
        
        return result

#delete from table 
@bp.route("/deletetable",methods=['GET'])
def deletetable():    
    if request.method=='GET':
        tablename=request.args.get('tablename')
        db.connect()
        db.deletetable(tablename)
        db.connect_out()
        return "delete from "+tablename