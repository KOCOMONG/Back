import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Blueprint,request
from database.database import database

bp=Blueprint('medicine',__name__,url_prefix="/model")
db=database() #database class instance 생성


#의약데이터
@bp.route("/medicine",methods=['GET'])
def medicine():
    if request.method=='GET':
        name=request.args.get('name')
        tool=request.args.get('tool') #무슨 정보 받을 건지 
        db.connect()

        if tool=="keep":
            data=db.find_keep(name)
        elif tool=="effect":
            data=db.find_effect(name)
        elif tool=="useage":
            data=db.find_useage(name)
        elif tool=="caution":
            data=db.find_caution(name)
        else: #information
            data=db.find_information(name)


        db.connect_out()

        data_dic={}
        data_dic['data']=data

        return data_dic