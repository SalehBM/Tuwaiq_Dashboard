from datetime import date
from typing import Optional
from pydantic import BaseModel

class AdminUserBase(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    registration_date: date

    class Config:
        orm_mode = True

class AdminUserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class AdminUserEdit(BaseModel):
    username: str
    email: str
    password: str
    
    class Config:
        orm_mode = True

class AdminUserShow(BaseModel):
    id: Optional[int]
    username: str
    email: str
    registration_date: date

    class Config:
        orm_mode = True