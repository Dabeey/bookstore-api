from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__='Books'
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)

    readers = relationship('User', back_populates='blogs')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)