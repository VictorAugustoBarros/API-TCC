from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.users import UsersModel, User, UserLogin

routes_users = APIRouter()


@routes_users.post("/users/login")
async def login(user: UserLogin):
    user_model = UsersModel()
    user = user_model.get_user_by_document(document=user.__dict__)
    if not user:
        return JSONResponse(status_code=200, content={})

    return JSONResponse(status_code=200, content=user)


@routes_users.get("/users")
async def get_users():
    users_model = UsersModel()
    users = users_model.get_all_users()
    if not users:
        return JSONResponse(
            status_code=200, content={"message": "Usuários não cadastrados!"}
        )

    return JSONResponse(status_code=200, content=users)


@routes_users.get("/users/{key}")
async def get_user(key: str):
    users_model = UsersModel()
    user = users_model.get_user_by_key(key=key)
    if not user:
        return JSONResponse(
            status_code=200, content={"message": "Usuário não encontrado!"}
        )

    return JSONResponse(status_code=200, content=user)


@routes_users.post("/users")
async def create_user(user: User):
    users_model = UsersModel()
    has_user = users_model.get_user_by_document(document={"email": user.email})
    if has_user:
        return JSONResponse(
            status_code=200, content={"message": "Usuário já cadastrado!"}
        )

    users_model.insert_user(
        email=user.email, username=user.username, password=user.password
    )
    return JSONResponse(
        status_code=200, content={"message": "Usuário cadastrado com sucesso!"}
    )


@routes_users.put("/users/{key}")
async def put(key: str, user: User):
    users_model = UsersModel()
    users_model.update_user(key=key, user=user.__dict__)
    return JSONResponse(
        status_code=200, content={"message": "Usuário atualizado com sucesso!"}
    )


@routes_users.delete("/users/{key}")
async def put(key: str):
    users_model = UsersModel()
    users_model.delete_user(key=key)
    return JSONResponse(
        status_code=200, content={"message": "Usuário deletado com sucesso!"}
    )
