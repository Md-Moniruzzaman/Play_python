import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_ref = db.collection('users_2')

userApi = Blueprint('userApi', __name__)

@userApi.route('/add', methods = ['POST'])
def create():
    try:
        id = uuid.uuid4()
        user_ref.document(id.hex).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An Error occured: {e}'
    
@userApi.route('/list', methods = ['GET'])
def read():
    try:
        all_user = [doc.to_dict() for doc in user_ref.stream()]
        return jsonify(all_user), 200
    except Exception as e:
        return f'An Error occured: {e}'
    

@userApi.route('/update', methods = ['POST'])
def update():
    try:
        docId = request.get_data

        user_ref.document(id.hex).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An Error occured: {e}'