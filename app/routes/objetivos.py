from app.utils.utils import remove_critical_data
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.objetivos import ObjetivosModel, Objetivo
from app.models.objetivos_users import ObjetivosUsuarioModel
from services.jwt_manager import JwtManager

routes_objetivos = APIRouter()

from app.validatores.token_validator import token_validation


@routes_objetivos.post("/objetivos")
@token_validation
async def create_objetivo(request: Request):
    body = await request.json()
    user_data = request.state.token

    objetivo = Objetivo(**body)

    objetivos_model = ObjetivosModel()
    objetivo_id = objetivos_model.insert_objetivo(objetivo=objetivo)

    objetivos_user_model = ObjetivosUsuarioModel()
    objetivos_user = objetivos_user_model.insert_objetivo_user(
        objetivo_id=objetivo_id.id, user_id=user_data.get("id")
    )

    return JSONResponse(status_code=200, content={"success": True})


@routes_objetivos.put("/objetivos")
@token_validation
async def update_objetivo(request: Request):
    body = await request.json()

    objetivos_model = ObjetivosModel()
    objetivo = Objetivo(**body)
    objetivo_id = objetivos_model.update_objetivo(objetivo_key=objetivo.key, objetivo=objetivo)
    return JSONResponse(status_code=200, content={"success": True})


@routes_objetivos.get("/objetivos")
@token_validation
async def get_objetivos_user(request: Request):
    user_data = request.state.token
    objetivos_user_model = ObjetivosUsuarioModel()
    objetivos = objetivos_user_model.get_objetivo_user(user_id=user_data.get("id"))

    for objetivo in objetivos:
        objetivo.update(remove_critical_data(data=objetivo, remove_data=["_rev", "_id"]))

    return JSONResponse(status_code=200, content=objetivos if objetivos else [])
