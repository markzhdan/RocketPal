from fastapi import FastAPI
from api.endpoints.auth.auth_router import router as auth_router
from api.endpoints.goals.goals_router import router as goals_router

app = FastAPI()

app.include_router(auth_router, tags=["auth"])
app.include_router(goals_router, tags = ["goals"])
