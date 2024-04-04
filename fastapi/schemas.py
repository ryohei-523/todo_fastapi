from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    is_admin:bool
    
class User(UserBase):
    id: int
    created_at: str
    class Config:
        orm_mode=True

class Todo(BaseModel):
    id : int
    user_id: int
    title: str
    content: str
    created_at: str
