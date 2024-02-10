from fastapi import APIRouter
from api.endpoints.journal import journals_controller

router = APIRouter(prefix = "/api")

router.post("/add_journal")(journals_controller.add_journal)
router.post("/modify_journal")(journals_controller.modify_goal)