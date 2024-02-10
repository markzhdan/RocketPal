from pydantic import BaseModel

class GoalData(BaseModel):
    name : str
    goal_id: str
    user_id : str
    icon : str
    tasks : list
    ptvalue : int