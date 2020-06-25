from fastapi import Body, Header, File, APIRouter
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response
from models.user import User
from models.author import Author
from models.book import Book
from utils.context_manager.db_functions import (db_insert_personnel, db_check_personnel,
     db_get_book_with_isbn, db_get_author, db_get_author_from_id, db_patch_author)


app_v1 = APIRouter()


@app_v1.post('/user', status_code=HTTP_201_CREATED, tags=["User"])
# async def post_user(user: User, x_custom: str = Header("Default header"), jwt: bool = Depends(check_jwt_token)):
async def post_user(user: User):
    await db_insert_personnel(user)
    return {"request body": user, "message": "Personnel is created"}


# Query parameter /user/?password
@app_v1.post('/login', tags=["User"])
async def get_user_validation(username: str = Body(...), password: str = Body(...)):
    is_valid = await db_check_personnel(username, password)
    return {"is_valid": is_valid}


# {} takes the parameter in the url itself (path parameter)
# Returns a Book model and removes author by default
@app_v1.get("/book/{isbn}", response_model=Book, response_model_exclude=["author"], tags=["Book"])
async def get_book_with_isbn(isbn: str):
    book = await db_get_book_with_isbn(isbn)
    author = await db_get_author(book['author'])
    author_object = Author(**author)
    book['author'] = author_object
    result_book = Book(**book)
    return result_book


# Query and path parameter
@app_v1.get("/author/{author_id}/book", tags=["Author"])
async def get_author_books(author_id: int,  order: str = "asc"):
    author = await db_get_author_from_id(author_id)
    if bool(author):
        books = author['books']
        if order == 'asc':
            books = sorted(books)
        else:
            books = sorted(books, reverse=True)
        return {'books': books}
    else:
        return {f"No author found by id {author_id}"}


# Update authors name, get the information from body request
# embed=True makes the parameter a key in body json
@app_v1.patch('/author/{author_id}/name', tags=["Author"])
async def put_user_name(author_id: int, name: str = Body(..., embed=True)):
    await db_patch_author(author_id, name)
    return {"message": "name is updated"}


# Take two models at the same time
@app_v1.post('/user/author', tags=["User", "Author"])
async def post_user_and_author(user: User, author: Author, bookstore_name: str = Body(..., embed=True)):
    return {"user": user, "author": author, "bookstore_name": bookstore_name}


# Upload an user photo (multipart)
@app_v1.post("/user/photo", tags=["User"])
async def update_photo(response: Response, profile_photo: bytes = File(...)):
    response.headers['x-file-size'] = str(len(profile_photo))
    response.set_cookie(key='cookie-api', value="test")
    return {"profile photo size": len(profile_photo)}

