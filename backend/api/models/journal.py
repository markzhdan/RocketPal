from pydantic import BaseModel

class JournalData(BaseModel):
    journal_id : str
    date : str
    content : str

