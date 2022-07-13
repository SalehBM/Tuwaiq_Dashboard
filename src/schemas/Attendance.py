from datetime import date
from typing import Optional
from pydantic import BaseModel

class Attendance(BaseModel):
    id: Optional[int]
    member_id: int
    date: date

    class Config:
        orm_mode = True

class CreateAttendance(BaseModel):
    member_id: int

class AttendanceRow(BaseModel):
    id: Optional[int]
    user: str
    date: date