# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import HTTPAuthorizationCredentials, OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer
# from pydantic import BaseModel
# from typing import Optional
# from ..db.db import Database
# from datetime import datetime, timedelta
# import jwt
# from jwt import PyJWTError
# from passlib.context import CryptContext

# router = APIRouter(prefix="/api")
# security = HTTPBearer()

# db = Database().get_database()

# SECRET_KEY = "your-secret-key"
# ALGORITHM = "HS256"
# # Token expiration time in minutes
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
#     token = credentials.credentials
#     try:
#         # Decode the JWT token to get the user's information
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username = payload.get("sub")  # Assuming the subject (sub) contains the username
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         user = db.get(username)  # Retrieve user from the mock database
#         if user is None:
#             raise HTTPException(status_code=401, detail="User not found")
#         return user
#     except jwt.JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")

# @router.get("/users/{user_id}")
# async def get_user(user_id: int, current_user: Optional[dict] = Depends(get_current_user)):
#     if user_id not in users:
#         raise HTTPException(status_code=404, detail="User not found")
#     return users[user_id]