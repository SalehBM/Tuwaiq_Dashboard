# ######################### #
#     Tuwaiq Dashboard      #
#      Web Router Base      #
# ######################### #

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

import internal.status_codes 
from webapps import route_dashboard
from webapps.course import route_course
from webapps.auth import route_auth
from webapps.submission import route_submissions
from webapps.users import route_user
from webapps.attendance import route_attendance
from webapps.attendance import route_qr
from webapps.badge import route_badge

api_router = APIRouter()

api_router.include_router(route_dashboard.router,prefix="",tags=["dashboard"])
api_router.include_router(route_course.router,prefix="",tags=["Courses"])
api_router.include_router(route_auth.router,prefix="",tags=["Auth"])
api_router.include_router(route_submissions.router,prefix="",tags=["Submissions"])
api_router.include_router(route_user.router,prefix="",tags=["users"])
api_router.include_router(route_attendance.router,prefix="",tags=["Attendance"])
api_router.include_router(route_qr.router,prefix="",tags=["QR Links"])
api_router.include_router(route_badge.router,prefix="",tags=["Badge"])

@api_router.get("/error{status_code}")
async def exception(request:Request, status_code: int, details : str = ''):
    return templates.TemplateResponse("pages/exception.html", {
        "request": request,
        "status_code": status_code,
        "status_message": internal.status_codes.codes[status_code],
        "details": details
        })

@api_router.get("/{str}")
async def exception(request:Request, str: str):
    return templates.TemplateResponse("pages/exception.html", {
        "request": request,
        "status_code": 404,
        "status_message": internal.status_codes.codes[404],
        "details": "Page Not Found!"
        })

@api_router.get("/")
async def exception(request:Request):
    return templates.TemplateResponse("pages/exception.html", {
        "request": request,
        "status_code": 404,
        "status_message": internal.status_codes.codes[404],
        "details": "Page Not Found!"
        })

