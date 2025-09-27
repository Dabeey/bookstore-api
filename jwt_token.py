from typing import Optional
from datetime import timedelta, datetime
from jose import jwt, JWTError
from schemas import TokenData
import os


SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=int('40')


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(token: str,  credentials_exceptions):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')

        if username is None:
            raise credentials_exceptions
        TokenData(username=username)
        
        
    except JWTError:
        raise credentials_exceptions