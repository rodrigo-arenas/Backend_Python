import aioredis
from fastapi import FastAPI, Depends, HTTPException
from routes.v1 import app_v1
from routes.v2 import app_v2
from starlette.status import HTTP_401_UNAUTHORIZED
from utils.security import check_jwt_token, authenticate_user, create_jwt_token
from utils.constants import REDIS_URL
from fastapi.security import OAuth2PasswordRequestForm
from models.jwt_user import JWTUser
import utils.context_manager.redis_object as red


app = FastAPI(title="Bookstore API", description="API for bookstore backend", version="1.3")

app.include_router(app_v1, prefix='/v1', dependencies=[Depends(check_jwt_token)])
app.include_router(app_v2, prefix='/v2', dependencies=[Depends(check_jwt_token)])


@app.on_event('startup')
async def connect_redis():
    red.redis = await aioredis.create_redis_pool(REDIS_URL)


@app.on_event('shutdown')
async def disconnect_redis():
    red.redis.close()
    await red.redis.await_closed()


# FastAPI requires that username and password be sent
@app.post('/token', summary="Returns JWT Token",
          description="Check for username and password to generate JWT token",
          tags=["Auth"])
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    jwt_user_dict = {"username": form_data.username, "password": form_data.password}
    jwt_user = JWTUser(**jwt_user_dict)
    user = await authenticate_user(jwt_user)
    if user is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    jwt_token = create_jwt_token(user)
    return {"access_token": jwt_token, "token_type": "bearer"}


"""
# Middleware to handle jwt auth in all the endpoints
@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    if not any(word in str(request.url) for word in ["/token", "/docs", "/openapi.json"]):
        # Get the JWT Token sent from request
        try:
            jwt_token = request.headers["Authorization"].split('Bearer ')[1]
            is_valid = check_jwt_token(jwt_token)
        except Exception as e:
            is_valid = False

        if not is_valid:
            return Response("Unauthorized", status_code=HTTP_401_UNAUTHORIZED)
    response = await call_next(request)
    execution_time = (datetime.utcnow() - start_time).microseconds
    response.headers["x-execution_time"] = str(execution_time)
    return response
"""