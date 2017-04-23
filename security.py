from flask_security import Security, SQLAlchemyUserDatastore
from finapp import app, db
from models import Manager, Role


#  Set up Flask-security
user_datastore = SQLAlchemyUserDatastore(db, Manager, Role)
security = Security(app, user_datastore)

