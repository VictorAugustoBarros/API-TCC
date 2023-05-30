from datetime import datetime
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app.models.feedbacks import FeedbacksModel, Feedbacks, Questoes
from app.models.objetivos import ObjetivosModel
from app.validatores.token_validator import token_validation
from app.utils.utils import datas_anteriores, ordenar_datas

routes_feedback = APIRouter()


@routes_feedback.post("/api/feedbacks")
@token_validation
async def insert(request: Request):
    user_data = request.state.token
    request_body = await request.json()

    objetivo_key = request_body.get("objetivoKey")
    data_feedback = request_body.get("dataFeedback")
    questao1 = request_body.get("questao1")
    questao2 = request_body.get("questao2")
    questao3 = request_body.get("questao3")
    questao4 = request_body.get("questao4")
    questao5 = request_body.get("questao5")
    observacao = request_body.get("observacao")

    feedback = Feedbacks(
        user_key=user_data.get("key"),
        objetivo_key=objetivo_key,
        observacao=observacao,
        data_feedback=data_feedback,
        questoes=Questoes(
            questao_progresso=int(questao1),
            questao_dificuldade=int(questao2),
            questao_satisfacao=int(questao3),
            questao_atingimento=int(questao4),
            questao_eficacia=int(questao5)
        ),
    )

    feedbacks_model = FeedbacksModel()
    feedbacks_model.create_feedback(feedback=feedback)

    return JSONResponse(
        status_code=200,
        content={"success": True},
    )


@routes_feedback.post("/api/feedbacks/pendentes")
@token_validation
async def generate(request: Request):
    user_data = request.state.token

    feedbacks_model = FeedbacksModel()

    return JSONResponse(
        status_code=200,
        content={"success": True},
    )


@routes_feedback.post("/api/feedbacks/generate")
@token_validation
async def generate(request: Request):
    user_data = request.state.token

    request_body = await request.json()
    objetivo_key = request_body.get("key")

    objetivos_model = ObjetivosModel()
    objetivo = objetivos_model.find_objetivo(objetivo_key=objetivo_key)
    if not objetivo:
        return JSONResponse(
            status_code=200,
            content={"error": "Objetivo não encontrado!"},
        )

    data_inicio = objetivo.get("data_inicio")
    feedbacks_pendentes = datas_anteriores(data=data_inicio)

    feedbacks_model = FeedbacksModel()
    feedbacks_concluidos = feedbacks_model.find_feedback(objetivo_key=objetivo_key)

    feedbacks_concluidos_data = [datetime.strptime(feedback.get("data_feedback"), "%d/%m/%Y").strftime("%Y-%m-%d") for
                                 feedback in feedbacks_concluidos]

    for feedback_data in feedbacks_concluidos_data:
        if feedback_data in feedbacks_pendentes:
            feedbacks_pendentes.remove(feedback_data)

    return JSONResponse(
        status_code=200,
        content={
            "concluidos": feedbacks_concluidos,
            "pendentes": feedbacks_pendentes
        },
    )


@routes_feedback.get("/api/feedbacks/{objetivo_key}")
@token_validation
async def get_feedbacks(request: Request):
    user_data = request.state.token
    objetivo_key = request.path_params.get("objetivo_key")

    objetivos_model = ObjetivosModel()
    objetivo = objetivos_model.find_objetivo(objetivo_key=objetivo_key)
    if not objetivo:
        return JSONResponse(
            status_code=200,
            content={"error": "Objetivo não encontrado!"},
        )

    feedbacks_model = FeedbacksModel()
    feedbacks_concluidos = feedbacks_model.find_feedback(objetivo_key=objetivo_key)

    feedbacks_concluidos_ok = []
    for feedbacks_concluido in feedbacks_concluidos:
        feedbacks_concluidos_ok.append({
            "key": feedbacks_concluido.get("_key"),
            "data": feedbacks_concluido.get("data_feedback"),
            "observacao": feedbacks_concluido.get("observacao"),
        })

    data_inicio = objetivo.get("data_inicio")
    feedbacks_pendentes = datas_anteriores(data=data_inicio)

    feedbacks_concluidos_data = [datetime.strptime(feedback.get("data_feedback"), "%d/%m/%Y").strftime("%Y-%m-%d") for feedback in feedbacks_concluidos]

    for feedback_data in feedbacks_concluidos_data:
        if feedback_data in feedbacks_pendentes:
            feedbacks_pendentes.remove(feedback_data)

    return JSONResponse(
        status_code=200,
        content={
            "concluidos": feedbacks_concluidos_ok,
            "pendentes": ordenar_datas(feedbacks_pendentes)
        },
    )

