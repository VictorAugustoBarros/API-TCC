from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app.services.register import Register
from app.models.users import UsersModel, User
from models.user_criterios import UserCriteriosModel
from validatores.token_validator import token_validation

routes_users = APIRouter()


@routes_users.post("/api/users")
async def create_user(user: User):
    register_service = Register()
    user_register = register_service.register_user(user=user)

    if not user_register.get("success"):
        return JSONResponse(
            status_code=200,
            content=user_register,
        )

    return JSONResponse(
        status_code=200,
        content=user_register,
    )


@routes_users.get("/api/users")
@token_validation
async def get_user(request: Request):
    user_data = request.state.token

    users_model = UsersModel()
    user = users_model.find_user_by_key(user_key=user_data.get("key"))
    if not user:
        return JSONResponse(
            status_code=200, content={"message": "Usuário não encontrado!"}
        )

    user_criterio_model = UserCriteriosModel()
    user_criterios = user_criterio_model.find_criterio_by_user(user_id=user.get("_id"))

    return JSONResponse(
        status_code=200,
        content={
            "user": {
                "name": user.get("name"),
                "email": user.get("email"),
                "password": user.get("password"),
                "username": user.get("username"),
                "followers": user.get("followers"),
                "following": user.get("following"),
                "userIcon": user.get("user_icon"),
                "userBanner": user.get("user_banner"),
            },
            "hasCriterios": True if len(user_criterios) > 0 else False,
        },
    )


@routes_users.put("/api/users")
@token_validation
async def update_user(request: Request):
    user_data = request.state.token
    request_body = await request.json()

    users_model = UsersModel()
    users_model.update_user(key=user_data.get("key"), user=request_body)
    return JSONResponse(
        status_code=200, content={"message": "Usuário atualizado com sucesso!"}
    )


@routes_users.delete("/api/users")
async def delete_user(request: Request):
    user_data = request.state.token

    users_model = UsersModel()
    users_model.delete_user(key=user_data.get("key"))
    return JSONResponse(
        status_code=200, content={"message": "Usuário deletado com sucesso!"}
    )


@routes_users.get("/api/usernames")
@token_validation
async def get_usernames(request: Request):
    users_model = UsersModel()
    usernames = users_model.find_all_usernames()
    if not usernames:
        return JSONResponse(
            status_code=200, content={"error": "Usernames não encontrados!"}
        )

    return JSONResponse(status_code=200, content=usernames)


@routes_users.get("/api/usernames/{username}")
@token_validation
async def get_usernames(request: Request):
    username = request.path_params.get("username")
    users_model = UsersModel()
    user = users_model.find_user_username(username=username)
    if not user:
        return JSONResponse(
            status_code=200, content={"error": "Usuário não encontrado!"}
        )

    return JSONResponse(
        status_code=200,
        content={
            "name": user.get("name"),
            "email": user.get("email"),
            "password": user.get("password"),
            "username": user.get("username"),
            "followers": user.get("followers"),
            "following": user.get("following"),
            "userIcon": user.get("user_icon"),
            "userBanner": user.get("user_banner"),
        },
    )
