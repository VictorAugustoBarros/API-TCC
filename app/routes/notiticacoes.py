from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from models.notificacoes import NotificacoesModel, Notificacao
from models.users import UsersModel
from validatores.token_validator import token_validation

routes_notificacoes = APIRouter()


@routes_notificacoes.get("/api/notificacao/amizade")
@token_validation
async def enviar_solicitacao_amizade(request: Request):
    try:
        user_data = request.state.token

        notificacoes_model = NotificacoesModel()
        notificacoes = notificacoes_model.find_notificacao(user_key=user_data.get("key"))
        if not notificacoes:
            return JSONResponse(
                status_code=200,
                content={"error": "Sem notificações"},
            )

        return JSONResponse(
            status_code=200,
            content=notificacoes,
        )

    except Exception as error:
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao buscar informações!"},
        )


@routes_notificacoes.delete("/api/notificacao/amizade/{key}")
@token_validation
async def get_user_card(request: Request):
    try:
        notificaco_key = request.path_params.get("key")

        notificacoes_model = NotificacoesModel()
        notificacoes_model.delete_notificacao(notificacao_key=notificaco_key)

        return JSONResponse(
            status_code=200,
            content={"success": True},
        )

    except Exception as error:
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao buscar informações!"},
        )


@routes_notificacoes.post("/api/notificacao/amizade")
@token_validation
async def get_user_card(request: Request):
    try:
        user_data = request.state.token
        request_body = await request.json()

        user = UsersModel().find_user_username(username=request_body.get("username"))

        notificacoes_model = NotificacoesModel()
        notificaco = Notificacao(
            user_key_origem=user_data.get("key"),
            user_key_destinatario=user.get("_key"),
            amizade=True
        )
        notificacoes_model.create_notificacao(notificaco)

        return JSONResponse(
            status_code=200,
            content={"success": True},
        )

    except Exception as error:
        print(error)
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao buscar informações!"},
        )
