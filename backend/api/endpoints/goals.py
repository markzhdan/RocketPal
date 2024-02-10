from fastapi import FastAPI
from pydantic import BaseModel

class Goal(BaseModel):
    user_id: str
    tasks: list
    name: str
    completed: bool
    ptvalue: int
    icon: str
