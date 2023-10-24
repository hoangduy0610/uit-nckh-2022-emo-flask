from providers.postgres import db
from datetime import datetime

from providers.serializer import Serializer

class User(db.Model, Serializer):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    name = db.Column(db.String())
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime())

    def __init__(self, username, password, name ):
        self.username = username
        self.password = password
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.deleted_at = None

    def __repr__(self):
        return f"<User {self.name}>"
    
    def serialize(self):
        d = Serializer.serialize(self)
        del d['password']
        return d