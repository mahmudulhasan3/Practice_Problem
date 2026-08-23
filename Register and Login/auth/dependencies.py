from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
import jwt
from auth.security import decode_access_token
from database import get_db
from models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
) -> User:
    creditionals_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= "Invalid or expired token",
        headers= {"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = decode_access_token(token)
        username = payload.get("sub")
        if username is None:
            raise creditionals_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code= 401,  detail= "Token expired")
    except jwt.InvalidTokenError:
        raise creditionals_exception
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise creditionals_exception
    return user
