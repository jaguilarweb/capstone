import os
from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json


database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    

class Project(db.Model):

    id = Column(Integer, primary_key=True)
    kind = Column(String)
    delivery = Column(DateTime)
    words = Column(Integer)
    hour = Column(Float)
    rate = Column(Float)
    person_id = Column(Integer, ForeignKey('person.id'))
    service_id = Column(Integer, ForeignKey('service.id'))
    person_child = db.relationship("Person", back_populates='services')
    service_child = db.relationship("Service", back_populates='people')


class Person(db.Model):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    kind = Column(String)
    email = Column(String)
    ratew = Column(Float)
    rateh = Column(Float)
    
    services = db.relationship("Projects", back_populates="person_child")
    
    
    
class Service(db.Model):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    source = Column(String)
    destiny = Column(String)
    
    people = db.relationship("Projects", back_populates="service_child")