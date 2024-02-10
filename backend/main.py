from fastapi import FastAPI
from api.endpoints.auth.auth_router import router as auth_router
from api.endpoints.goals.goals_router import router as goals_router
from api.endpoints.tasks.tasks_router import router as tasks_router
from api.endpoints.journal.journals_router import router as journals_router
from api.endpoints.ai.ai_router import router as ai_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
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
app.include_router(tasks_router, tags = ["tasks"])
app.include_router(journals_router, tags = ["journal"])
app.include_router(ai_router, tags = ["ai"])
