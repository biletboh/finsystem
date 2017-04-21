from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()


class Client(Base):
    __tablename__ = 'Clients'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    passport_number = Column(String, unique=True)
  
    #Add a property decorator to serialize information from Client model 
    @property
    def serialize(self):
        return {
                'id' : self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email' : self.email,
                'passport_number' : self.passport_number,
                }


class Manager(Base):
    __tablename__ = 'Managers'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
  
    #Add a property decorator to serialize information from Manager model 
    @property
    def serialize(self):
        return {
                'id' : self.id,
                'username': self.username,
                }


engine = create_engine('sqlite:///roles.db')
 

Base.metadata.create_all(engine)

