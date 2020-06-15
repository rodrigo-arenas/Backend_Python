from pydantic import BaseModel
from models.autorh import AUthor

class Book(BaseModel):
    isbn: str
    name: str
    author: Author
    year: int