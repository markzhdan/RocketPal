from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from bson.json_util import dumps
import uuid
from dotenv import load_dotenv
from api.models.goal import GoalData, NewGoalData, RemoveGoalData
from db.db import Database
from ai_func import gen_tasks
from api.endpoints.helper import get_current_user

# Load environment variables from .env file
load_dotenv()
    
router = APIRouter()

client = Database().get_database()

goals_collection = client.Goals

oauth2_scheme_token = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/get_goals")
def get_goals(token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        goals_collection = client.Goals
        goals = goals_collection.find({"user_id": user_id})

        goals_list = []
        for goal in goals:
            goals_list.append(goal)
        data = {"goals" : goals_list, "status_code" : 200}
        return dumps(data)
    
@router.post("/add_goal")
async def add_goal(request_body : NewGoalData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        data = {}
        data['name'] = request_body.name
        data["goal_id"] = str(uuid.uuid4())
        data["user_id"] = user_id 
        tasks = gen_tasks(request_body.name)
        data["tasks"] = tasks
        data["ptvalue"] = 20
        goals_collection = client.Goals
        result = goals_collection.insert_one(data)

        if result.inserted_id:
            return {"message": "Goal added successfully", "status_code" : 200}
        else:
            return {"message": "Goal not added, error", "status_code" : 500}
    

@router.post("/modify_goal")
async def modify_goal(request_body: GoalData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        goal_id = request_body.goal_id
        result = goals_collection.update_one({"goal_id": goal_id}, {"$set": request_body.model_dump()})
        if result.modified_count == 1:
            return {"message": "Goal updated successfully", "status_code" : 200}
        else:
            return {"message": "Failed to update goal", "status_code" : 500}
        
@router.post("/remove_goal")
async def remove_goal(request_body : RemoveGoalData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        goal_id = request_body.goal_id
        goals_collection = client.Goals
        result = goals_collection.delete_one({"goal_id": goal_id})
    
        if result.deleted_count == 1:
            return {"message": "Goal deleted successfully", "status_code" : 200}
        else:
            return {"message": "Goal not found", "status_code" : 500}
