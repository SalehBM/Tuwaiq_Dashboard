from typing import Optional
from pydantic import BaseModel

class Link(BaseModel):
    id: Optional[int]
    member_id: str
    link: str

    class Config:
        orm_mode= True