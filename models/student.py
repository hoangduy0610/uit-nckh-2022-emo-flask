from datetime import datetime
import json
from providers.postgres import db

from providers.serializer import Serializer

class Student(db.Model, Serializer):
    __tablename__ = 'students'

    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime())

    def __init__(self, id, name, age ):
        self.id = id
        self.name = name
        self.age = age
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<Student {self.name}>"
    
    def serialize(self, has_log=False):
        d = Serializer.serialize(self)
        if has_log:
            d['logs'] = [log.serialize() for log in self.logs]
        else:
            d['logs'] = []
        return d