from fastapi import FastAPI
from models.user import User

app = FastAPI()


@app.post('/user')
async def post_user(user: User):
    return {"request body": user}
