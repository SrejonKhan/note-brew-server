from app.extensions import db
from app.helper import Serializer

class Note(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable = False)
    owner = db.Column(db.String(120), nullable=False)
    
    def __init__(self, content, owner):
        self.content = content
        self.owner = owner

    def __repr__(self):
        return '<Note %r>' % self.note
    
    def serialize(self):
        dict = Serializer.serialize(self)
        return dict
