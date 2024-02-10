from fastapi import APIRouter
from api.endpoints.ai import ai_controller

router = APIRouter(prefix = "/api")

router.post("/generate_response")(ai_controller.generate_response)