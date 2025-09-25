from fastapi.security import OAuth2, OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f'Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    return credentials_exceptions