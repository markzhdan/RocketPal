from pydantic import BaseModel

class JournalData(BaseModel):
    journal_id : str
    date : str
    content : str


class RemoveJournalData(BaseModel):
    journal_id : str