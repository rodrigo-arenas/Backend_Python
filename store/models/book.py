from pydantic import BaseModel, Field
from store.models.author import Author


class Book(BaseModel):
    isbn: str = Field(None, description="Book unique identifier")
    name: str
    author: Author
    year: int = Field(None, gt=1900, lt=2100)
