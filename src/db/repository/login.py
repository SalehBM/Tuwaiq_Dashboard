from fastapi import HTTPException, status, Depends, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from schemas.Login import Login
from jose import jwt,JWTError

from internal.hashing import Hash
from internal import JWToken
from internal.oauth2 import oauth2_scheme
from core.admin_config import Settings
from db.admin_database import get_db
from db.models.AdminUser import AdminUser

DB = next(get_db())

def login(response: Response, user_request : Login, db: Session = DB):
    user = db.query(AdminUser).filter(AdminUser.username == user_request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials"
            )
    if not Hash.verify(user_request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Incorrect Password"
            )
    access_token = JWToken.create_access_token(data={"sub": user_request.username})
    response.set_cookie(key="access_token",value=f"Bearer {access_token}",httponly=True)
    return {"access_token": access_token, "token_type": "bearer"}

def get_user(username: str, db: Session = DB):
    return db.query(AdminUser).filter(AdminUser.username == username).first()

def get_current_user_from_token(token:str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_302_FOUND,
        detail="Could not validate credentials",
        headers = {"Location": "/error401"}
        )
    try:
        payload = jwt.decode(token, Settings.SECRET_KEY,algorithms=[Settings.ALGORITHM])
        username:str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username=username, db=db)
    if user is None:
        raise credentials_exception
    return user