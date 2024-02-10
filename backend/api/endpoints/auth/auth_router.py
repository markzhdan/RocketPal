from fastapi import APIRouter
from ..auth import auth_controller

router = APIRouter(prefix = "/api")

router.post("/login")(auth_controller.login_for_access_token)
router.post("/register")(auth_controller.register_user)
router.get("/me")(auth_controller.verify_user)