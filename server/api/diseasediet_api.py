

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
        id=request.json['id'] #id
        
        #data classification 시작 
        db.connect()
        
        basicdata=db.get_userbasicdata(id)
        userpast=basicdata['past']
        
        
        
        if  userpast=="동맥경화" or "고지혈증" or "심근경색":
            classification='chol' #사용할 모델 종류
        elif userpast == "당뇨병성 신종" or "당뇨병성 망막병증" or "말초신경병증" or "동맥경화증" or "당뇨성마비":
            classification='diabetes' #사용할 모델 종류
        elif userpast == "고혈압" or "고혈압으로 인한 심장병" or "만성 신장병" or "뇌경색" or "위암" or "백의 고혈압" or "본태성 고혈압" or "임신성 고혈압" or "폐경에 의한 고혈압":
            classification='salt' #사용할 모델 종류
        else:
            classification="salt" 
        
        
        practice=int(request.json['practice']) #활동량 

        

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