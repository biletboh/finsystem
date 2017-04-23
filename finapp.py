from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import config


#  Add dababase
db = SQLAlchemy()


#  Application Factory
def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(configuration)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


#  Create application
app = create_app(config)

#  Create Restful instance
api = Api(app)

import views, models

