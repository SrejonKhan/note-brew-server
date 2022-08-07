from flask import Blueprint
from flask_jwt_extended import jwt_required, current_user

user_api_bp = Blueprint("user_api", __name__)


@user_api_bp.route('/me')
@jwt_required()
def me():
    user = current_user
    return user.user_id


