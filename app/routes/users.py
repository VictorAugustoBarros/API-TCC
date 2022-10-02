from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.users import UsersModel, User

routes_users = APIRouter()


@routes_users.get("/users")
async def get_users():
    users_model = UsersModel()
    users = users_model.get_users()
    return JSONResponse(status_code=200, content=users)


@routes_users.get("/users/{user_key}")
async def get_user(user_key: str):
    users_model = UsersModel()
    user = users_model.get_user(user_key=user_key)
    return JSONResponse(status_code=200, content=user)


@routes_users.post("/users")
async def create_user(user: User):
    users_model = UsersModel()
    users_model.insert_user(
        email=user.email, username=user.username, password=user.password
    )
    return JSONResponse(
        status_code=200, content={"message": "Usuário cadastrado com sucesso!"}
    )


@routes_users.put("/users/{user_key}")
async def put(user_key: str, user: User):
    users_model = UsersModel()
    users_model.update_user(
        user_key=user_key,
        email=user.email,
        username=user.username,
        password=user.password,
    )
    return JSONResponse(
        status_code=200, content={"message": "Usuário atualizado com sucesso!"}
    )


@routes_users.delete("/users/{user_key}")
async def put(user_key: str):
    users_model = UsersModel()
    users_model.delete_user(user_key=user_key)
    return JSONResponse(
        status_code=200, content={"message": "Usuário deletado com sucesso!"}
    )
