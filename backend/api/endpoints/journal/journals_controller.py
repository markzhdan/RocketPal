from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from api.models.journal import JournalData
from db.db import Database
from api.endpoints.helper import get_current_user
from bson.json_util import dumps
router = APIRouter()

client = Database().get_database()

journal_collection = client.Journals

oauth2_scheme_token = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/get_journals")
def get_journals(token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        journals = journal_collection.find({"user_id": user_id})
        journals_list = []
        for journal in journals:
            journals_list.append(journal)
        data = {"journals" : journals_list, "status_code" : 200}
        return dumps(data)
    else:
        return {"message": "Could not retrieve journals", "status_code" : 500}


@router.post("/add_journal")
def add_journal(request_body : JournalData, token: str = Depends(oauth2_scheme_token)):
    user_id = get_current_user(token)
    if user_id:
        data = request_body.model_dump()
        data['user_id'] = user_id
        result = journal_collection.insert_one(data)

        if result.inserted_id:
            # Return the inserted document's ID
            return {"message": "Journal added successfully", "status_code" : 200}
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
            return {"message": "Journal updated successfully", "status_code" : 200}
        else:
            return {"message": "Failed to update journal", "status_code" : 500}