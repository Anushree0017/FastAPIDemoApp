from pydantic import BaseModel, EmailStr

class UserCreateRequest(BaseModel):
    username:str
    email:EmailStr
    full_name:str | None = None

class UserUpdateRequest(BaseModel):
    email:EmailStr | None=None
    full_name:str | None=None