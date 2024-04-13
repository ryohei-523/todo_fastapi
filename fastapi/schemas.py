from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    is_admin: bool


class User(UserBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True


class TodoBase(BaseModel):
    title: str
    content: str


class Todo(TodoBase):
    id: int
    user_id: int
    created_at: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: str
