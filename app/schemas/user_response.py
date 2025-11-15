from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id:int
    username:str
    email:EmailStr
    full_name:str | None=None

    class Config:
        orm_mode = True