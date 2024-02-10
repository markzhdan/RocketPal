from pydantic import BaseModel


class NewTaskData(BaseModel):
    name : str
    goal_id : str