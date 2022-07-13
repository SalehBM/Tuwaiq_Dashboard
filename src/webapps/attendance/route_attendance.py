# ######################### #
#     Tuwaiq Dashboard      #
#     Attedances Pages      #
# ######################### #

from fastapi import APIRouter, Request, Depends

from db.repository.login import get_current_user_from_token
from db.models.AdminUser import AdminUser
from schemas.Attendance import AttendanceRow
from routers.attendance import get_all, get_attendances_today, delete_attendance
from routers.admin import get_admin
from webapps.base import templates

router = APIRouter(include_in_schema=False)

@router.get("/attedances")
async def attendances(request:Request, auth: AdminUser = Depends(get_current_user_from_token)):
    attendances = get_all()
    list = []
    for attendance in attendances:
        user = get_admin(attendance.member_id)

        if user is None:
            delete_attendance(attendance.id)
        else:
            list.append(AttendanceRow(
                id = attendance.id,
                user = user.username,
                date = attendance.date
            ))
    return templates.TemplateResponse("attendances.html", {
        "request": request,
        "attendances": list
        })

@router.get("/attedancestoday")
async def attendances(request:Request, auth: AdminUser = Depends(get_current_user_from_token)):
    attendances = get_attendances_today()
    list = []
    for attendance in attendances:
        user = get_admin(attendance.member_id)

        if user is None:
            delete_attendance(attendance.id)
        else:
            list.append(AttendanceRow(
                id = attendance.id,
                user = user.username,
                date = attendance.date
            ))
    return templates.TemplateResponse("attendances.html", {
        "request": request,
        "attendances": list
        })