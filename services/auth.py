from datetime import datetime, timedelta
from flask import json, jsonify
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt

from common.constants import SECRET_KEY
from repositories.user import createNewUser, getUserByUsername

def login_service(username, password):
    # user = User.query\
    #     .filter_by(email = auth.get('email'))\
    #     .first()
    user = getUserByUsername(username)

    if not user:
        # returns 401 if user does not exist
        return {
            'status': False,
            'message': 'User does not exist',
            'code': 401
        }
  
    if check_password_hash(user.password, password):
        # generates the JWT Token
        token = jwt.encode({
            'public_id': '1',
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, SECRET_KEY)
  
        return {
            'status': True,
            'message': 'Successfully logged in',
            'code': 200,
            'token': token,
            'user': user.serialize()
        }
    # returns 403 if password is wrong
    return {
        'status': False,
        'message': 'Wrong credentials',
        'code': 403
    }

def register_service(username, password, name):
    user = getUserByUsername(username)

    if user:
        # returns 400 if user exist
        return {
            'status': False,
            'message': 'User already exist',
            'code': 400
        }
  
    user = createNewUser(username, generate_password_hash(password, method='scrypt'), name)
    return {
        'status': True,
        'message': 'Successfully registered',
        'code': 200,
        'data': user.serialize()
    }