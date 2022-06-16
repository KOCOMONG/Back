

from flask import Blueprint,request
from db.database import database

bp=Blueprint('medicine',__name__,url_prefix="/model")
db=database() #database class instance 생성


#의약데이터
@bp.route("/medicine",methods=['GET'])
def medicine():
    if request.method=='GET':
        name=request.args.get('name')
        tool=request.args.get('tool') #무슨 정보 받을 건지 
        
        data_dic={}
        
        db.connect()

        if db.jud_medicine(name)==0: #해당 의약 데이터 없음
            data_dic['data']="no data"
        else:
        
            if tool=="keep":
                data=db.find_keep(name)
            elif tool=="effect":
                data=db.find_effect(name)
            elif tool=="usage":
                data=db.find_useage(name)
            elif tool=="caution":
                data=db.find_caution(name)
            else: #information
                data=db.find_information(name)
                
            data_dic['data']=data

        db.connect_out()

        
        

        return data_dic