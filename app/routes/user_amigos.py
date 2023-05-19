from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.users_amigos import UsersAmigosModel, UserAmigos

routes_user_amigos = APIRouter()


@routes_user_amigos.post("/amigos/create")
async def create_amizade(user_amigos: UserAmigos):
    users_amigos_model = UsersAmigosModel()

    user_amigo_key = users_amigos_model.insert_user_amigos(user_id=user_amigos.user_id,
                                                           amigos_user_id=user_amigos.amigo_user_id)
    return JSONResponse(
        status_code=200, content={"message": "Amizade criada com sucesso!", "user_amigo_key": user_amigo_key}
    )


@routes_user_amigos.post("/amigos/get")
async def buscar_amizade(request: Request):
    request_body = await request.json()
    users_amigos_model = UsersAmigosModel()

    amigos = users_amigos_model.get_amigos_by_user_id(user_id=request_body.get("user_id"))
    return JSONResponse(
        status_code=200, content=amigos
    )
