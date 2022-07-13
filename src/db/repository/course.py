from sqlalchemy.orm import Session
from datetime import date
import calendar

from schemas.Course import CourseCreate
from db.admin_database import get_db
from db.models.Course import Course

DB = next(get_db())

def create(course: CourseCreate, creator_id: int, db: Session = DB):
    course_db = Course(
        name = course.name,
        description = course.description,
        requirements = course.requirements,
        start_date = course.start_date,
        end_date = course.end_date,
        created_by_id = creator_id,
    )
    db.add(course_db)
    db.commit()
    db.refresh(course_db)
    return course_db

def get(id: int, db: Session = DB):
    return db.query(Course).filter(Course.id==id).first()

def get_month_courses(sdate: date, db: Session = DB):
    year = sdate.year
    month = sdate.month
    start = date(year, month, 1)
    end = date(year, month, calendar.monthrange(year, month)[1])
    return db.query(Course).filter(Course.start_date >= start).filter(Course.start_date <= end).all()

def get_all(db: Session = DB):
    return db.query(Course).order_by(Course.start_date.asc()).all()

def edit(id: int, newEdit: CourseCreate, db: Session = DB):
    course = db.query(Course).get(id)
    if course:
        course.name = newEdit.name
        course.description = newEdit.description
        course.requirements = newEdit.requirements
        course.start_date = newEdit.start_date
        course.end_date = newEdit.end_date
        return course

def delete(id : int, db : Session = DB):
    delete_user = db.query(Course).filter(Course.id == id)
    obj = delete_user
    if not delete_user.first():
        return 0
    delete_user.delete(synchronize_session=False)
    db.commit()
    return obj