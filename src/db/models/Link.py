from db.admin_database import Base
from sqlalchemy import Integer, Column, Text

class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key = True, unique = True, nullable = False)
    member_id = Column(Integer, nullable = False)
    link = Column(Text)
