# importing libraries
from functools import wraps
import jwt
from flask import jsonify, request

from common.constants import SECRET_KEY

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY, ['HS256'])
            # print(data)
            current_user = {
                "username" : "admin",
                "name" : "admin",
                "email" : "admin@localhost.com"
            }
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated
