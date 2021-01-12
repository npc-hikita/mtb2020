# pylint: disable=E0611
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    dept: str

    class Config:
        orm_mode = True
