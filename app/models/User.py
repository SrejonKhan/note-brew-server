from flask import jsonify
from app.extensions import db
from app.helper import Serializer
import shortuuid
from werkzeug.security import generate_password_hash

class User(db.Model, Serializer):
    __tablename__ = "users"
    user_id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))
    notes = db.relationship('Note', backref='owner')

    def __init__(self, name, email, password):
        self.user_id = shortuuid.uuid()
        self.name = name
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
    
    def add_self(self):
        db.session.add(self)
        db.session.commit()
    
    def jsonify_self(self):
        return jsonify(self.dictify_self())
        
    def dictify_self(self):
        return {
            'userId': self.user_id,
            'name': self.name,
            'email': self.email,
            }
    
    @staticmethod
    def find_user(email):
        return User.query.filter(User.email == email).first()
    
    @staticmethod
    def find_user_by_uid(user_id):
        return User.query.filter(User.user_id == user_id).one_or_none()


        
