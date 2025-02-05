from jose import jwt, JWTError

SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"

def create_access_token(data):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
