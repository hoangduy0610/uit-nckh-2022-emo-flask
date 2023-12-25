

from datetime import datetime
import os
import shutil
from deepface import DeepFace
from flask import jsonify
from ML_Model.handle import face_match
from models.log import StatusEnum
from repositories.log import changeLogStatus, createLog
from repositories.student import getStudentById

def image_process_service(img_path, data_path):    
    result = face_match(img_path, data_path)
    
    f_path=img_path
    student_id=result[0]
    conf=StatusEnum.SUCCESS
    id=None
    name="Unknown"

    if result[1] > 1:
        f_path=None
        student_id=None
        conf=StatusEnum.FAILED

    elif result[1] > 0.7:
        conf=StatusEnum.PENDING

    if student_id is not None:
        std = getStudentById(student_id)
        if std is not None:
            name=std.name

        face_analysis = DeepFace.analyze(img_path = img_path, actions=['emotion'], silent=True)
        # print('Face matched with: ',result[0], 'With distance: ',result[1])
        # print(face_analysis[0]['emotion'])
        # print(face_analysis[0]['dominant_emotion'])
    
    id=createLog(student_id, face_analysis[0]['emotion'], face_analysis[0]['dominant_emotion'], result[1], img_path, conf)

    return jsonify(
        id=id.id,
        student_id=student_id,
        name=name,
        img_path=f_path,
        status=conf,
        distance=result[1],
        emotion=face_analysis[0]['emotion'],
        dominant_emotion=face_analysis[0]['dominant_emotion']
    )


def confirm_image_service(id):
    # filename = os.path.basename(img_path)
    # destination_path = os.path.join('public/faces', filename)
    # shutil.move(img_path, destination_path)
    log = changeLogStatus(id, StatusEnum.SUCCESS)
    return {
        'code':200,
        'message':'Image confirmed',
        'result':True,
        'img_path':log.img_path,
        'status':StatusEnum.SUCCESS
    }