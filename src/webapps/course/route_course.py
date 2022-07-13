# ######################### #
#     Tuwaiq Dashboard      #
#       Courses Page        #
# ######################### #

from fastapi import APIRouter, Request, Depends

from db.repository.login import get_current_user_from_token
from db.models.AdminUser import AdminUser
from routers.admin import get_admin
from routers.course import get_all_courses
from routers.submission import get_submission_by_course_id
from webapps.base import templates

router = APIRouter(include_in_schema=False)

@router.get("/courses")
async def courses(request:Request, auth: AdminUser = Depends(get_current_user_from_token)):
    courses = get_all_courses()
    for course in courses:
        course.submissions = len(get_submission_by_course_id(course.id))
        course.instructor = get_admin(course.created_by_id).username
    return templates.TemplateResponse("courses.html", {
        "request": request,
        "courses": courses
        })
