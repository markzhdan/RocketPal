from fastapi import FastAPI
from pydantic import BaseModel

class Tasks(BaseModel):
    name: str
    completed: bool
    ptvalue: int