from db.admin_database import Base
from sqlalchemy import String, Integer, Column, Text, Date

class AdminUser(Base):
    __tablename__ = 'admin_users'
    id = Column(Integer, primary_key = True, unique = True, nullable = False)
    username = Column(String(33), unique = True, nullable = False)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    registration_date = Column(Date)
