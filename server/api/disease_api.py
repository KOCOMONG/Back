

from flask import Blueprint,request
from db.database import database

from model.disease.diseasemodel import disease_diagnose



bp=Blueprint('disease',__name__,url_prefix="/model")
db=database() #database class instance 생성


#질병진단
@bp.route("/disease",methods=['post'])
def disease():    
    if request.method=='POST':
        id=request.json['id']
        level2_answer=request.json['level2_answer'] #lv2에서 사용자가 선택한 답안
    
        duration=request.json['duration'] #증상지속
        course=request.json['course'] #증상의 양상
        experience=request.json['experience']
        character=request.json['character']
        factor=request.json['factor'] #어떤 경우에 증상이 더 심해지거나 완화되나?
        associated=request.json['associated']
        drug=request.json['drug']
        social=request.json['social']
        family=request.json['family']
        traumatic=request.json['traumatic']
        

        db.connect()

        data=db.get_userbasicdata(id) #해당 id의 기초문진 데이터 가져오기 

        
        
        height=data['height']
        weight=data['weight']
        age=data['age']
        sex=data['sex']
        event=data['event']
        past=data['past']
        feminity=data['feminity']
        
        data=db.get_diseasedata(id) #해당 id의 diseasedata 가져오기

        chiefcomplaint=data['chiefcomplaint']
        onset=data['onset']
        location=data['location']

        db.connect_out()

        #모델 불러오기
        model=disease_diagnose()
        model.input(level2_answer,height,weight,age,sex,chiefcomplaint,onset,location,duration,course,experience,character,factor,associated,event,drug,social,family,traumatic,past,feminity)
        model.run_model()


        #3개의 질병 정보 넘겨주기
        data_dic={}
        data_dic['name1']=model.result1[0]
        data_dic['percent1']=str(model.result1[1])
        data_dic['synonym1']=model.result1[2]
        data_dic['department1']=model.result1[3]
        data_dic['explain1']=model.result1[4]
        
        data_dic['name2']=model.result2[0]
        data_dic['percent2']=str(model.result2[1])
        data_dic['synonym2']=model.result2[2]
        data_dic['department2']=model.result2[3]
        data_dic['explain2']=model.result2[4]

        data_dic['name3']=model.result3[0]
        data_dic['percent3']=str(model.result3[1])
        data_dic['synonym3']=model.result3[2]
        data_dic['department3']=model.result3[3]
        data_dic['explain3']=model.result3[4]

        return data_dic