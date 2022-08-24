from flask import Flask
from flask_cors import CORS
from app.configs.swagger import swagger_config, swagger_template 
from app.extensions import db, migrate, jwt, swagger
from app.middleware import user_lookup_callback, is_token_revoked
from app.auth import auth_blueprint
from app.api import api_blueprint
from app.pages import page_blueprint

def create_app(config='configs.config.DevelopmentConfig'):
    app = Flask(__name__)  
    app.config.from_object(config)

    CORS(app)

    init_db(app)
    init_swagger(app)
    register_blueprints(app)

    return app

# JWT
def init_jwt(app):
    jwt.__init__(app)
    jwt.user_lookup_loader(user_lookup_callback)
    jwt.token_in_blocklist_loader(is_token_revoked)

# DB
def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)

# Swagger
def init_swagger(app):
    swagger.config = swagger_config
    swagger.template = swagger_template
    swagger.init_app(app)

# Blueprints
def register_blueprints(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(page_blueprint)
