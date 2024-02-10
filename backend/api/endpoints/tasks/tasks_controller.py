from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pymongo.mongo_client import MongoClient
from bson.json_util import dumps
import uuid
from bson import ObjectId
from dotenv import load_dotenv
from api.models.goal import GoalData, NewGoalData, RemoveGoalData
import os
from db.db import Database

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    
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
    
@router.get("/get_goals")
def get_goals(token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        goals_collection = client.Goals
        goals = goals_collection.find({"user_id": user_id})

        goals_list = []
        for goal in goals:
            goals_list.append(goal)
        data = {"goals" : goals_list}
        return dumps(data)
    
@router.post("/add_goal")
async def add_goal(request_body : NewGoalData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        data = {}
        data['name'] = request_body.name
        data["goal_id"] = str(uuid.uuid4())
        data["user_id"] = user_id
        data["icon"] = "test" # gemini parsing 
        data["tasks"] = []
        data["ptvalue"] = 20
        goals_collection = client.Goals
        result = goals_collection.insert_one(data)

        if result.inserted_id:
            # Return the inserted document's ID
            return {"message": "Goal added successfully", "goal_id": str(result.inserted_id)}
        else:
            # If insertion failed, raise an HTTPException with a 500 status code
            return {"message": "Goal not added, error", "status_code" : 500}
    

@router.post("/modify_goal")
async def modify_goal(request_body: GoalData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        goal_id = request_body.goal_id
        result = goals_collection.update_one({"goal_id": goal_id}, {"$set": request_body.model_dump()})
        if result.modified_count == 1:
            return {"message": "Goal updated successfully"}
        else:
            return {"message": "Failed to update goal"}
        
@router.post("/remove_goal")
async def remove_goal(request_body : RemoveGoalData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        goal_id = request_body.goal_id
        goals_collection = client.Goals
        result = goals_collection.delete_one({"goal_id": goal_id})

        if result.deleted_count == 1:
            return {"message": "Goal deleted successfully"}
        else:
            return {"message": "Goal not found "}
