from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
import uuid
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from db.db import Database
from api.models.ai import GenerateResponse
from dotenv import load_dotenv
import os
from ai_func import gen_response

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

router = APIRouter()

client = Database().get_database()

users_collection = client.Users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme_token = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
            # raise HTTPException(
            #     status_code=status.HTTP_401_UNAUTHORIZED,
            #     detail="Invalid authentication credentials",
            #     headers={"WWW-Authenticate": "Bearer"},
            # )
        return user_id
    except JWTError:
        return None
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Invalid authentication credentials",
        #     headers={"WWW-Authenticate": "Bearer"},
        # )
    
@router.post("/generate_response")
async def generate_response(request_body: GenerateResponse, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        try:
            response = gen_response(request_body.text)
            return {"response" : response}
        except Exception as e:
            print(e)
            return {"response" : "invalid response"}
    else:
        return {"response" : "not a valid user"}
