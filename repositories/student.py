from models.student import Student
from providers.postgres import db
from models.user import User
from datetime import datetime

def getAllStudents():
    return Student.query.filter_by(deleted_at=None).all()

def getStudentById(id):
    return Student.query.filter_by(id=id, deleted_at=None).first()

def createNewStudent(id, name):
    newStudent = Student(id, name)
    db.session.add(newStudent)
    db.session.commit()
    return newStudent

def updateStudent(id, name):
    student = getStudentById(id)
    if (student is None):
        return None
    student.name = name
    student.updated_at = datetime.now()
    db.session.commit()
    return student

def deleteStudent(id):
    student = getStudentById(id)
    if (student is None):
        return None
    student.deleted_at = datetime.now()
    db.session.commit()
    return student

def restoreStudent(id):
    student = getStudentById(id)
    student.deleted_at = None
    db.session.commit()
    return student
