from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from models.notificacoes import NotificacoesModel
from models.feedbacks import FeedbacksModel
from models.objetivos_users import ObjetivosUsuarioModel
from models.users_amigos import UsersAmigosModel
from validatores.token_validator import token_validation

from app.models.users import UsersModel
from app.utils.utils import contar_registros_por_mes

routes_evolucao = APIRouter()


@routes_evolucao.get("/api/evolucao/objetivos")
@token_validation
async def get_evolucao(request: Request):
    try:
        user_data = request.state.token

        objetivos_usuario_model = ObjetivosUsuarioModel()
        objetivos = objetivos_usuario_model.get_objetivo_user(user_id=user_data.get("id"))

        objetivos_evolucao = {
            "quantidade": {
                "Objetivos Concluidos": 0,
                "Objetivos em andamento": len(objetivos),
                "Objetivos cancelados": 0,
            },
            "quantidade_mes": contar_registros_por_mes([objetivo.get("data_inicio") for objetivo in objetivos]),
            "categorias": {},
        }
        for objetivo in objetivos:
            if objetivo.get("categoria") not in objetivos_evolucao["categorias"].keys():
                objetivos_evolucao["categorias"][objetivo.get("categoria")] = 0

            objetivos_evolucao["categorias"][objetivo.get("categoria")] += 1

        return JSONResponse(
            status_code=200,
            content=objetivos_evolucao,
        )

    except Exception as error:
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao buscar informações!"},
        )


@routes_evolucao.get("/api/evolucao/amizades")
@token_validation
async def get_evolucao_amizades(request: Request):
    try:
        user_data = request.state.token

        user_amigos_model = UsersAmigosModel()
        amigos = user_amigos_model.find_amigos_by_user_id(user_id=user_data.get("id"))

        amigos_evolucao = {
            "quantidade": len(amigos),
            "quantidade_mes": contar_registros_por_mes([amigo.get("data") for amigo in amigos]),
        }

        return JSONResponse(
            status_code=200,
            content=amigos_evolucao,
        )

    except Exception as error:
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao buscar informações!"},
        )


@routes_evolucao.get("/api/evolucao/feedbacks")
@token_validation
async def get_evolucao_feedbacks(request: Request):
    try:
        user_data = request.state.token

        feedbacks_model = FeedbacksModel()
        feedbacks = feedbacks_model.find_user_feedbacks(user_key=user_data.get("key"))

        feedbacks_evolucao = {
            "quantidade": len(feedbacks),
            "quantidade_mes": contar_registros_por_mes([feedback.get("data_insert") for feedback in feedbacks]),
        }

        return JSONResponse(
            status_code=200,
            content=feedbacks_evolucao,
        )

    except Exception as error:
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao buscar informações!"},
        )
