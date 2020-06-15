from fastapi import FastAPI, Body, Header, File
from models.user import User
from models.author import Author
from models.book import Book
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response

app = FastAPI()


@app.post('/user', status_code=HTTP_201_CREATED)
async def post_user(user: User, x_custom: str = Header("Default header")):
    return {"request body": user, "request customer header": x_custom}


# Query parameter /user/?password
@app.get('/user')
async def get_user_validation(password: str):
    return {"query parameter": password}


# {} takes the parameter in the url itself (path parameter)
# Returns a Book model and removes author by default
@app.get("/book/{isbn}", response_model=Book, response_model_exclude=["author"])
async def get_book_with_isbn(isbn: str):
    author_dict ={
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
@app.get("/author/{author_id}/book")
async def get_author_books(author_id: int, category: str, order: str = "asc"):
    return {"query changeable parameter": category + order + str(author_id)}


# Update authors name, get the information from body request
# embed=True makes the parameter a key in body json
@app.patch('/author/name')
async def put_user_name(name: str = Body(..., embed=True)):
    return {"body parameters": name}


# Take two models at the same time
@app.post('/user/author')
async def post_user_and_author(user: User, author: Author, bookstore_name: str = Body(..., embed=True)):
    return {"user": user, "author": author, "bookstore_name": bookstore_name}


# Upload an user photo (multipart)
@app.post("/user/photo")
async def update_photo(response:Response, profile_photo: bytes = File(...)):
    response.headers['x-file-size'] = str(len(profile_photo))
    response.set_cookie(key ='cookie-api', value="test")
    return {"profile photo size": len(profile_photo)}
