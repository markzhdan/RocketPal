from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    email: str
    password: str 
    first_login: bool
