import os
from dotenv import load_dotenv
from flask import render_template, request, abort
from flask_cors import CORS
from app.config.swagger import swagger_config, swagger_template 
from app.extensions import app, db, migrate, jwt, swagger
from app.auth import auth_blueprint
from app.api import api_blueprint
from app.middleware import user_lookup_callback, is_token_revoked

load_dotenv() 

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY']= os.environ['SECRET_KEY']
app.config['SWAGGER'] = {'title': 'Note Brew API Docs', 'uiversion': 3}
# app.config['SWAGGER']['openapi'] = '3.0.2'
app.config['JWT_AUTH_URL_RULE'] = '/api/auth'
app.config['JWT_AUTH_HEADER_NAME'] = 'JWTAuthorization'

# CORS
CORS(app)

# JWT
jwt.__init__(app)
jwt.user_lookup_loader(user_lookup_callback)
jwt.token_in_blocklist_loader(is_token_revoked)

# DB
db.init_app(app)
migrate.init_app(app, db)

# Swagger
swagger.config = swagger_config
swagger.template = swagger_template
swagger.init_app(app)

# Blueprint
app.register_blueprint(auth_blueprint)
app.register_blueprint(api_blueprint)

@app.route('/') 
def index():
    return render_template("index.html")
