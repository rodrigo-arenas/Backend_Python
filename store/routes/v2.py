from fastapi import FastAPI, Header
from models.user import User
from starlette.status import HTTP_201_CREATED

app_v2 = FastAPI(openapi_prefix='/v1')


@app_v2.post('/user', status_code=HTTP_201_CREATED)
async def post_user(user: User):
    return {"request body": user, "api version": 2}
