from passlib.context import CryptContext
from models.jwt_user import JWTUser
from datetime import datetime, timedelta
from utils.constants import JWT_EXPIRATION_MINUTES, JWT_SECRET_KEY, JWT_ALGORITHM
import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED

pwd_context = CryptContext(schemes=["bcrypt"])
jwt_user1 = {"username": "user1",
             "password": "$2b$12$EwjSQTNMAoiWYSZy.HAGoeeyVmxGj/I4stPh49iDkAH.ng5vSGzIu",
             "disabled": False,
             "role": "admin"}
fake_jwt_user1 = JWTUser(**jwt_user1)

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
def authenticate_user(user: JWTUser):
    if fake_jwt_user1.username == user.username and verify_password(user.password, fake_jwt_user1.password):
        return True
    return False


# Create Access JWT Token
def create_jwt_token(user: JWTUser):
    expiration_time = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    jwt_payload = {"sub": user.username,
                   "role": user.role,
                   "exp": expiration_time}
    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, JWT_ALGORITHM)
    return {"token": jwt_token}


# Check whether JWT token is correct
def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")
        if datetime.utcnow() < expiration and fake_jwt_user1.username == username:
            return final_checks(role)
    except Exception as e:
        return HTTP_401_UNAUTHORIZED


# Last checking and return final result, for now, only login admin role
def final_checks(role: str):
    if role == "admin":
        return True
    else:
        return False
