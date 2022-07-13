from sqlalchemy.orm import Session
from datetime import date
import calendar

from internal.hashing import Hash
from schemas.AdminUser import AdminUserCreate, AdminUserEdit
from db.admin_database import get_db
from db.models.AdminUser import AdminUser

DB = next(get_db())

def create(user: AdminUserCreate, db: Session = DB):
    user.password = Hash.hash_pwd(user.password)
    userDB = AdminUser(
        username = user.username,
        email = user.email,
        password = user.password,
        registration_date = date.today()
    )
    db.add(userDB)
    db.commit()
    db.refresh(userDB)
    return user

def get(user_id: int, db: Session = DB):
    return db.query(AdminUser).filter(AdminUser.id==user_id).first()

def get_month_users(sdate: date, db: Session = DB):
    year = sdate.year
    month = sdate.month
    start = date(year, month, 1)
    end = date(year, month, calendar.monthrange(year, month)[1])
    return db.query(AdminUser).filter(AdminUser.registration_date >= start).filter(AdminUser.registration_date <= end,).all()

def get_all(db: Session = DB):
    return db.query(AdminUser).order_by(AdminUser.id.asc()).all()

def edit(user_id: int, newEdit: AdminUserEdit, db: Session = DB):
    user = db.query(AdminUser).get(user_id)
    newEdit.password = Hash.hash_pwd(newEdit.password)
    if user:
        user.username = newEdit.username
        user.email = newEdit.email
        user.password = newEdit.password
        return user

def delete(user_id : int, db : Session = DB):
    delete_user = db.query(AdminUser).filter(AdminUser.id == user_id)
    if not delete_user.first():
        return 0
    delete_user.delete(synchronize_session=False)
    db.commit()
    return delete_user