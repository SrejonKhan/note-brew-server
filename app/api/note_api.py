import json
from flask import Blueprint, jsonify, request
from app.middleware import token_required
from app.models import Note
from app.extensions import db 

note_api_bp = Blueprint("note_api", __name__)

@note_api_bp.route('/notes', methods=["GET"])
@token_required
def get_notes(current_user):
    query_result = Note.query.all()
    result_dict = [n.serialize() for n in query_result]
    return jsonify(result_dict)


@note_api_bp.route('/note', methods=["POST"])
def set_note():
    data = json.loads(request.data)
    
    new_note = Note(data["content"], "s4sdh36jd")
    db.session.add(new_note)
    db.session.commit()
    return request.data, 200



# @note_api_bp.route('/note-details/<id>')
# def get_details(id):
#     result = Note.query.filter_by(id=id).first()
#     Note.query.filter(Note.id == id).first()
     
#     # if result:  
    