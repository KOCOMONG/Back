import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Blueprint,request
from database import database
from model.level2.model import lv2_disease_diagnose



bp=Blueprint('level2',__name__,url_prefix='/model')
db=database() #database class instance 생성


#lv2 모델 
@bp.route("/level2",methods=['POST'])
def level2():
    if request.method=='POST':
        id=request.form['id']

        db.connect()

        data=db.get_userbasicdata(id) #해당 id의 기초문진 데이터 가져오기 

        

        sex=data['sex']

        chiefcomplaint=request.form['chiefcomplaint'] #주요증상
        onset=request.form['onset'] #언제부터 증상이 시작되었는지
        location=request.form['location'] #해당부위

        db.update_diseasedata(id,chiefcomplaint,onset,location) #질병 진단 필수 데이터 업데이트

        db.connect_out()


        model=lv2_disease_diagnose()
        model.input(sex,chiefcomplaint,onset,location)
        model.run_model()
        
        result={}
        result['result1']=model.result_1
        result['result2']=model.result_2
        result['result3']=model.result_3

        return result
