

from flask import Flask,request
from database import database

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from model.diet.diet import Diet
from model.level2.model import lv2_disease_diagnose 
from model.disease.diseasemodel import disease_diagnose 

from ast import literal_eval


def createAPP():
    app=Flask(__name__)

    db=database() #database class instance 생성


    
    #사용자 기본 데이터
    @app.route("/userlist",methods=['GET','POST'])
    def user():

        #get user name,pw 
        if request.method=='GET':
            db.connect()
        
            id=request.args.get('id')
            
            data=db.get_userdata(id)
            
            
            db.connect_out()

            return data

        #회원가입
        if request.method=='POST':
            name=request.form['name']
            id=request.form['id']
            pw=request.form['pw']
            
            db.connect()

            id_exist=db.checkid(id) #id 중복 체크
            
            result={}

            if id_exist==0:
                db.connect_out()
                result['result']="overlap"
            else:
                db.register(name,id,pw)
                db.connect_out()
                result['result']="complete"
            
            
            

            return result

    #사용자 기초 문진 데이터 
    @app.route("/userbasicdata",methods=['GET','PUT'])
    def userbasicdata():

        #get user basic data
        if request.method=='GET':
            db.connect()
        
            id=request.args.get('id')
            
            data=db.get_userbasicdata(id)
            
            
            db.connect_out()

            return data

        #기초 문진 데이터 업데이트
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

        
    #식단조절
    @app.route("/diet",methods=['POST'])
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

    #의약데이터
    @app.route("/medicine",methods=['GET'])
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
    
    #lv2 모델 
    @app.route("/level2",methods=['POST'])
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

    #질병진단
    @app.route("/disease",methods=['post'])
    def disease():    
        if request.method=='POST':
            id=request.form['id']
            level2_answer=request.form['level2_answer'] #lv2에서 사용자가 선택한 답안
        
            duration=request.form['duration'] #증상지속
            course=request.form['course'] #증상의 양상
            experience=request.form['experience']
            character=request.form['character']
            factor=request.form['factor'] #어떤 경우에 증상이 더 심해지거나 완화되나?
            associated=request.form['associated']
            drug=request.form['drug']
            social=request.form['social']
            family=request.form['family']
            traumatic=request.form['traumatic']
            

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
            data_dic['percent1']=model.result1[1]
            data_dic['synonym1']=model.result1[2]
            data_dic['department1']=model.result1[3]
            data_dic['explain1']=model.result1[4]
            
            data_dic['name2']=model.result2[0]
            data_dic['percent2']=model.result2[1]
            data_dic['synonym2']=model.result2[2]
            data_dic['department2']=model.result2[3]
            data_dic['explain2']=model.result2[4]

            data_dic['name3']=model.result3[0]
            data_dic['percen3']=model.result3[1]
            data_dic['synonym3']=model.result3[2]
            data_dic['department3']=model.result3[3]
            data_dic['explain3']=model.result3[4]

            return data_dic


    #delete from table 
    @app.route("/deletetable",methods=['GET'])
    def deletetable():    
        if request.method=='GET':
            tablename=request.args.get('tablename')
            db.connect()
            db.deletetable(tablename)
            db.connect_out()
            return "delete from "+tablename



    return app