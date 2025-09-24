from fastapi import APIRouter, HTTPException, status, Depends
from models import Book
from database import get_db
from sqlalchemy.orm import Session
from schemas import BookCreate


router = APIRouter(
    prefix = '/books',
    tags=['Books']
)

@router.get('')
def all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not load books.')

    return books


@router.post('', status_code=status.HTTP_201_CREATED)
def create_book(request: BookCreate, db: Session = Depends(get_db)):
    book_instance = Book(title=request.title, description=request.description,author=request.author, year=request.year)
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance


@router.get('/{id}', status_code=status.HTTP_200_OK)
def show_book(id:int, db: Session = Depends(get_db)):
    book_instance = db.query(Book).filter(Book.id == id).first()

    if not book_instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id {id} not found.')

    return book_instance


@router.get('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).delete(synchronize_session=False)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not load books.')

    db.commit()
    return f'Deleted blog with id {id}'


@router.post('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_book(request:BookCreate, id:int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id)

    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not load books.')

    book.update(request.model_dump())
    db.commit()
    return book.first()


