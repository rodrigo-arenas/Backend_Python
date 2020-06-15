from pydantic import BaseModel
from models.author import Author


class Book(BaseModel):
    isbn: str
    name: str
    author: Author
    year: int
