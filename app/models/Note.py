from flask import jsonify
from app.extensions import db
from app.helper import Serializer

class Note(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable = False)
    user_id = db.Column(db.String(120), db.ForeignKey('users.user_id'))
    
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Note %r>' % self.id
    
    def jsonify_self(self):
        return jsonify(self.dictify_self())
        
    def dictify_self(self):
        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id,
            }
