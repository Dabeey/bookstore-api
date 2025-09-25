from fastapi import HTTPException, status, Depends
from models import User
from sqlalchemy.orm import Session


def create_user(request, db: Session):
    new_user = User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id: int, db: Session):
    user = db.query(User).filter(User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found.')
    return user