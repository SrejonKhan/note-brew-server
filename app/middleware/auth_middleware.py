from app.extensions import db
from app.models import Token, User

def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.find_user_by_uid(identity)

# callback function to check if a JWT exist in blocklist
def is_token_revoked(jwt_header, jwt_data):
    jti = jwt_data["jti"]
    token = db.session.query(Token).filter_by(jti=jti).first()
    if token is None: 
        return True 
    return not token.is_valid 
