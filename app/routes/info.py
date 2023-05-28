from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from models.notificacoes import NotificacoesModel
from models.objetivos_users import ObjetivosUsuarioModel
from models.users_amigos import UsersAmigosModel
from validatores.token_validator import token_validation

from app.models.users import UsersModel

routes_info = APIRouter()


@routes_info.get("/api/info/user_card")
@token_validation
async def get_user_card(request: Request):
    try:
        user_data = request.state.token

        users_amigos_model = UsersAmigosModel()
        amigos = users_amigos_model.find_amigos_by_user_id(user_id=user_data.get("id"))

        objetivos_user_model = ObjetivosUsuarioModel()
        objetivos = objetivos_user_model.get_objetivo_user(user_id=user_data.get("id"))

        users_model = UsersModel()
        user = users_model.find_user_by_key(user_key=user_data.get("key"))

        return JSONResponse(
            status_code=200,
            content={
                "qntObjetivos": len(objetivos),
                "qntObjetivosConcluidos": 0,
                "qntAmigos": len(amigos),
                "username": user.get("username"),
                "email": user.get("email"),
                "userIcon": user.get("user_icon"),
            },
        )

    except Exception as error:
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao buscar informações!"},
        )


@routes_info.get("/api/info/lista_amigos")
@token_validation
async def get_lista_amigos(request: Request):
    try:
        user_data = request.state.token

        users_amigos_model = UsersAmigosModel()
        amigos = users_amigos_model.find_amigos_by_user_id(user_id=user_data.get("id"))

        lista_amigos = []
        for amigo in amigos:
            lista_amigos.append(
                {
                    "username": amigo.get("username"),
                    "userIcon": amigo.get("user_icon"),
                }
            )

        return JSONResponse(
            status_code=200,
            content=lista_amigos,
        )

    except Exception as error:
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao buscar informações!"},
        )


@routes_info.get("/api/info/user_perfil/{username}")
@token_validation
async def get_user(request: Request):
    try:
        user_token = request.state.token

        username = request.path_params.get("username")

        users_model = UsersModel()
        user = users_model.find_user_username(username=username)
        if not user:
            return JSONResponse(
                status_code=200, content={"error": "Usuário não encontrado!"}
            )

        notificacao_model = NotificacoesModel()
        friend_request = notificacao_model.has_send_notificao(user_key=user.get("_key"))

        user_amigo_model = UsersAmigosModel()
        is_friend = user_amigo_model.is_friend(user_id=user_token.get("id"), user_id_find=user.get("_id"))

        return JSONResponse(
            status_code=200,
            content={
                "username": user.get("username"),
                "userIcon": user.get("user_icon"),
                "userBanner": user.get("user_banner"),
                "friendRequest": friend_request,
                "isFriend": is_friend,
            },
        )

    except Exception as error:
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao buscar informações!"},
        )
