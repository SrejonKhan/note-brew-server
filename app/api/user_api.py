from flask import Blueprint
from flask_jwt_extended import jwt_required, current_user
from flasgger import swag_from

user_api_bp = Blueprint("user_api", __name__, url_prefix="/user")

@user_api_bp.route('/me')
@jwt_required()
@swag_from("../../docs/user/me.yml")
def me():
    user = current_user
    return user.jsonify_self(), 200


