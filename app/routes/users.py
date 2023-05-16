from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.users import UsersModel, User, LoginUser

routes_users = APIRouter()


@routes_users.post("/users/login")
async def login(login_user: LoginUser):
    user_model = UsersModel()
    user = user_model.find_user_login(login_user=login_user)
    if not user:
        return JSONResponse(status_code=200, content={})

    return JSONResponse(status_code=200, content={"user_id": user._id})


@routes_users.get("/users/{key}")
async def get_user(key: str):
    users_model = UsersModel()
    user = users_model.find_user_by_key(key=key)
    if not user:
        return JSONResponse(
            status_code=200, content={"message": "Usuário não encontrado!"}
        )

    return JSONResponse(status_code=200, content=user)


@routes_users.post("/users")
async def create_user(user: User):
    users_model = UsersModel()

    has_user = users_model.find_user_by_email(email=user.email)
    if has_user:
        return JSONResponse(
            status_code=200, content={"message": "Email já cadastrado!"}
        )

    has_user = users_model.find_user_by_username(username=user.username)
    if has_user:
        return JSONResponse(
            status_code=200, content={"message": "Username já utilizado!"}
        )

    users_model.insert_user(user=user)
    return JSONResponse(
        status_code=200, content={"message": "Usuário cadastrado com sucesso!"}
    )


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
