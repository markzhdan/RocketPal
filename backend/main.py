from fastapi import FastAPI
from api.endpoints.auth.auth_router import router as auth_router
from api.endpoints.goals.goals_router import router as goals_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, tags=["auth"])
app.include_router(goals_router, tags = ["goals"])
