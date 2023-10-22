from __main__ import app

from controllers.auth import login_controller
from decorators.auth import token_required

@app.route('/jwt-check', methods =['GET'])
@token_required
def jwt_check(current_user):
    print(current_user)
    return "SUCCESS"

# route for logging user in
@app.route('/login', methods =['POST'])
def login_route():
    return login_controller()