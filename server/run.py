
from api.app import createAPP
from config import server_port

app=createAPP()

if __name__=='__main__':
    app.run(host='0.0.0.0',port=server_port)   