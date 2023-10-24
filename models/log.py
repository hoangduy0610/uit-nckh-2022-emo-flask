
from datetime import datetime
from providers.postgres import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, insert 

from providers.serializer import Serializer
from models.student import Student

import enum
from sqlalchemy import Integer, Enum

class StatusEnum(enum.IntEnum):
    FAILED = -1
    PENDING = 0
    SUCCESS = 1

class Log(db.Model, Serializer):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(), ForeignKey('students.id', ondelete='CASCADE'))
    student = relationship(Student, backref="logs")
    emotion = db.Column(JSONB)
    dominant_emotion = db.Column(db.String())
    distance = db.Column(db.Float())
    img_path = db.Column(db.String())
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime())

    def __init__(self, student_id, emotion, dominant_emotion, distance, img_path, status ):
        self.student_id = student_id
        self.emotion = emotion
        self.dominant_emotion = dominant_emotion
        self.distance = distance
        self.img_path = img_path
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<Log {self.name}>"
    
    def serialize(self):
        d = Serializer.serialize(self)
        return d