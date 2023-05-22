from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.users_amigos import UsersAmigosModel
from app.models.users import UsersModel
from app.utils.errors import APIErrors
from app.validatores.token_validator import token_validation

routes_user_amigos = APIRouter()


@routes_user_amigos.post("/amigos")
@token_validation
async def create_amizade(request: Request):
    request_body = await request.json()
    if not (amigo_username := request_body.get("amigo_username")):
        return JSONResponse(
            status_code=200, content={"error": APIErrors.USER_ID_NOT_FOUND.value}
        )

    user_data = request.state.token
    users_amigos_model = UsersAmigosModel()

    amigo = UsersModel().find_user_username(username=amigo_username)

    amizade_existente = users_amigos_model.find_user_amigo(
        user_id=user_data.get("id"), amigo_id=amigo.get("_id")
    )
    if amizade_existente:
        return JSONResponse(
            status_code=200, content={"error": "Usuários já são amigos"}
        )

    user_amigo_key = users_amigos_model.insert_user_amigos(
        user_id=user_data.get("id"), amigo_id=amigo.get("id")
    )

    return JSONResponse(
        status_code=200,
        content={
            "message": "Amizade criada com sucesso!",
            "user_amigo_key": user_amigo_key.key,
        },
    )


@routes_user_amigos.get("/amigos")
@token_validation
async def buscar_amizade(request: Request):
    user_data = request.state.token

    users_amigos_model = UsersAmigosModel()
    amigos = users_amigos_model.find_amigos_by_user_id(user_id=user_data.get("id"))
    return JSONResponse(status_code=200, content=amigos)
