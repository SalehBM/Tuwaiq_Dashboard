from fastapi import APIRouter

from routers.admin import router as admin_router
from routers.login import router as auth_router
from routers.submission import router as submission_router
from routers.course import router as course_router
from routers.attendance import router as attendance_router
from routers.attendace_generator import router as QR_Router
from routers.link import router as link_router

api_router = APIRouter()

api_router.include_router(admin_router,prefix="",tags=["Admin User"])
api_router.include_router(auth_router,prefix="",tags=["Auth"])
api_router.include_router(submission_router,prefix="",tags=["Submissions"])
api_router.include_router(course_router,prefix="",tags=["Courses"])
api_router.include_router(attendance_router,prefix="",tags=["Attendance"])
api_router.include_router(QR_Router,prefix="",tags=["QR Code"])
api_router.include_router(link_router,prefix="",tags=["QR Links"])
