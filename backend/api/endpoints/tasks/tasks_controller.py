from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from bson.json_util import dumps
from dotenv import load_dotenv
from api.models.task import NewTaskData
from db.db import Database
from api.endpoints.helper import get_current_user

router = APIRouter()

client = Database().get_database()

goals_collection = client.Goals

oauth2_scheme_token = OAuth2PasswordBearer(tokenUrl="token")

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
            goals_collection.update_one({"goal_id": goal_id}, {"$set": goal})
            return {"message" : "Task added successfully", "status_code" : 200}
        else:
            return {"message" : "Something went wrong", "status_code" : 400}
        