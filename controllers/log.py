from __main__ import app

from flask import jsonify, make_response, request
from services.log import query_logs

def query_log_controller():
    params = request.args.to_dict()
    result = query_logs(params)

    return make_response(
        jsonify(result),
        result['code'],
        {}
    )