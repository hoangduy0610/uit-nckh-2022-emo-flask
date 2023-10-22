from __main__ import app

from flask import request
from services.image import image_process_service

def image_process_controller():
    print("render process request")
    data = request.files["img"]
    data.save("img.jpg")

    return image_process_service('img.jpg', 'ML_Model/data.pt')