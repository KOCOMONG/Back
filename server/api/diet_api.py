import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Blueprint,request
from database.database import database
from ast import literal_eval

from model.diet.diet import Diet


bp=Blueprint('diet',__name__,url_prefix="/model")
db=database() #database class instance 생성


#식단조절
@bp.route("/diet",methods=['POST'])
def diet():
    if request.method=='POST':

        dietmodel=Diet() #식단추천모델 객체 생성

        id=request.form['id']

        db.connect()

        data=db.get_userbasicdata(id) #해당 id의 기초문진 데이터 가져오기 

        db.connect_out()

        height=data['height']
        weight=data['weight']
        age=data['age']
        sex=data['sex']
        want_weight=float(request.form['want_weight'])
        want_time=int(request.form['want_time'])
        practice=int(request.form['practice'])

        dietmodel.input(height,weight,age,sex,want_weight,want_time,practice)
        dietmodel.rec()

        result_str=dietmodel.result   
        
        result_tuple=literal_eval(result_str) #튜플형 문자열을 튜플로 형변환

        result={}
        result['rice']=result_tuple[0] #밥
        result['soup']=result_tuple[1] #국
        result['sidedish']=result_tuple[2] #반찬
        
        return result