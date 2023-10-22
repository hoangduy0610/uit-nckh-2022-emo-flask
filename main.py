# importing libraries
from datetime import datetime, timedelta
from functools import wraps
from facenet_pytorch import MTCNN, InceptionResnetV1
import jwt
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image
from deepface import DeepFace
from flask import Flask, jsonify, make_response, render_template, request
from flask_cors import CORS, cross_origin
from  werkzeug.security import generate_password_hash, check_password_hash

mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20) # initializing mtcnn for face detection
resnet = InceptionResnetV1(pretrained='vggface2').eval() # initializing resnet for face img to embeding conversion

def face_match(img_path, data_path): # img_path= location of photo, data_path= location of data.pt 
    # getting embedding matrix of the given img
    img = Image.open(img_path)
    face, prob = mtcnn(img, return_prob=True) # returns cropped face and probability
    emb = resnet(face.unsqueeze(0)).detach() # detech is to make required gradient false
    
    saved_data = torch.load(data_path) # loading data.pt file
    embedding_list = saved_data[0] # getting embedding data
    name_list = saved_data[1] # getting list of names
    dist_list = [] # list of matched distances, minimum distance is used to identify the person
    
    for idx, emb_db in enumerate(embedding_list):
        dist = torch.dist(emb, emb_db).item()
        dist_list.append(dist)
        
    idx_min = dist_list.index(min(dist_list))
    return (name_list[idx_min], min(dist_list))

# Initializing flask application
app = Flask(__name__)
cors = CORS(app)

app.config['SECRET_KEY'] = 'JWT_SECRET_KEY'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = {
                "username" : "admin",
                "name" : "admin",
                "email" : "admin@localhost.com"
            }
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated

@app.route("/health-check")
def main():
    return """
        Application is working
    """

@app.route('/jwt-check', methods =['GET'])
@token_required
def jwt_check(current_user):
    print(current_user)
    return "SUCCESS"

# route for logging user in
@app.route('/login', methods =['POST'])
def login():
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
  
    # user = User.query\
    #     .filter_by(email = auth.get('email'))\
    #     .first()
    user = {
        "username" : "admin",
        "name" : "admin",
        "email" : "admin@localhost.com",
        "password" : "admin"
    }

    if not user:
        # returns 401 if user does not exist
        return make_response(
            'User not exist',
            401,
            {}
        )
  
    if check_password_hash(user['password'], auth['password']) or user['password'] == auth['password']:
        # generates the JWT Token
        token = jwt.encode({
            'public_id': '1',
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, app.config['SECRET_KEY'])
  
        return make_response(jsonify({'token' : token}), 200)
    # returns 403 if password is wrong
    return make_response(
        'Wrong password',
        403,
        {}
    )

# Process images
@app.route("/process", methods=["POST"])
def processReq():
    print("render process request")
    data = request.files["img"]
    data.save("img.jpg")

    result = face_match('img.jpg', 'data.pt')
    face_analysis = DeepFace.analyze(img_path = "2.jpg", actions=['emotion'], silent=True)

    print('Face matched with: ',result[0], 'With distance: ',result[1])
    print(face_analysis[0]['emotion'])
    print(face_analysis[0]['dominant_emotion'])
    # print(face_analysis["dominant_emotion"])

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8933, debug=True)