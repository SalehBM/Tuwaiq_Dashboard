from datetime import date
from typing import Optional
from pydantic import BaseModel

class SubmissionBase(BaseModel):
    id: Optional[int]
    member_id: int
    course_id: int
    date: date
    Approved: bool = False

    class Config:
        orm_mode= True

class SubmissionCreate(BaseModel):
    member_id: int
    course_id: int
    Approved: bool = False

class SubmissionRow(BaseModel):
    id: int
    user: str
    course: str
    date: date
    Approved: bool = False
