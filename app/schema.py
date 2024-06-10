from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """
    Pydantic schema for creating a new user.
    """
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    """
    Pydantic schema for user  login
    """
    email: EmailStr
    password: str

class PostCreate(BaseModel):
    """
    Pydantic schema for creating a new post
    """
    text: str

class Post(BaseModel):
    """
    Pydantic schema for returning a post
    """
    id: int
    text: str
    owner_id: int

    class Config:
        orm_mode = True
