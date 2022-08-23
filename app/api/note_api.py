import json
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user
from app.models import Note, User
from app.extensions import db 

note_api_bp = Blueprint("note_api", __name__)

@note_api_bp.route('/notes', methods=["GET"])
@jwt_required()
def get_notes():
    user = current_user
    query_result = User.query.filter_by(user_id=user.user_id).first()
    result_dict = [n.dictify_self() for n in query_result.notes]
    print(result_dict)
    return jsonify(result_dict)


@note_api_bp.route('/note', methods=["POST"])
@jwt_required()
def set_note():
    user = current_user
    new_note = Note(request.json["content"], user.user_id)
    db.session.add(new_note)
    db.session.commit()
    response = jsonify({"data": request.json["content"]}) 
    return response, 200
