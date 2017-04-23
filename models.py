from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from finapp import db

class Role(db.Model, RoleMixin):
    __tablename__ = 'Roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class BaseClient(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String, unique=True)
    passport_number = db.Column(db.String(255), unique=True)
  
    #Add a property decorator to serialize information from Client model 
    @property
    def serialize(self):
        return {
                'id' : self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email' : self.email,
                'passport_number' : self.passport_number,
                'balance' : self.balance,
                }


class Client(BaseClient):
    __tablename__ = 'Clients'

    password = db.Column(db.String(255))
    balance = db.Column(db.Integer)
    
    #Add a property decorator to serialize information from Client model 
    @property
    def serialize(self):
        return {
                'balance' : self.balance,
                }


class ApprovalList(BaseClient):
    __tablename__ = 'Approval'

    approved = db.Column(db.Boolean, default=False) 

    #Add a property decorator to serialize information from Client model 
    @property
    def serialize(self):
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email' : self.email,
                'passport_number' : self.passport_number,
                'approved' : self.approved,
                }


class Manager(db.Model):
    __tablename__ = 'Managers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
  
    #Add a property decorator to serialize information from Manager model 
    @property
    def serialize(self):
        return {
                'id' : self.id,
                'username': self.username,
                }

