# ######################### #
#     Tuwaiq Dashboard      #
#     Submission Pages      #
# ######################### #

from fastapi import APIRouter, Request, Depends

from webapps.base import templates
from db.repository.login import get_current_user_from_token
from db.models.AdminUser import AdminUser
from routers.submission import get_all_submissions, delete_submission, get_submission_by_course_id, get_submission_by_member_id
from routers.course import get_courses_by_id
from routers.admin import get_admin
from schemas.Submission import SubmissionRow

router = APIRouter(include_in_schema=False)

@router.get("/submissions")
async def submission(request:Request, auth: AdminUser = Depends(get_current_user_from_token)):
    submissions =  get_all_submissions()
    list = []
    for submission in submissions:
        course = get_courses_by_id(id=submission.course_id)
        user = get_admin(submission.member_id)

        if course is None or user is None:
            delete_submission(submission.id)
        else:
            list.append(SubmissionRow(
                id = submission.id,
                course = course.name,
                user = user.username,
                date = submission.date,
                Approved = submission.Approved
            ))
    return templates.TemplateResponse("submissions.html", {
        "request": request,
        "submissions": list
        })

@router.get("/submissions{course_id}")
async def submission(request:Request, course_id: int, auth: AdminUser = Depends(get_current_user_from_token)):
    submissions =  get_submission_by_course_id(course_id)
    list = []
    for submission in submissions:
        course = get_courses_by_id(id=submission.course_id)
        user = get_admin(submission.member_id)

        if course is None or user is None:
            delete_submission(submission.id)
        else:
            list.append(SubmissionRow(
                id = submission.id,
                course = course.name,
                user = user.username,
                date = submission.date,
                Approved = submission.Approved
            ))
    return templates.TemplateResponse("submissions.html", {
        "request": request,
        "submissions": list
        })

@router.get("/usersubmissions{member_id}")
async def submission(request:Request, member_id: int, auth: AdminUser = Depends(get_current_user_from_token)):
    submissions =  get_submission_by_member_id(member_id)
    list = []
    for submission in submissions:
        course = get_courses_by_id(id=submission.course_id)
        user = get_admin(submission.member_id)

        if course is None or user is None:
            delete_submission(submission.id)
        else:
            list.append(SubmissionRow(
                id = submission.id,
                course = course.name,
                user = user.username,
                date = submission.date,
                Approved = submission.Approved
            ))
    return templates.TemplateResponse("submissions.html", {
        "request": request,
        "submissions": list
        })