from pydantic import BaseModel
from typing import List, Dict, Union

class GoalData(BaseModel):
    name : str
    goal_id: str
    user_id : str
    tasks : list
    ptvalue : int

class NewGoalData(BaseModel):
    name : str

class RemoveGoalData(BaseModel):
    goal_id : str 