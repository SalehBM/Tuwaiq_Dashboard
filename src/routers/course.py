from fastapi import Depends, APIRouter, status
from datetime import date
from dateutil.relativedelta import relativedelta
import calendar

from internal import oauth2
from db.repository import course as courseDB
from db.repository.login import get_current_user_from_token
from db.models.AdminUser import AdminUser
from schemas.Course import CourseCreate

router = APIRouter(
    prefix='/courses',
    tags=['Courses']
    )

@router.post('/create', status_code=status.HTTP_200_OK)
def create(course: CourseCreate, auth: AdminUser = Depends(get_current_user_from_token)):
    return courseDB.create(course, creator_id= auth.id)

@router.get('/get', status_code=status.HTTP_200_OK)
def get_courses_by_id(id: int, auth: AdminUser = Depends(oauth2.get_current_user)):
    return courseDB.get(id=id)

@router.get('/get_lastMonths', status_code=status.HTTP_200_OK)
def get_last_three_months(auth: AdminUser = Depends(oauth2.get_current_user)):
    _1 = date.today()
    _2 = date.today() - relativedelta(months=1)
    _3 = date.today() - relativedelta(months=2)
    months = {
        calendar.month_abbr[_1.month]: len(courseDB.get_month_courses(_1)),
        calendar.month_abbr[_2.month]: len(courseDB.get_month_courses(_2)),
        calendar.month_abbr[_3.month]: len(courseDB.get_month_courses(_3))
    }
    return months

@router.get('/getAll', status_code=status.HTTP_200_OK)
def get_all_courses(auth: AdminUser = Depends(oauth2.get_current_user)):
    return courseDB.get_all()

@router.put('/edit', status_code=status.HTTP_200_OK)
def edit_course(id: int, newEdit: CourseCreate, auth: AdminUser = Depends(oauth2.get_current_user)):
    return courseDB.edit(id, newEdit)

@router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_course(id : int, auth: AdminUser = Depends(oauth2.get_current_user)):
    return courseDB.delete(id)