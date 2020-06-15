from pydantic import BaseModel
from models.book import Book
from typing import List


class Author(BaseModel):
    name: str
    book: List[Book]

