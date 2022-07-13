from db.admin_database import Base
from sqlalchemy import Boolean, String, Integer, Column, Date

class Submission(Base):
    __tablename__ = 'submissions'
    id = Column(Integer, primary_key = True, unique = True, nullable = False)
    member_id = Column(Integer, nullable = False)
    course_id = Column(Integer, nullable = False)
    date = Column(Date)
    Approved = Column(Boolean)
