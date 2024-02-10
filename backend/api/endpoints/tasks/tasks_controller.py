from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pymongo.mongo_client import MongoClient
from bson.json_util import dumps
import uuid
from bson import ObjectId
from dotenv import load_dotenv
from api.models.task import NewTaskData
import os
from db.db import Database

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
    
router = APIRouter()

client = Database().get_database()

goals_collection = client.Goals

oauth2_scheme_token = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
@router.post("/add_task")
def add_task(request_body : NewTaskData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        goals_collection = client.Goals
        task_name = request_body.name
        goal_id = request_body.goal_id
        goal = goals_collection.find_one({"goal_id": goal_id})
        if goal:
            data = {
                "name" : task_name,
                "completed" : False,
                "pointsValue" : 10
            }
            goal['tasks'].append(data)
            print(goal['tasks'])
            goals_collection.update_one({"goal_id": goal_id}, {"$set": goal})
            return {"message" : "Task added successfully", "status_code" : 200}
        else:
            return {"message" : "Somethingw ent wrong", "status_code" : 401}
        
# @router.post("/")
# def add_task(request_body : NewTaskData, token: str = Depends(oauth2_scheme_token)):
#     user_id = get_current_user(token)
#     if user_id:
#         goals_collection = client.Goals
#         task_name = request_body.name
#         goal_id = request_body.goal_id
#         goal = goals_collection.find_one({"goal_id": goal_id})
#         if goal:
#             data = {
#                 "name" : task_name,
#                 "completed" : False,
#                 "pointsValue" : 10
#             }
#             goal['tasks'].append(data)
#             print(goal['tasks'])
#             goals_collection.update_one({"goal_id": goal_id}, {"$set": goal})
#             return {"message" : "Task added successfully", "status_code" : 200}
#         else:
#             return {"message" : "Somethingw ent wrong", "status_code" : 401}