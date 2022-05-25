import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask
from api import user_api,diet_api,disease_api,diseasediet_api,level2_api

def createAPP():
    app=Flask(__name__)

    app.register_blueprint(user_api.bp)
    app.register_blueprint(diet_api.bp)
    app.register_blueprint(diseasediet_api.bp)
    app.register_blueprint(level2_api.bp)
    app.register_blueprint(disease_api.bp)
    

    return app


