from flask import jsonify, request, Blueprint
from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models import User
from flasgger import swag_from

sign_up_bp = Blueprint('sign_up', __name__)

@sign_up_bp.route('/sign-up', methods=["POST"])
@swag_from("../../docs/auth/sign-up.yml")
def sign_up():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password') or not data.get('name'):
        return jsonify({
            'status': 400, 
            'data':None, 
            'msg':'Sufficient details not provided!',
            }), 400

    user = User.find_user(data['email'])
    if user: 
        return jsonify({
            'status': 400, 
            'data': None, 
            'msg':'User already exists!',
            }), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_user = User(name = data['name'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    new_user_json = new_user.dictify_self()
    return jsonify({
        'status': 200, 
        'data': new_user_json, 
        'msg':'signed up successfully!',
        }), 200
