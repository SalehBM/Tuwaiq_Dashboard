from fastapi import Depends, HTTPException, status

from internal import JWToken
from internal.utils import OAuth2PasswordBearerWithCookie

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="auth/login")
    
def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
    status_code=status.HTTP_302_FOUND,
    detail="Could not validate credentials",
    headers = {"Location": "error401"}
            )
    return JWToken.verify_token(data, credentials_exception)