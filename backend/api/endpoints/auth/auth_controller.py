from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
import uuid
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from db.db import Database
from api.models.user import LoginData, RegisterData
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

router = APIRouter()

client = Database().get_database()

users_collection = client.Users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme_token = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(email: str, password: str):
    user = users_collection.find_one({"email": email})
    if not user:
        return False
    if not verify_password(password, user['hash_pass']):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/register")
async def register_user(form_data: RegisterData):
    name = form_data.name
    email = form_data.email
    password = form_data.password
    hashed_password = get_password_hash(password)
    print(name)
    # Check if user already exists 
    existing_user = users_collection.find_one({"email": email})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    # Insert new user into the database
    new_user = {"name" : name, "email": email, "hash_pass": hashed_password, "user_id" : str(uuid.uuid4()), "first_login" : True}
    result = users_collection.insert_one(new_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to register user")

    return {"message": "User registered successfully"}

@router.post("/login")
async def login_for_access_token(form_data: LoginData):
    user = authenticate_user(form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["user_id"]}, expires_delta=access_token_expires
    )
    user_data = {
        "name" : user['name'],
        "email" : user['email'],
    }
    return {"access_token": access_token, "user" : user_data, "token_type": "bearer"}

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

def get_user_by_id(user_id: str):
    # Assuming your User model has a method to fetch a user by their ID
    user = client.Users.find_one({"user_id": user_id})
    return user

@router.post("/me")
async def verify_user(token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    user = get_user_by_id(user_id)
    user_data = {
        "name" : user['name'],
        "email" : user['email'],
    }
    if user:
        return {"user" : user_data, "status_code" : status.HTTP_200_OK}
    else:
        return {"user" : None, "status_code" : status.HTTP_401_UNAUTHORIZED}
