

from deepface import DeepFace
from flask import jsonify
from ML_Model.handle import face_match

def image_process_service(img_path, data_path):    
    result = face_match(img_path, data_path)
    face_analysis = DeepFace.analyze(img_path = img_path, actions=['emotion'], silent=True)

    print('Face matched with: ',result[0], 'With distance: ',result[1])
    print(face_analysis[0]['emotion'])
    print(face_analysis[0]['dominant_emotion'])

    if result[1] > 0.8:
        return jsonify(
            name="Unknown",
            emotion=None,
            dominant_emotion=None
        )

    return jsonify(
        name=result[0],
        emotion=face_analysis[0]['emotion'],
        dominant_emotion=face_analysis[0]['dominant_emotion']
    )