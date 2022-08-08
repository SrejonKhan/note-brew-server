from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()