from __main__ import app

from controllers.log import query_log_controller
from decorators.auth import token_required

# route for query logs in params
@app.route('/logs', methods=['GET'])
@token_required
def query_log_route(current_user):
    return query_log_controller()