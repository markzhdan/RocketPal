from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pymongo.mongo_client import MongoClient
from bson.json_util import dumps
import uuid
from bson import ObjectId
from dotenv import load_dotenv
from api.models.journal import JournalData
import os
from db.db import Database

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
    
router = APIRouter()

client = Database().get_database()

journal_collection = client.Journals

oauth2_scheme_token = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        # if user_id is None:
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Invalid authentication credentials",
        #         headers={"WWW-Authenticate": "Bearer"},
        #     )
        return user_id
    except JWTError:
        return None
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Invalid authentication credentials",
        #     headers={"WWW-Authenticate": "Bearer"},
        # )

@router.post("/add_journal")
def add_journal(request_body : JournalData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        data = request_body.model_dump()
        data['user_id'] = user_id
        result = journal_collection.insert_one(data)

        if result.inserted_id:
            # Return the inserted document's ID
            return {"message": "Journal added successfully", "journal_id": str(result.inserted_id)}
        else:
            # If insertion failed, raise an HTTPException with a 500 status code
            return {"message": "Goal not added, error", "status_code" : 500}


@router.post("/modify_journal")
async def modify_goal(request_body: JournalData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        journal_id = request_body.journal_id
        result = journal_collection.update_one({"journal_id": journal_id}, {"$set": {"content" : request_body.content}})
        if result.modified_count == 1:
            return {"message": "Journal updated successfully"}
        else:
            return {"message": "Failed to update journal"}