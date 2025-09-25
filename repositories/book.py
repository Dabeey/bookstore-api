from fastapi import Depends, status, HTTPException
from database import get_db
from  models import Book
from schemas import BookCreate, ShowBook
from sqlalchemy.orm import Session



def all_books(db: Session):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not load books.')

    return books


def create_book(request: BookCreate, db: Session):
    book_instance = Book(title=request.title, description=request.description,author=request.author, year=request.year)
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance


def show_book(id:int, db: Session):
    book_instance = db.query(Book).filter(Book.id == id).first()

    if not book_instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id {id} not found.')

    return book_instance


def delete_book(id:int, db: Session):
    book = db.query(Book).filter(Book.id == id).delete(synchronize_session=False)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not load books.')

    db.commit()
    return f'Deleted blog with id {id}'


def update_book(request:BookCreate, id:int, db: Session):
    book = db.query(Book).filter(Book.id == id)

    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not load books.')

    book.update(request.model_dump())
    db.commit()
    db.refresh(book.first())
    return book.first()


