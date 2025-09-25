from fastapi import APIRouter, HTTPException, status, Depends
from models import Book
from database import get_db
from sqlalchemy.orm import Session
from schemas import BookCreate, ShowBook
from typing import List
from repositories import book

router = APIRouter(
    prefix = '/books',
    tags=['Books']
)

@router.get('', response_model= List[ShowBook])
def all(db: Session = Depends(get_db)):
    return book.all_books(db)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=ShowBook)
def create(request: BookCreate, db: Session = Depends(get_db)):
    return book.create_book(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBook)
def show(id:int, db: Session = Depends(get_db)):
    return book.show_book(id,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(get_db)):
    return book.delete_book(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ShowBook)
def update_book(request:BookCreate, id:int, db: Session = Depends(get_db)):
    return book.update_book(request, id, db)