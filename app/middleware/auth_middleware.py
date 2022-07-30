from functools import wraps
import jwt
from flask import jsonify, request, abort
from app.extensions import app
from app.models import User

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
    
        if not token:
            return jsonify({
                'status': 401, 
                'data':None, 
                'msg':'Token is missing!',
            }), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.find_user_by_uid(data["user_id"])

        except:
            return jsonify({
                'status': 401, 
                'data':None, 
                'msg':'Invalid Token!',
            }), 401
    
        return f(current_user, *args, **kwargs)
    
    return decorator