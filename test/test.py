from tableclass import userlist,userbasicdata


data=userlist("http://192.168.0.140:8080")
data.register("cheol","jc","1111")
data.set_data("jc")

print("user name = "+data.get_name())


