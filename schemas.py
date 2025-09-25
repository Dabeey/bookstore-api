from pydantic import BaseModel
from typing import List


class BookBase(BaseModel):
    title: str
    author: str
    description: str
    year: int

class UserBase (BaseModel):
    name: str
    email: str
    username: str


class BookCreate(BookBase):
    pass

class UserCreate(UserBase):
    pass


class ShowBook(BookBase):
    id: int

    class config:
        from_attribute = True


class ShowUser(UserBase):
    name: str
    email: str

    books: List[BookCreate]

    class Config():
        from_attributes = True