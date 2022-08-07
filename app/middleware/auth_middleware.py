from app.models import User

def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.find_user_by_uid(identity)