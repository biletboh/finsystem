from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required


Base = declarative_base()

class Role(Base, RoleMixin):
    __tablename__ = 'Roles'

    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))


class BaseClient(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String, unique=True)
    passport_number = Column(String(255), unique=True)
  
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

    password = Column(String(255))
    balance = Column(Integer)
    
    #Add a property decorator to serialize information from Client model 
    @property
    def serialize(self):
        return {
                'balance' : self.balance,
                }


class ApprovalList(BaseClient):
    __tablename__ = 'Approval'

    approved = Column(Boolean, default=False) 

    #Add a property decorator to serialize information from Client model 
    @property
    def serialize(self):
        return {
                'approved' : self.approved,
                }


class Manager(Base):
    __tablename__ = 'Managers'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
  
    #Add a property decorator to serialize information from Manager model 
    @property
    def serialize(self):
        return {
                'id' : self.id,
                'username': self.username,
                }


engine = create_engine('sqlite:///roles.db')
 

Base.metadata.create_all(engine)

