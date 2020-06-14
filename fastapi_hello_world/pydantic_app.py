import datetime
from typing import List, Dict
from pydantic import BaseModel


def get_book(book_name: List[str], year: datetime, price: float, editorials_years: Dict[str, int]):
    """
    FastAPI uses pydantic for, declaring data types, generating documentation and inputs validation
    """
    pass


class Book(BaseModel):
    name: str
    price: float
    year: datetime.datetime


book1 = {'name': "book 1", 'price': 15.3, 'year': datetime.datetime.now()}
book_object = Book(**book1)


def print_book(book: Book):
    """
    :param book: Book object
    :return: print Book object
    """
    print(Book)


print_book(book_object)
