from app.extensions import db
from flask_jwt_extended import get_current_user

class Token(db.Model):
    __tablename__ = "tokens"
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    type = db.Column(db.String(16), nullable=False)
    user_id = db.Column(
        db.ForeignKey('users.user_id'), 
        default=lambda: get_current_user().user_id, 
        nullable=False,
        )
    created_at = db.Column(db.DateTime, nullable=False)
    last_updated_at = db.Column(db.DateTime, nullable=False)
    is_valid = db.Column(db.Boolean(), nullable=False, default=True)