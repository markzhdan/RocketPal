import requests
import uuid
import json
from bson import ObjectId
from pydantic import BaseModel
register_url = "http://127.0.0.1:8000/api/register"
login_url = "http://127.0.0.1:8000/api/login/"
goals_url = "http://127.0.0.1:8000/api/goals/"
add_goal_url = "http://127.0.0.1:8000/api/add_goal"
modify_goal_url = "http://127.0.0.1:8000/api/modify_goal"
auth_me_url = "http://127.0.0.1:8000/api/me"
remove_goal_url = "http://127.0.0.1:8000/api/remove_goal"
from pydantic import BaseModel

valid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjMzIyNTRmNi05NmU1LTQ3NzctOTM0Yy00MmVjMTdjMTYwODciLCJleHAiOjE3MTM1ODE1NjJ9.s_rjGjlQZmCPxVQBFC9HRwHcryWn7FOolU0kIHXLYTo"

class RegisterData(BaseModel):
    name: str
    email: str
    password: str

class LoginData(BaseModel):
    email : str
    password : str


payload = {
        "user_id" : uuid.uuid4(),
        "name" : "Jae",
        "username": "parkjae433@gmail.com",
        "password": "monkeyboy123",
        "first_login" : True,
}

def register_user(payload):
    response = requests.post(register_url, json=payload)
    print(response.status_code)

def login_user(payload):
    response = requests.post(login_url, json = payload)
    print(response.json()['access_token'])
    return response.json()['access_token']

def test_authenticated_user(payload):
    # Simulate an authenticated user by providing a valid JWT token in the Authorization header
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwYTM2MWI4Yy0yMDAyLTRlMTYtYjA2Yy1kMDJiMjEwOThmZjQiLCJleHAiOjE3MDc1NDQ2OTV9.NCAwdQtnEnsnKvZj7vTMTiSZoziuJ6ScnctaOYS6HGw"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(goals_url, headers = headers)
    print(json.loads(response.content))

goal_data = {
    "name" :"yoikitenaki",
    "goal_id" : "0137ac72-cdb6-4eae-b680-390696c9d0b4",
    "user_id" :"0a361b8c-2002-4e16-b06c-d02b21098ff4",
    "icon" : "test",    
    "tasks" : [],
    "ptvalue" : 24
}

def add_goal():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwYTM2MWI4Yy0yMDAyLTRlMTYtYjA2Yy1kMDJiMjEwOThmZjQiJleHAiOjE3MDc1NjMyMTl9.IRPUpN6mQNGr0FXwpfon4__lNcGiRGuDNhodok7A2sY"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(add_goal_url, json = goal_data, headers = headers)
    print(response.status_code)


def modify_goal(new_data):
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwYTM2MWI4Yy0yMDAyLTRlMTYtYjA2Yy1kMDJiMjEwOThmZjQiLCJleHAiOjE3MDc1NjMyMTl9.IRPUpN6mQNGr0FXwpfon4__lNcGiRGuDNhodok2sY"
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.post(modify_goal_url, json = new_data, headers = headers)
    print(response.content)

def remove_goal(goal_id):
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwYTM2MWI4Yy0yMDAyLTRlMTYtYjA2Yy1kMDJiMjEwOThmZjQiLCJleHAiOjE3MDc1NjgzODN9.aeA_3NwZS75HIxhfZBi1cL5tjUweRja-FBXRDujvzw8"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(remove_goal_url, json = {"goal_id" : goal_id}, headers = headers)
    print(response.content)

def test_auth_me():
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.get(auth_me_url, headers = headers)
    print(response.content)

modify_goal(goal_data)

# login_user({
#                "email" : "park123@gmail.com",
#                "password" : "yo123"})


# print(LoginData.model_validate({"email" : "marker@gmail.com",
#             "password" : "Marker123"}))
    

# register_user({"name" : "jae",
#                "email" : "park123@gmail.com",
#                "password" : "yo123"})