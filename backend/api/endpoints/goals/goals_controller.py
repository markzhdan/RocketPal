from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pymongo.mongo_client import MongoClient
from bson.json_util import dumps
import uuid
from bson import ObjectId

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://parkjae433:zBazf6Rzca8N4ccr@rocketpalcluster.txs3ukk.mongodb.net/?retryWrites=true&w=majority")

    def close(self):
        self.client.close()

    def get_database(self):
        return self.client["RocketPalDB"]
    
router = APIRouter()

client = Database().get_database()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def get_current_user(token: str = Depends(oauth2_scheme)):
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
def get_goals(request: Request):
    header_content = request.headers.get("Authorization")
    token = header_content.split("Bearer")[1].strip()
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
async def add_goal(request : Request):
    data = await request.json()
    header_content = request.headers.get("Authorization")
    token = header_content.split("Bearer")[1].strip()
    user_id = get_current_user(token)
    if user_id:
        data["goal_id"] = str(uuid.uuid4())
        data["user_id"] = user_id
        data["icon"] = "test"
        data["tasks"] = []
        data["ptvalue"] = 20
        goals_collection = client.Goals
        result = goals_collection.insert_one(data)

        if result.inserted_id:
            # Return the inserted document's ID
            return {"message": "Goal added successfully", "goal_id": str(result.inserted_id)}
        else:
            # If insertion failed, raise an HTTPException with a 500 status code
            raise HTTPException(status_code=500, detail="Failed to add goal")
    

@router.post("/modify_goal")
async def modify_goal(request : Request):
    data = await request.json()
    header_content = request.headers.get("Authorization")
    token = header_content.split("Bearer")[1].strip()
    user_id = get_current_user(token)
    if user_id:
        goal_id = data['goal_id']
        goals_collection = client.Goals
        result = goals_collection.update_one({"goal_id": goal_id}, {"$set": data})

        if result.modified_count == 1:
            print("Goal updated successfully")
        else:
            print("Failed to update goal")
        
@router.post("/remove_goal")
async def remove_goal(request : Request):
    data = await request.json()
    header_content = request.headers.get("Authorization")
    token = header_content.split("Bearer")[1].strip()
    user_id = get_current_user(token)
    if user_id:
        goal_id = data['goal_id']
        goals_collection = client.Goals
        result = goals_collection.delete_one({"goal_id": goal_id})

        if result == 1:
            return "Goal deleted succesfully"
        else:
            return "Goal not found"
