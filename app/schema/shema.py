from pydantic import BaseModel, EmailStr
from sqlalchemy.dialects.postgresql import array


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    voice_data : array[int]

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True