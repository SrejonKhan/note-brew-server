from datetime import datetime, timedelta
from flask import jsonify, request, Blueprint
import jwt
from werkzeug.security import check_password_hash
from app.models import User

sign_in_bp = Blueprint('sign_in', __name__)

@sign_in_bp.route('/sign-in', methods=["POST"])
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
    
    token = jwt.encode({
        'user_id': user.user_id,
        'exp' : datetime.utcnow() + timedelta(minutes=15),
    },sign_in_bp.config['SECRET_KEY'], "HS256")
    
    return jsonify({
        'status': 200, 
        'data': {'token': token}, 
        'msg':'Signed in successfully!',
        }), 200
