from __main__ import app

from flask import jsonify, make_response, request
from services.auth import login_service

def login_controller():
    # creates dictionary of form data
    auth = request.get_json()
    print(auth['password'])
  
    if not auth or not auth['email'] or not auth['password']:
        # returns 401 if any email or / and password is missing
        return make_response(
            'Missing params',
            401,
            {}
        )
    
    result = login_service(auth['email'], auth['password'])

    return make_response(
        jsonify(result),
        result['code'],
        {}
    )
