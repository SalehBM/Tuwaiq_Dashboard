from db.admin_database import Base
from sqlalchemy import Integer, Column, Date

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key = True, unique = True, nullable = False)
    member_id = Column(Integer)
    date = Column(Date)
