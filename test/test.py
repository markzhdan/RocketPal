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
add_task_url = "http://127.0.0.1:8000/api/add_task"
add_journal_url = "http://127.0.0.1:8000/api/add_journal"
modify_journal_url = "http://127.0.0.1:8000/api/modify_journal"
generate_response_url = "http://127.0.0.1:8000/api/generate_response"

get_journals_url = "http://127.0.0.1:8000/api/get_journals"
remove_journal_url = "http://127.0.0.1:8000/api/remove_journal"

from pydantic import BaseModel

valid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjMzIyNTRmNi05NmU1LTQ3NzctOTM0Yy00MmVjMTdjMTYwODciLCJleHAiOjE3MDc3NjcyMTN9.D0pf6vGc9jirCJouDvEyU2InBtGeYnBHXSI8brduPR4"

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

new_goal_data = {
    "name" :"yoikitenaki",
}

new_journal_data = {
    "journal_id" : "123",
    "date" : "05/25/34",
    "content" : "yo im a bitch nvm i a12int"
}

def add_goal(goal_data):
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.post(add_goal_url, json = goal_data, headers = headers)
    print(response.content)

def modify_goal(new_data):
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwYTM2MWI4Yy0yMDAyLTRlMTYtYjA2Yy1kMDJiMjEwOThmZjQiLCJleHAiOjE3MDc1NjMyMTl9.IRPUpN6mQNGr0FXwpfon4__lNcGiRGuDNhodok2sY"
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.post(modify_goal_url, json = new_data, headers = headers)
    print(response.content)

def remove_goal(goal_id):
    headers = {"Authorization": f"Bearer {valid_token}"}
    response = requests.post(remove_goal_url, json = {"goal_id" : goal_id}, headers = headers)
    print(response.content)

def test_auth_me():
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.get(auth_me_url, headers = headers)
    print(response.content)

def add_task(new_task):
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.post(add_task_url, json = new_task, headers = headers)
    print(response.content)

def add_journal(new_journal):
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.post(add_journal_url, json = new_journal, headers = headers)
    print(response.content)

def modify_journal(modified_journal):
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.post(modify_journal_url, json = modified_journal, headers = headers)
    print(response.content)

def generate_response(text):
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.post(generate_response_url, json = text, headers = headers)
    print(response.content)

def get_journals():
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.get(get_journals_url, headers = headers)
    print(response.content)

def remove_journal():
    headers = {"Authorization": f"Bearer {valid_token}"}

    response = requests.post(remove_journal_url, json = {"journal_id" : "123"}, headers = headers)
    print(response.content)

remove_journal()
# goal_data = {
#   "goal_id": "5e8836fc-f1bc-487f-88c7-1037ce3b8b47",
#   "user_id": "c32254f6-96e5-4777-934c-42ec17c16087",
#   "tasks": [
#     {
#       "name": "Update online dating profile",
#       "completed": True,
#       "pointsValue": 10
#     },
#     {
#       "name": "Join a social club or group",
#       "completed": True,
#       "pointsValue": 10
#     },
#     {
#       "name": "Ask a friend to set you up on a date",
#       "completed": False,
#       "pointsValue": 10
#     }
#   ],
#   "ptvalue": 20
# }

# add_goal({"name" : "find a girlfriend"})

# add_task({"name" : "drink juice", "goal_id" : "1c0d6409-1d11-47ae-ad57-67c96b76607a"})

# remove_goal("a18f65be-79a1-48d6-ae7e-15e680165590")

# add_goal(new_goal_data)

# modify_goal(goal_data)
# login_user({
#                "email" : "park123@gmail.com",
#                "password" : "yo123"})


# print(LoginData.model_validate({"email" : "marker@gmail.com",
#             "password" : "Marker123"}))
    

# register_user({"name" : "jae",
#                "email" : "park123@gmail.com",
#                "password" : "yo123"})