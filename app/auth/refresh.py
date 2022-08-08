from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask import jsonify, Blueprint

refresh_bp = Blueprint('refresh', __name__)

@refresh_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({
        'status': 200, 
        'data': {
            'access_token': access_token
            }, 
        'msg':'Token refreshed successfully!',
        }), 200