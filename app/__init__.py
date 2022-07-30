import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.extensions import db, app
from app.auth import auth_blueprint
from app.api import api_blueprint

load_dotenv() 

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']= os.environ['SECRET_KEY']

CORS(app)

db.init_app(app)

app.register_blueprint(auth_blueprint)
app.register_blueprint(api_blueprint)

print(app.url_map)
