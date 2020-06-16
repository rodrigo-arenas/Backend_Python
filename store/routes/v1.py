from fastapi import FastAPI, Body, Header, File, Depends
from models.user import User
from models.author import Author
from models.book import Book
from starlette.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from starlette.responses import Response
from fastapi.security import OAuth2PasswordRequestForm
from utils.security import authenticate_user, create_jwt_token
from models.jwt_user import JWTUser

app_v1 = FastAPI(root_path='/v1')


# FastAPI requires that username and password be sent
@app_v1.post('/token')
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    jwt_user_dict = {"username": form_data.username, "password": form_data.password}
    jwt_user = JWTUser(**jwt_user_dict)
    user = authenticate_user(jwt_user)
    if user is None:
        return HTTP_401_UNAUTHORIZED
    jwt_token = create_jwt_token(user)
    return {"token": jwt_token}


@app_v1.post('/user', status_code=HTTP_201_CREATED)
async def post_user(user: User, x_custom: str = Header("Default header")):
    return {"request body": user, "request customer header": x_custom}


# Query parameter /user/?password
@app_v1.get('/user')
async def get_user_validation(password: str):
    return {"query parameter": password}


# {} takes the parameter in the url itself (path parameter)
# Returns a Book model and removes author by default
@app_v1.get("/book/{isbn}", response_model=Book, response_model_exclude=["author"])
async def get_book_with_isbn(isbn: str):
    author_dict = {
        "name": "author 1",
        "book": ["book 1", "book 2"]
    }
    author_1 = Author(**author_dict)
    book_dict = {
        "isbn": isbn,
        "name": "my book",
        "year": 2019,
        "author": author_1
    }
    book_1 = Book(**book_dict)
    return book_1


# Query and path parameter
@app_v1.get("/author/{author_id}/book")
async def get_author_books(author_id: int, category: str, order: str = "asc"):
    return {"query changeable parameter": category + order + str(author_id)}


# Update authors name, get the information from body request
# embed=True makes the parameter a key in body json
@app_v1.patch('/author/name')
async def put_user_name(name: str = Body(..., embed=True)):
    return {"body parameters": name}


# Take two models at the same time
@app_v1.post('/user/author')
async def post_user_and_author(user: User, author: Author, bookstore_name: str = Body(..., embed=True)):
    return {"user": user, "author": author, "bookstore_name": bookstore_name}


# Upload an user photo (multipart)
@app_v1.post("/user/photo")
async def update_photo(response: Response, profile_photo: bytes = File(...)):
    response.headers['x-file-size'] = str(len(profile_photo))
    response.set_cookie(key='cookie-api', value="test")
    return {"profile photo size": len(profile_photo)}
