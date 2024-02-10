from fastapi import APIRouter
from ..goals import goals_controller

router = APIRouter(prefix = "/api")

router.get("/goals")(goals_controller.get_goals)
router.post("/add_goal")(goals_controller.add_goal)
router.post("/modify_goal")(goals_controller.modify_goal)
router.post("/remove_goal")(goals_controller.remove_goal)