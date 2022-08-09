import os
from dotenv import load_dotenv
from flask_cors import CORS
from app.extensions import app, db, migrate, jwt, swagger
from app.auth import auth_blueprint
from app.api import api_blueprint
from app.middleware import user_lookup_callback, is_token_revoked

load_dotenv() 

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY']= os.environ['SECRET_KEY']
app.config['SWAGGER'] = {'title': 'Note Brew API Docs', 'uiversion': 3}
# app.config['SWAGGER']['openapi'] = '3.0.2'
app.config['JWT_AUTH_URL_RULE'] = '/api/auth'
app.config['JWT_AUTH_HEADER_NAME'] = 'JWTAuthorization'

CORS(app)

jwt.__init__(app)
jwt.user_lookup_loader(user_lookup_callback)
jwt.token_in_blocklist_loader(is_token_revoked)

db.init_app(app)
migrate.init_app(app, db)

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

template = {
    "swagger": "2.0",
    "info": {
        "title": "Note Brew API",
        "description": "API for Note Brew",
        "version": "0.0.1"
    },
    "schemes": [
        "https",
        "http",
    ], 
    "securityDefinitions": {
        "JWT": {
            "type": "apiKey",
            "name": "access_token",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme."
        }
    },
    "security": {
        "JWT" : []
    }
}
swagger.config = swagger_config
swagger.template = template
swagger.init_app(app)
app.register_blueprint(auth_blueprint)
app.register_blueprint(api_blueprint)

print(app.url_map)
