from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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


import views, models

