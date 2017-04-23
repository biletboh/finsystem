from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#  Create application
app = Flask(__name__)


#  Configuration of application
app.config.update(dict(
                    DEBUG=True,
                    SECRET_KEY='development key',
                    WTF_CSRF_SECRET_KEY='secret csrf key',
                    SQLALCHEMY_DATABASE_URI='sqlite:///roles.db',
                    SQLALCHEMY_TRACK_MODIFICATIONS=False
                    ))

#  Add dababase
db = SQLAlchemy(app)


import views, models

