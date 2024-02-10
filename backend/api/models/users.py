from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str 
    id: str
    email: str
    hash_pass: float 
    first_login: bool

