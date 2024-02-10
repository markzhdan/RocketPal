from fastapi import APIRouter
from api.endpoints.tasks import tasks_controller

router = APIRouter(prefix = "/api")

router.post("/add_task")(tasks_controller.add_task)