from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.users import UsersModel, LoginUser
from app.services.jwt_manager import JwtManager

routes_login = APIRouter()


@routes_login.post("/auth/login")
async def login(login_user: LoginUser):
    user_model = UsersModel()
    user = user_model.find_user_login(login_user=login_user)
    if not user:
        return JSONResponse(status_code=200, content={"error": 'Usuário não encontrado!'})

    jwt_manager = JwtManager()
    token = jwt_manager.create_token(payload={
        "email": user.get("email"),
        "password": user.get("password")
    })

    return JSONResponse(status_code=200, content={"user": user.get("name"), "token": token})


@routes_login.get("/auth/verify")
async def check_token(request: Request):
    if not (token := request.headers.get("authorization")):
        return JSONResponse(status_code=400, content='Token não informado')

    jwt_manager = JwtManager()
    user_data = jwt_manager.verify_token(token=token)
    if not user_data:
        return JSONResponse(status_code=401, content='Não Autorizado!')

    return JSONResponse(status_code=200, content=user_data)
