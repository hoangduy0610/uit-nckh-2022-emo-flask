from models.student import Student
from providers.postgres import db
from models.user import User
from datetime import datetime
from models.log import Log

def createLog(student_id, emotion, dominant_emotion, distance, img_path, status):
    log = Log(student_id, emotion, dominant_emotion, distance, img_path, status)
    db.session.add(log)
    db.session.commit()
    return log

def getLogById(id):
    return Log.query.filter_by(id=id, deleted_at=None).first()

def getLogs():
    return Log.query.filter_by(deleted_at=None).all()

def getLogsByStudentId(student_id):
    return Log.query.filter_by(student_id=student_id, deleted_at=None).all()

def getLogsByStudentIdAndStatus(student_id, status):
    return Log.query.filter_by(student_id=student_id, status=status, deleted_at=None).all()

def getLogsByStatus(status):
    return Log.query.filter_by(status=status, deleted_at=None).all()

def updateLog(id, student_id, emotion, dominant_emotion, distance, img_path, status):
    log = getLogById(id)
    if log is None:
        return None
    log.student_id = student_id
    log.emotion = emotion
    log.dominant_emotion = dominant_emotion
    log.distance = distance
    log.img_path = img_path
    log.status = status
    log.updated_at = datetime.now()
    db.session.commit()
    return log

def changeLogStatus(id, status):
    log = getLogById(id)
    if log is None:
        return None
    log.status = status
    log.updated_at = datetime.now()
    db.session.commit()
    return log

def deleteLog(id):
    log = getLogById(id)
    if log is None:
        return None
    log.deleted_at = datetime.now()
    db.session.commit()
    return log

def getLogsByStudentIdAndStatusAndDate(student_id, status, date):
    return Log.query.filter_by(student_id=student_id, status=status, created_at=date, deleted_at=None).all()

def getLogsByStatusAndDate(status, date):
    return Log.query.filter_by(status=status, created_at=date, deleted_at=None).all()

def getLogsByStudentIdAndDate(student_id, date):
    return Log.query.filter_by(student_id=student_id, created_at=date, deleted_at=None).all()

def getLogsByDate(date):
    return Log.query.filter_by(created_at=date, deleted_at=None).all()