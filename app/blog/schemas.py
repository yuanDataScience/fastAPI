from pydantic import BaseModel
from typing import List, Optional


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]

    class Config():
        orm_mode = True

# this class is for show method to show post title of a specific post id
class ShowBlog(BaseModel):

    # when we use pydantic model for sqlalchemy model,
    # we are using orm. So we need to config pydantic orm_mode
    # to be true. main:show() function to use response_model. When
    # sqlalchemy returns, we need to use orm config to convert it to pydanic
    # response model
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
