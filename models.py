from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    books = relationship('Book', back_populates='readers')
    
class Book(Base):
    __tablename__='Books'
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)
    reader_id = Column(Integer, ForeignKey('users.id'))

    readers = relationship('User', back_populates='books')


