from pydantic import BaseModel
from typing import List, Optional


class BookBase(BaseModel):
    title: str
    author: str
    description: str
    year: int


class UserBase (BaseModel):
    name: str
    email: str
    password: str


class BookCreate(BookBase):
    pass

class UserCreate(UserBase):
    pass




class Login(BaseModel):
    username : str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


    
class ShowUser(UserBase):
    name: str
    email: str

    books: List[BookCreate]

    class Config():
        from_attributes = True


class ShowBook(BookBase):
    reader: ShowUser

    class config:
        from_attribute = True
