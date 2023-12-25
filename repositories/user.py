from providers.postgres import db
from models.user import User
from datetime import datetime

def createNewUser(username, password, name):
    newUser = User(username, password, name)
    db.session.add(newUser)
    db.session.commit()
    return newUser

def getUserByUsername(username):
    return User.query.filter_by(username=username, deleted_at=None).first()

def getUserById(id):
    return User.query.filter_by(id=id, deleted_at=None).first()

def getAllUsers():
    return User.query.filter_by(deleted_at=None).all()

def updateUser(id, username, password, name):
    user = getUserById(id)
    if (user is None):
        return None
    user.username = username
    user.password = password
    user.name = name
    user.updated_at = datetime.now()
    db.session.commit()
    return user

def deleteUser(id):
    user = getUserById(id)
    if (user is None):
        return None
    user.deleted_at = datetime.now()
    db.session.commit()
    return user

def restoreUser(id):
    user = getUserById(id)
    user.deleted_at = None
    db.session.commit()
    return user