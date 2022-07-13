from datetime import date
from sqlalchemy.orm import Session

from db.admin_database import get_db
from db.models.Attendance import Attendance

DB = next(get_db())

def create(member_id: int, db: Session = DB):
    attendance = Attendance(
        id = None,
        member_id = member_id,
        date = date.today()
        )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance


def get(id: int, db: Session = DB):
    return db.query(Attendance).filter(Attendance.member_id==id).first()

def get_by_member_id(id: int, db: Session = DB):
    return db.query(Attendance).filter(Attendance.member_id==id).order_by(Attendance.id.asc()).all()

def get_all(db: Session = DB):
    return db.query(Attendance).order_by(Attendance.id.asc()).all()

def get_today(db: Session = DB):
    return db.query(Attendance).filter(Attendance.date==str(date.today())).order_by(Attendance.id.asc()).all()

def get_today_by(id: int, db: Session = DB):
    return db.query(Attendance).filter(Attendance.date==str(date.today())).filter(Attendance.member_id == id).first()

def delete(id : int, db : Session = DB):
    delete_user = db.query(Attendance).filter(Attendance.id == id)
    if not delete_user.first():
        return 0
    delete_user.delete(synchronize_session=False)
    db.commit()
    return delete_user