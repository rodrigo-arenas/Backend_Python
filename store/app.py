from fastapi import FastAPI, Body
from models.user import User
from models.author import Author
from models.book import Book

app = FastAPI()


@app.post('/user')
async def post_user(user: User):
    return {"request body": user}


# Query parameter /user/?password
@app.get('/user')
async def get_user_validation(password: str):
    return {"query parameter": password}


# {} takes the parameter in the url itself (path parameter)
@app.get("/book/{isbn}")
async def get_book_with_isbn(isbn: str):
    return {"query changeable parameter": isbn}


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

