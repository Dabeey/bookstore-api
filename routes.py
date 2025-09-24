from fastapi import APIRouter, HTTPException, status, Depends
from models import Book
from database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Books']
)

@router.get('/books')
def all():
    return 