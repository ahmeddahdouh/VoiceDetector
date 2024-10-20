from typing import List
from pydantic import BaseModel, EmailStr



class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    vocal_data: List[int]
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    vocal_data: List[int]
    password: str



class UserResponse(UserBase):
    id: int
    username: str


    class Config:
        orm_mode = True