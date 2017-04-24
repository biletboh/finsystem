from passlib.apps import custom_app_context as pwd_context
from flask_security.utils import encrypt_password
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from finapp import db


roles_managers = db.Table(
    'roles_managers',
    db.Column('manager_id', db.Integer(), db.ForeignKey('manager.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


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


class Client(BaseClient, UserMixin):
    __tablename__ = 'Clients'
    
    active = db.Column(db.Boolean())
    password = db.Column(db.String(255))
    balance = db.Column(db.Integer)
    
    #Add a property decorator to serialize information from Client model 
    @property
    def serialize(self):
        return {
                'balance': self.balance,
                'active': self.active
                }
    
    def __str__(self):
        return self.email


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

    def __str__(self):
        return self.email


class Manager(db.Model, UserMixin):
    __tablename__ = 'manager'

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean(), default=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    roles = db.relationship('Role', secondary=roles_managers, 
                        backref=db.backref('managers', lazy='dynamic'))

    def __str__(self):
        return self.email

    #Add a property decorator to serialize information from Manager model 
    @property
    def serialize(self):
        return {
                'id' : self.id,
                'username': self.username,
                'email': self.email,
                }


db.create_all()
db.session.commit()

