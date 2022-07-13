"""
The project "Tuwaiq Dashboard", which simulates "Automate the admission and preparation process", 
has been built for the end of the FastAPI course that was presented by Tuwaiq Academy.
The project is composed of two APIs that are the admin side of the project.

((The project has been built for learning purposes))
"""
# ######################### #
#     Tuwaiq Dashboard      #
#        main file          #
# ######################### #

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from db.admin_database import db_conn as admin_engine
from db.admin_database import Base as admin_base
from db.models import Attendance, AdminUser, Course, Submission
import routers.base
import webapps.base

def create_tables():
    admin_base.metadata.create_all(bind=admin_engine)

def include_router(app):
    app.include_router(router=routers.base.api_router)
    app.include_router(router=webapps.base.api_router)

def configure_static(app):
    app.mount(
    "/templates",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "app/templates"),
    name="templates"
    )

def start_application():
    app = FastAPI(redoc_url=None,
        docs_url=None,
        title="TuwaiqDashboard",
        description="Automate the admission and attedance process",
        version= "0.0.5",
        contact = {
        "name": "Saleh Bin Mohammed",
        "url": "https://www.linkedin.com/in/salehbinmohammed/",
        "email": "salehalsaeed911@gmail.com"
        }
    )
    create_tables()
    include_router(app)
    configure_static(app)
    return app
    
app = start_application()