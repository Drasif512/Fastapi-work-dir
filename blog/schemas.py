from pydantic import BaseModel
from typing import Optional



class Students(BaseModel):
    firstName: str
    lastName: str


class ShowStudents(BaseModel):
    firstName: str
    lastName: str
    class config():
        orm_mode = True