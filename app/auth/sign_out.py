from datetime import datetime
from flask import jsonify, Blueprint, request
from flask_jwt_extended import get_jwt, jwt_required, get_current_user
from app.extensions import db
from app.models import Token
from flasgger import swag_from

sign_out_bp = Blueprint('sign_out', __name__)

@sign_out_bp.route('/sign-out', methods=["DELETE"])
@jwt_required()
@swag_from("../../docs/auth/sign-out.yml")
def sign_out():
    token = get_jwt()
    access_token = token["jti"]
    refresh_token = request.json["refresh_token"]
    
    stored_access_token = db.session.query(Token).filter_by(jti=access_token).scalar()
    stored_refresh_token = db.session.query(Token).filter_by(jti=refresh_token).scalar()

    utcnow = datetime.utcnow()
    stored_access_token.is_valid = False
    stored_access_token.last_updated_at = utcnow 
    stored_refresh_token.is_valid = False
    stored_refresh_token.last_updated_at = utcnow 

    db.session.commit()
    
    return jsonify({
        'status': 200, 
        'data': { }, 
        'msg':'Signed out successfully!',
        }), 200

@sign_out_bp.route('/sign-out-all', methods=["DELETE"])
@jwt_required()
@swag_from("../../docs/auth/sign-out-all.yml")
def sign_out_all():
    user = get_current_user()
    tokens = db.session.query(Token).filter_by(user_id=user.user_id)

    for token in tokens: 
        token.is_valid = False
    
    db.session.commit()

    return jsonify({
        'status': 200, 
        'data': { }, 
        'msg':'Successfully signed out from every devices!',
        }), 200

