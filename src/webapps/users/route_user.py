# ######################### #
#     Tuwaiq Dashboard      #
#         User Page         #
# ######################### #

from fastapi import APIRouter, Request

from routers.admin import get_all_admin, get_admin
from routers.submission import get_approved_submission_by_member
from routers.course import get_courses_by_id
from webapps.base import templates

router = APIRouter(include_in_schema=False)

@router.get("/users")
async def users(request:Request):
    return templates.TemplateResponse("user/users.html", {
        "request": request,
        "users": get_all_admin()
        })

@router.get("/user{id}")
def users(request:Request, id: int):
    user = get_admin(id)
    username = user.username
    submission = get_approved_submission_by_member(user.id)
    if submission:
        course = get_courses_by_id(submission.course_id)
        course_name, course_start, course_end = course.name, course.start_date, course.end_date
    else:
        course = course_name = course_start = course_end = None

    return templates.TemplateResponse("user/profile.html", {
        "request": request,
        "username": username,
        "course": course_name,
        "start_date": course_start,
        "end_date": course_end
        })