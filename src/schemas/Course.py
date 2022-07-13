from datetime import date, timedelta
from typing import Optional
from pydantic import BaseModel

class Course(BaseModel):
    id: Optional[int]
    name: str
    description: str
    requirements: str
    start_date: date
    end_date: date = date.today() + timedelta(days = 3) # By default
    created_by_id: int

    class Config:
        orm_mode= True

class CourseCreate(BaseModel):
    name: str
    description: str
    requirements: str
    start_date: date
    end_date: date = date.today() + timedelta(days = 3) # By default

    class Config:
        orm_mode= True
