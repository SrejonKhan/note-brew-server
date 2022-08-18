from datetime import datetime, timedelta
from urllib import response
from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, get_jti
from werkzeug.security import check_password_hash
from app.models import Token, User
from app.extensions import db
from flasgger import swag_from

sign_in_bp = Blueprint('sign_in', __name__)

@sign_in_bp.route('/sign-in', methods=["POST"])
@swag_from("../../docs/auth/sign-in.yml")
def sign_in():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({
            'status': 400, 
            'data':None, 
            'msg':'User details not provided!',
            }), 400
    
    user = User.find_user(data['email'])

    if not user:
        return jsonify({
            'status': 404, 
            'data':None, 
            'msg':'User not found!',
            }), 404

    if not check_password_hash(user.password, data['password']):
        return jsonify({
            'status': 401, 
            'data':None, 
            'msg':'Could not verify!',
            }), 401
    
    utcnow = datetime.utcnow()
    addiotional_claims = {
        'exp' : utcnow + timedelta(minutes=15),
    }
    access_token = create_access_token(identity=user.user_id, additional_claims=addiotional_claims)
    refresh_token = create_refresh_token(identity=user.user_id)
    
    db.session.add(
        Token(
            jti=get_jti(access_token), 
            type="access", 
            user_id=user.user_id, 
            created_at=utcnow, 
            last_updated_at=utcnow,
            ))
    db.session.add(
        Token(
            jti=get_jti(refresh_token), 
            type="refresh", 
            user_id=user.user_id, 
            created_at=utcnow, 
            last_updated_at=utcnow
            ))

    db.session.commit()

    response = jsonify({
        'status': 200, 
        'data': {
            'access_token': access_token, 
            'refresh_token' : refresh_token
            }, 
        'msg':'Signed in successfully!',
        })
    response.headers.extend({'jwt-token': access_token})

    return response, 200