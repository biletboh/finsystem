from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_admin import Admin
import config



#  Create application
app = Flask(__name__)
app.config.from_object(config)


#  Add dababase
db = SQLAlchemy(app)


#  Create Restful instance
api = Api(app)


import views, models, admin, security

