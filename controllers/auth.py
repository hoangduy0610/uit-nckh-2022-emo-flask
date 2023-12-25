from __main__ import app

from flask import jsonify, make_response, request
from services.auth import login_service, register_service

def login_controller():
    # creates dictionary of form data
    auth = request.get_json()
    print(auth['password'])
  
    if not auth or not auth['username'] or not auth['password']:
        # returns 401 if any email or / and password is missing
        return make_response(
            'Missing params',
            400,
            {}
        )
    
    result = login_service(auth['username'], auth['password'])

    return make_response(
        jsonify(result),
        result['code'],
        {}
    )

def register_controller():
    # creates dictionary of form data
    auth = request.get_json()
  
    if not auth or not auth['username'] or not auth['password'] or not auth['name']:
        # returns 401 if any email or / and password is missing
        return make_response(
            'Missing params',
            400,
            {}
        )
    
    result = register_service(auth['username'], auth['password'], auth['name'])

    return make_response(
        jsonify(result),
        result['code'],
        {}
    )
