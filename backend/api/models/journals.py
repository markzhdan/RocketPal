from fastapi import FastAPI
from pydantic import BaseModel

class Journals(BaseModel):
    date: int
    title: str
    subtitle: str
    content: str
    

    