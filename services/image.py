

from datetime import datetime
import os
import shutil
from deepface import DeepFace
from flask import jsonify
from ML_Model.handle import face_match

def image_process_service(img_path, data_path):    
    result = face_match(img_path, data_path)
    face_analysis = DeepFace.analyze(img_path = img_path, actions=['emotion'], silent=True)

    print('Face matched with: ',result[0], 'With distance: ',result[1])
    print(face_analysis[0]['emotion'])
    print(face_analysis[0]['dominant_emotion'])

    f_path=img_path
    id=result[0]
    conf=1

    if result[1] > 1:
        f_path=None
        id=None

    elif result[1] > 0.7:
        conf=0

    return jsonify(
        id=id,
        img_path=f_path,
        conf=conf,
        distance=result[1],
        emotion=face_analysis[0]['emotion'],
        dominant_emotion=face_analysis[0]['dominant_emotion']
    )


def confirm_image_service(img_path):
    filename = os.path.basename(img_path)
    destination_path = os.path.join('public/faces', filename)
    shutil.move(img_path, destination_path)
    return {
        'code':200,
        'message':'Image confirmed',
        'result':True,
        'data':destination_path
    }