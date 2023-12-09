from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Users(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_no: str = Field(max_length=10)
    password: str
    created_at:Optional[datetime]=None
    modified_at:Optional[datetime]=None


class LoginModel(BaseModel):
    email: str
    password: str
