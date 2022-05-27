

from flask import Blueprint,request
from db.database import database
from ast import literal_eval

from model.diseasediet.chol_model import choldiet
from model.diseasediet.diabetes_model import diabetesdiet
from model.diseasediet.salt_model import saltdiet



bp=Blueprint('diseasediet',__name__,url_prefix='/model')
db=database() #database class instance 생성


#질병 식단 
@bp.route("/diseasediet",methods=['POST'])
def diseasediet():
    if request.method=='POST':
        id=request.form['id'] #id
        classification=request.form['classification'] #사용할 모델 종류
        practice=int(request.form['practice']) #활동량 

        db.connect()

        data=db.get_userbasicdata(id) #해당 id의 기초문진 데이터 가져오기 

        db.connect_out()

        height=data['height']
        weight=data['weight']
        age=data['age']
        sex=data['sex']

        if classification=='chol':
            model=choldiet()
        elif classification=='diabetes':
            model=diabetesdiet()
        else:
            model=saltdiet()

        model.input(height,weight,age,sex,practice)
        model.rec()

        result_str=model.result   
        
        result_tuple=literal_eval(result_str) #튜플형 문자열을 튜플로 형변환

        result={}
        result['rice']=result_tuple[0] #밥
        result['soup']=result_tuple[1] #국
        result['sidedish']=result_tuple[2] #반찬
        
        return result