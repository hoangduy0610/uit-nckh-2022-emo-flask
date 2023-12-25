from __main__ import app

from flask import jsonify, make_response, request
from common.utils import generate_random_image_path
from services.image import confirm_image_service, image_process_service

def image_process_controller():
    print("render process request")
    data = request.files["img"]
    f_name = generate_random_image_path()
    data.save(f_name)

    return image_process_service(f_name, 'ML_Model/data.pt')

def confirm_image_controller():
    body = request.get_json()
    f_name = body['id']
    result = confirm_image_service(f_name)

    return make_response(
        jsonify(result),
        result['code'],
        {}
    )