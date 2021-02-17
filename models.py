import os
from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys
import json


database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
#    db.create_all()


class Project(db.Model):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    kind = Column(String, nullable=True)
    deadline = Column(DateTime, nullable=True)
    word_count = Column(Integer, nullable=True)
    hour_count = Column(Float, nullable=True)
    rate = Column(Float, nullable=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('service.id'), nullable=False)
    person_child = db.relationship("Person", back_populates='services')
    service_child = db.relationship("Service", back_populates='people')

    def __init__(self, name, kind, deadline, word_count, hour_count, rate, person_id, service_id):
        self.name = name
        self.kind = kind
        self.deadline = deadline
        self.word_count = word_count
        self.hour_count = hour_count
        self.rate = rate
        self.person_id = person_id
        self.service_id = service_id

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'kind': self.kind,
            'deadline': self.deadline,
            'word_count': self.word_count,
            'hour_count': self.hour_count,
            'rate': self.rate,
            'person_id': self.person_id,
            'service_id': self.service_id
        }


class Person(db.Model):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    kind = Column(String, nullable=True)
    email = Column(String, nullable=True)
    ratew = Column(Float, nullable=True)
    rateh = Column(Float, nullable=True)
    services = db.relationship("Project", back_populates="person_child")

    def __init__(self, name, kind, email, ratew, rateh):
        self.name = name
        self.kind = kind
        self.email = email
        self.ratew = ratew
        self.rateh = rateh

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())

    def close(self):
        db.session.close()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'kind': self.kind,
            'email': self.email,
            'ratew': self.ratew,
            'rateh': self.rateh
        }


class Service(db.Model):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    source = Column(String, nullable=True)
    destiny = Column(String, nullable=True)
    people = db.relationship("Project", back_populates="service_child")

    def __init__(self, name, source, destiny):
        self.name = name
        self.source = source
        self.destiny = destiny

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())
    
    def close(self):
        db.session.close()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'source': self.source,
            'destiny': self.destiny
        }
