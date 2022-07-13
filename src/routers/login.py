# ################ #
# AdminUser        #
# ################ #
from fastapi import APIRouter, Response, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from db.repository.login import login
from db.admin_database import get_db
from schemas.Login import Login

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
    )

@router.post('/login', status_code=status.HTTP_200_OK)
async def login_user(request: Response ,auth: OAuth2PasswordRequestForm = Depends()):
    return login(response=request, user_request=auth, db = next(get_db()))

async def login_user_form(response, username, password):
    request = Login(username=username, password= password)
    return login(response=response, user_request=request, db=next(get_db()))