from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity 
from flask_jwt_extended import create_access_token, get_jwt, get_jti, get_current_user
from flask import jsonify, Blueprint
from app.extensions import db
from app.models import Token

refresh_bp = Blueprint('refresh', __name__)

@refresh_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    user = get_current_user()
    token = get_jwt()
    access_token = token["jti"]

    stored_access_token = db.session.query(Token).filter_by(jti=access_token).first()

    utcnow = datetime.utcnow()
    stored_access_token.is_valid = False
    stored_access_token.last_updated_at = utcnow 
    
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)

    db.session.add(
        Token(
            jti=get_jti(access_token), 
            type="access", 
            user_id=user.user_id, 
            created_at=utcnow, 
            last_updated_at=utcnow,
            ))

    db.session.commit()

    return jsonify({
        'status': 200, 
        'data': {
            'access_token': access_token
            }, 
        'msg':'Token refreshed successfully!',
        }), 200