from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.users import UsersModel, User, LoginUser

routes_users = APIRouter()


@routes_users.post("/users")
async def create_user(user: User):
    """Criação de um novo usuário

    Args:
        user (User):
            name: str
            email: str
            password: str
            username: str

    Returns:
        200 -> {"message": "Email já cadastrado!"}
        200 -> {"message": "Username já utilizado!"}
        200 -> {"message": "Usuário cadastrado com sucesso!", "user": <user_id>}

    """
    users_model = UsersModel()

    has_user = users_model.find_user_by_email(email=user.email)
    if has_user:
        return JSONResponse(
            status_code=200, content={"success": False, "message": "Email já cadastrado!"}
        )

    has_user = users_model.find_user_by_username(username=user.username)
    if has_user:
        return JSONResponse(
            status_code=200, content={"success": False, "message": "Username já utilizado!"}
        )

    user_created = users_model.insert_user(user=user)
    return JSONResponse(
        status_code=200, content={"success": True, "message": "Usuário cadastrado com sucesso!", "user": user_created}
    )


@routes_users.post("/users/login")
async def login(login_user: LoginUser):
    user_model = UsersModel()
    user = user_model.find_user_login(login_user=login_user)
    if not user:
        return JSONResponse(status_code=200, content={})

    return JSONResponse(status_code=200, content={"user_id": user.get("_id")})


@routes_users.post("/users/id")
async def get_user(request: Request):
    user_request = await request.json()
    users_model = UsersModel()

    user = users_model.find_user_by_id(user_id=user_request.get("user_id"))
    if not user:
        return JSONResponse(
            status_code=200, content={"message": "Usuário não encontrado!"}
        )

    return JSONResponse(status_code=200, content=user)


@routes_users.put("/users/{key}")
async def put_user(key: str, user: User):
    users_model = UsersModel()
    users_model.update_user(key=key, user=user.__dict__)
    return JSONResponse(
        status_code=200, content={"message": "Usuário atualizado com sucesso!"}
    )


@routes_users.delete("/users/{key}")
async def delete_user(key: str):
    users_model = UsersModel()
    users_model.delete_user(key=key)
    return JSONResponse(
        status_code=200, content={"message": "Usuário deletado com sucesso!"}
    )
