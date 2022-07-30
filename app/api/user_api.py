from flask import Blueprint
from app.middleware import token_required

user_api_bp = Blueprint("user_api", __name__)

@user_api_bp.route('/me')
@token_required
def me(current_user):
    return current_user.jsonify_self()


