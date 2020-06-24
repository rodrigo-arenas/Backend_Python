import jwt
import time
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from datetime import datetime, timedelta
from models.jwt_user import JWTUser
from utils.constants import JWT_EXPIRATION_MINUTES, JWT_SECRET_KEY, JWT_ALGORITHM
from utils.context_manager.db_functions import db_get_user, db_check_jwt_username


pwd_context = CryptContext(schemes=["bcrypt"])

# Creates oauth /token endpoint
oauth_schema = OAuth2PasswordBearer(tokenUrl='/token')


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(password, hashed_password):
    try:
        return pwd_context.verify(password, hashed_password)
    except Exception as e:
        return False


# Authenticate username and password to give JWT Token
async def authenticate_user(user: JWTUser):
    potential_user = await db_get_user(user)
    is_valid = verify_password(user.password, potential_user['password'])
    if is_valid:
        user.role = "admin"
        return user
    return None


# Create Access JWT Token
def create_jwt_token(user: JWTUser):
    expiration_time = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    jwt_payload = {"sub": user.username,
                   "role": user.role,
                   "exp": expiration_time}
    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, JWT_ALGORITHM)
    return jwt_token


# Check whether JWT token is correct
async def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")
        is_valid = await db_check_jwt_username(username)
        if time.time() < expiration and is_valid:
            return final_checks(role)
    except Exception as e:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)


# Last checking and return final result, for now, only login admin role
def final_checks(role: str):
    if role == "admin":
        return True
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
