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

class UserModel(BaseModel):
    name: str
    email: str
    password: str

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
    response = requests.post(login_url, data = payload)
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
    "goal_id" : "a40b5f75-2341-4dd5-8c71-c11fa0084449",
    "user_id" :"0a361b8c-2002-4e16-b06c-d02b21098ff4",
    "icon" : "test",    
    "tasks" : [],
    "ptvalue" : 21
}

def add_goal():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwYTM2MWI4Yy0yMDAyLTRlMTYtYjA2Yy1kMDJiMjEwOThmZjQiJleHAiOjE3MDc1NjMyMTl9.IRPUpN6mQNGr0FXwpfon4__lNcGiRGuDNhodok7A2sY"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(add_goal_url, json = goal_data, headers = headers)
    print(response.status_code)


def modify_goal(new_data):
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwYTM2MWI4Yy0yMDAyLTRlMTYtYjA2Yy1kMDJiMjEwOThmZjQiLCJleHAiOjE3MDc1NjMyMTl9.IRPUpN6mQNGr0FXwpfon4__lNcGiRGuDNhodok2sY"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(modify_goal_url, json = new_data, headers = headers)
    print(response.content)

def remove_goal(goal_id):
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwYTM2MWI4Yy0yMDAyLTRlMTYtYjA2Yy1kMDJiMjEwOThmZjQiLCJleHAiOjE3MDc1NjgzODN9.aeA_3NwZS75HIxhfZBi1cL5tjUweRja-FBXRDujvzw8"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(remove_goal_url, json = {"goal_id" : goal_id}, headers = headers)
    print(response.content)

def test_auth_me():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwYTM2MWI4Yy0yMDAyLTRlMTYtYjA2Yy1kMDJiMjEwOThmZjQiLCJleHAiOjE3MDc1NjgzODN9.aeA_3NwZS75HIxhfZBi1cL5tjUweRja-FBXRDujvzw8"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(auth_me_url, headers = headers)
    print(response.content)

register_user({
    "name" : "Jasons",
    "email" : "jasonderul2o@gmail.com",
    "password" : "JacksonTyson"
})

