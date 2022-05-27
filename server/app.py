
from flask import Flask
from api import user_api,diet_api,diseasediet_api,level2_api,disease_api

def createAPP():
    app=Flask(__name__)

    app.register_blueprint(user_api.bp)
    app.register_blueprint(diet_api.bp)
    app.register_blueprint(diseasediet_api.bp)
    app.register_blueprint(level2_api.bp)
    app.register_blueprint(disease_api.bp)
    

    return app


