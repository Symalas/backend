from flask_jwt_extended import create_access_token
from datetime import timedelta

def getJwt(data):
    expires = timedelta(days=5000)
    return create_access_token(data, fresh=True, expires_delta=expires)
