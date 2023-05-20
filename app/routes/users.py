from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.users import UsersModel, User, LoginUser
from models.users_amigos import UsersAmigosModel
from services.jwt_manager import JwtManager

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


@routes_users.get("/users")
async def get_user(request: Request):
    if not (token := request.headers.get("token")):
        return JSONResponse(
            status_code=401, content={"message": "Favor informar o token!"}
        )

    jwt_manager = JwtManager()
    user_data = jwt_manager.verify_token(token=token)
    key = user_data.get("key")

    users_model = UsersModel()

    user = users_model.find_user_by_key(user_key=key)
    if not user:
        return JSONResponse(
            status_code=200, content={"message": "Usuário não encontrado!"}
        )

    del user["_id"]
    del user["_rev"]
    del user["password"]
    user["key"] = user.pop("_key")

    users_amigos_model = UsersAmigosModel()
    amigos = users_amigos_model.get_amigos_by_user_id(user_id=user.get("_id"))
    for amigo in amigos:
        del amigo["_id"]
        del amigo["_rev"]
        amigo["key"] = amigo.pop("_key")

    return JSONResponse(status_code=200, content={
        "user": user,
        "amigos": amigos
    })


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
