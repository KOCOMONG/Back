
import requests

#의료챗봇 api test


#사용자 기본 정보 class
class userlist:

    def __init__(self,url):
        
        self.url=url
        self.endpoint="/userlist"
        
    #회원가입
    def register(self,name,id,pw):
    
        datas={
            'name':name,
            'id':id,
            'pw':pw
        }
        requests.post(self.url+self.endpoint,data=datas)
        print("register "+id+" !!!")


    #해당 id의 data 가져오기
    def set_data(self,id):
        self.data=requests.get(self.url+self.endpoint,params={"id": id}).json() #json 형태로 data 받기

    #해당 id의 name 가져오기
    def get_name(self):
        name=self.data['name']
        return name

    #해당 id의 password 가져오기
    def get_pw(self):
        pw=self.data['pw']
        return pw




#사용자 기초문진 정보 class
class userbasicdata:

    def __init__(self,url):
        
        self.url=url
        self.endpoint="/userbasicdata"

    #해당 id의 기초문진 data update 변경 안되는 값들도 다시 다 적어줘야 함 
    def update(self,id,sex,age,height,weight,event,history,pregnant):
        datas={
            
            'id':id,
            'sex':sex,
            'age':age,
            'height':height,
            'weight':weight,
            'event':event,
            'history':history,
            'pregnant':pregnant
            
        }
        requests.put(self.url+self.endpoint,data=datas)
        print("update "+id+" basic data !!!")

    def set_data(self,id):
        self.data=requests.get(self.url+self.endpoint,params={"id": id}).json() #json 형태로 data 받기 

    def get_sex(self):
        sex=self.data['sex']
        return sex

    def get_age(self):
        age=self.data['age']
        return age

    def get_height(self):
        height=self.data['height']
        return height

    def get_weight(self):
        weight=self.data['weight']
        return weight

    def get_event(self):
        event=self.data['event']
        return event 
    
    def get_history(self):
        history=self.data['history']
        return history

    def get_pregnant(self):
        pregnant=self.data['pregnant']
        return pregnant
