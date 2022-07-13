# ######################### #
#     Tuwaiq Dashboard      #
#        Badge Page         #
# ######################### #

from datetime import date
from fastapi import APIRouter, Request, Depends

from db.repository.login import get_current_user_from_token
from db.models.AdminUser import AdminUser
from routers.attendace_generator import create_QR_CODE
from routers.attendance import get_attendances_today_by_member_id
from routers.admin import get_admin
from routers.submission import get_approved_submission_by_member
from routers.course import get_courses_by_id
from webapps.base import templates

router = APIRouter(include_in_schema=False)

@router.get("/mybadge")
def mybadge(request:Request, auth: AdminUser = Depends(get_current_user_from_token)):
    isAttendance = get_attendances_today_by_member_id(auth.id)
    if isAttendance is None:
        isAttendance = ""
    else:
        isAttendance = "Your attendance been registered"

    approved_submission = get_approved_submission_by_member(auth.id)
    if approved_submission:
        approved_submission = get_approved_submission_by_member(auth.id).course_id
    course = get_courses_by_id(approved_submission)
    if course:
        course = course.name
    return templates.TemplateResponse("badge.html", {
        "request": request,
        "isAttendance": isAttendance,
        "QR_Code": create_QR_CODE(request, auth),
        "username": get_admin(auth.id).username,
        "course": course,
        "date": date.today()
        })
