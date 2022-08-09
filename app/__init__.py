import os
from dotenv import load_dotenv
from flask_cors import CORS
from app.extensions import app, db, migrate, jwt
from app.auth import auth_blueprint
from app.api import api_blueprint
from app.middleware import user_lookup_callback, is_token_revoked

load_dotenv() 

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY']= os.environ['SECRET_KEY']

CORS(app)

jwt.__init__(app)
jwt.user_lookup_loader(user_lookup_callback)
jwt.token_in_blocklist_loader(is_token_revoked)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(auth_blueprint)
app.register_blueprint(api_blueprint)

print(app.url_map)
