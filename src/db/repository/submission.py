from sqlalchemy.orm import Session
from datetime import date
import calendar

from schemas.Submission import SubmissionCreate
from db.admin_database import get_db
from db.models.Submission import Submission

DB = next(get_db())

def create(submission: SubmissionCreate, db: Session = DB):
    submission_db = Submission(
        member_id = submission.member_id,
        course_id = submission.course_id,
        date = date.today(),
        Approved = submission.Approved
    )
    db.add(submission_db)
    db.commit()
    db.refresh(submission_db)
    return submission_db

def get(id: int, db: Session = DB):
    return db.query(Submission).filter(Submission.id==id).first()

def get_by_member_id(id: int, db: Session = DB):
    return db.query(Submission).filter(Submission.member_id==id).all()

def get_by_course_id(id: int, db: Session = DB):
    return db.query(Submission).filter(Submission.course_id==id).all()

def get_month_submissions(sdate: date, db: Session = DB):
    year = sdate.year
    month = sdate.month
    start = date(year, month, 1)
    end = date(year, month, calendar.monthrange(year, month)[1])
    return db.query(Submission).filter(Submission.date >= start).filter(Submission.date <= end).all()

def get_all(db: Session = DB):
    return db.query(Submission).order_by(Submission.id.asc()).all()

def edit(id: int, newEdit: bool, db: Session = DB):
    submission = db.query(Submission).get(id)
    if submission:
        submission.Approved = newEdit
        return submission

def delete(id : int, db : Session = DB):
    delete_user = db.query(Submission).filter(Submission.id == id)
    if not delete_user.first():
        return 0
    delete_user.delete(synchronize_session=False)
    db.commit()
    return delete_user