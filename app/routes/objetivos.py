from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.users import UsersModel, User, LoginUser

routes_objetivos = APIRouter()


@routes_objetivos.post("/objetivos")
async def login(login_user: LoginUser):
    user_model = UsersModel()
    user = user_model.find_user_login(login_user=login_user)
    if not user:
        return JSONResponse(status_code=200, content={})

    return JSONResponse(status_code=200, content={"user_id": user._id})