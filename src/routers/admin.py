# ################ #
# AdminUser        #
# ################ #
from fastapi import APIRouter, status, Depends
from datetime import date
from dateutil.relativedelta import relativedelta

from internal import oauth2
from db.repository import adminuser as adminDB
from schemas.AdminUser import AdminUserCreate, AdminUserShow

router = APIRouter(
    prefix='/admin',
    tags=['Admin User']
    )

@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_admin(user: AdminUserCreate, auth: AdminUserShow = Depends(oauth2.get_current_user)):
    return adminDB.create(user)

@router.get('/get/{adminuser_id}', status_code=status.HTTP_200_OK)
def get_admin(user_id: int, auth: AdminUserShow = Depends(oauth2.get_current_user)):
    return adminDB.get(user_id)

@router.get('/getYear_users', status_code=status.HTTP_200_OK)
def get_users_year(auth: AdminUserShow = Depends(oauth2.get_current_user)):
    year = [len(adminDB.get_month_users(date.today() - relativedelta(months=n))) for n in range(11, -1, -1)]
    return year

@router.get('/getAll', status_code=status.HTTP_200_OK)
def get_all_admin(auth: AdminUserShow = Depends(oauth2.get_current_user)):
    return adminDB.get_all()

@router.put('/edit/{adminuser_id}', status_code=status.HTTP_202_ACCEPTED)
def edit_adminuser(user_id: int, newEdit: AdminUserCreate, auth: AdminUserShow = Depends(oauth2.get_current_user)):
    return adminDB.edit(user_id, newEdit)

@router.delete('/delete/{adminuser_id}', status_code=status.HTTP_202_ACCEPTED)
def delete_adminuser(user_id: int, auth: AdminUserShow = Depends(oauth2.get_current_user)):
    return adminDB.delete(user_id)