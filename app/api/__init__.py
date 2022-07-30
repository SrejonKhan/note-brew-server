from flask import Blueprint
from .note_api import note_api_bp
from .user_api import user_api_bp

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

api_blueprint.register_blueprint(note_api_bp)
api_blueprint.register_blueprint(user_api_bp)