from flask import Blueprint
from .sign_in import sign_in_bp
from .sign_up import sign_up_bp
from .sign_out import sign_out_bp
from .refresh import refresh_bp

auth_blueprint = Blueprint('auth_v1', __name__, url_prefix='/auth')

auth_blueprint.register_blueprint(sign_in_bp)
auth_blueprint.register_blueprint(sign_up_bp)
auth_blueprint.register_blueprint(sign_out_bp)
auth_blueprint.register_blueprint(refresh_bp)