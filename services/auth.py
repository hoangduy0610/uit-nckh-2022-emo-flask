from datetime import datetime, timedelta
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt

from common.constants import SECRET_KEY

def login_service(username, password):
    # user = User.query\
    #     .filter_by(email = auth.get('email'))\
    #     .first()
    user = {
        "username" : "admin",
        "name" : "admin",
        "email" : "admin@localhost.com",
        "password" : "admin"
    }

    if not user:
        # returns 401 if user does not exist
        return {
            'status': False,
            'message': 'User does not exist',
            'code': 401
        }
  
    if check_password_hash(user['password'], password) or user['password'] == password:
        # generates the JWT Token
        token = jwt.encode({
            'public_id': '1',
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, SECRET_KEY)
  
        return {
            'status': True,
            'message': 'Successfully logged in',
            'code': 200,
            'token': token
        }
    # returns 403 if password is wrong
    return {
        'status': False,
        'message': 'Wrong credentials',
        'code': 403
    }