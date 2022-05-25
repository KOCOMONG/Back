import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Blueprint,request
from database.database import database

bp=Blueprint('update',__name__,url_prefix="/update")
db=database() #database class instance 생성


#기초 문진 데이터 업데이트
@bp.route("/basicdata",methods=['PUT'])
def update_basicdata():
    if request.method=='PUT':
        id=request.form['id']
        sex=request.form['sex']
        age=request.form['age']
        height=request.form['height']
        weight=request.form['weight']
        event=request.form['event']
        past=request.form['past']
        feminity=request.form['feminity']
        
        db.connect()


        db.update_userbasicdata(id,sex,age,height,weight,event,past,feminity)
        db.connect_out()
        
        result={}
        result['result']="complete"
        
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