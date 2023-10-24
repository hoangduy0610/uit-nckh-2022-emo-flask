from datetime import datetime
from providers.postgres import db

from providers.serializer import Serializer

class Student(db.Model, Serializer):
    __tablename__ = 'students'

    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime())

    def __init__(self, id, name ):
        self.id = id
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<Student {self.name}>"
    
    def serialize(self):
        d = Serializer.serialize(self)
        return d