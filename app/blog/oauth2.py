from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from blog.token import verify_token


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# tokenUrl defines the route of the function that returns token
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return verify_token(token, credentials_exception)
