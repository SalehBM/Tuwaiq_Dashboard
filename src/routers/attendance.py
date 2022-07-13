from fastapi import Depends, APIRouter, status

from internal import oauth2
from db.models.AdminUser import AdminUser
from db.repository import attendance as attendanceDB

router = APIRouter(
    prefix='/attendance',
    tags=['Attendance']
    )

@router.post('/create', status_code=status.HTTP_200_OK)
def create(member_id: int, auth: AdminUser = Depends(oauth2.get_current_user)):
    return attendanceDB.create(member_id)

@router.get('/get', status_code=status.HTTP_200_OK)
def get_by_id(id: int, auth: AdminUser = Depends(oauth2.get_current_user)):
    return attendanceDB.get(id=id)

@router.get('/getToday', status_code=status.HTTP_200_OK)
def get_attendances_today(auth: AdminUser = Depends(oauth2.get_current_user)):
    return attendanceDB.get_today()

@router.get('/isAttedanceToday', status_code=status.HTTP_200_OK)
def get_attendances_today_by_member_id(id: int, auth: AdminUser = Depends(oauth2.get_current_user)):
    return attendanceDB.get_today_by(id)

@router.get('/getByMember', status_code=status.HTTP_200_OK)
def get_all_by_member_id(auth: AdminUser = Depends(oauth2.get_current_user)):
    return attendanceDB.get_by_member_id(id)

@router.get('/getAll', status_code=status.HTTP_200_OK)
def get_all(auth: AdminUser = Depends(oauth2.get_current_user)):
    return attendanceDB.get_all()

@router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_attendance(id : int, auth: AdminUser = Depends(oauth2.get_current_user)):
    return attendanceDB.delete(id)