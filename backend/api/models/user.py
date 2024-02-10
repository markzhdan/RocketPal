from pydantic import BaseModel

class RegisterData(BaseModel):
    name: str
    email: str
    password: str

class LoginData(BaseModel):
    email : str
    password : str
