from fastapi import APIRouter, HTTPException, status, Depends
from models import User
from database import get_db
from sqlalchemy.orm import Session
from schemas import UserCreate, ShowUser
from typing import List
from repositories import user


router = APIRouter(
    prefix = '/users',
    tags=['Users']
)


@router.post('', response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create(request: UserCreate, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)