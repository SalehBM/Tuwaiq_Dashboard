from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

from core.admin_config import settings as admin_settings
from typing import Generator

SQLALCHEMY_DATABASE_URL = admin_settings.DATABASE_URL
db_conn = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, poolclass=NullPool)

Base = declarative_base()
Session = sessionmaker(autocommit = False,autoflush=False, bind=db_conn)

def get_db() -> Generator:
    try:
        db = Session()
        yield db 
    finally:
        db.close_all()