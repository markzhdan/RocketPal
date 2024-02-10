from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from db.db import Database
from api.models.ai import GenerateResponse
from dotenv import load_dotenv
import os
from ai_func import gen_response
from api.endpoints.helper import get_current_user

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

router = APIRouter()

client = Database().get_database()

users_collection = client.Users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme_token = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/generate_response")
async def generate_response(request_body: GenerateResponse, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        try:
            response = gen_response(request_body.text)
            return {"response" : response, "status_code" : 200}
        except Exception as e:
            return {"response" : e, "status_code" : 500}
    else:
        return {"response" : "not a valid user", "status_code" : 401}
