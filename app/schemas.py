from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class PostBase(BaseModel):
    title: str 
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut #for this to work make sure User out class is above (already defined), not below 
    class Config: #for pydantic up to date this is not necesary 5:40 ish in the video orm_mode
        from_attributes = True #https://www.youtube.com/watch?v=0sOvCWFmrtA&ab_channel=freeCodeCamp.org

class PostOut(BaseModel):
    Post: Post
    votes: int

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None #sanjeev has str but i get an error with that so i put int

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) #needs to allow 0 or 1 but this allows negative numbers to so...
