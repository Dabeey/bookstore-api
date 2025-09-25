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


@router.get('', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found.')
    return user