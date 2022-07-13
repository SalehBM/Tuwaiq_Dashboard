import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    POSTGRES_USER: str = os.getenv("ADMIN_POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("ADMIN_POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("ADMIN_POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("ADMIN_POSTGRES_PORT", 5433) 
    POSTGRES_DB: str = os.getenv("ADMIN_POSTGRES_DB", "db_course")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

settings = Settings()