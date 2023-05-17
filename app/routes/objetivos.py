from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.objetivos import ObjetivosModel, Objetivo
from app.models.objetivos_usuario import ObjetivosUsuarioModel

routes_objetivos = APIRouter()


@routes_objetivos.post("/objetivos")
async def create_objetivo(objetivo: Objetivo):
    objetivos_model = ObjetivosModel()
    objetivo_id = objetivos_model.insert_objetivo(objetivo=objetivo)

    objetivos_user_model = ObjetivosUsuarioModel()
    objetivos_user_model.insert_objetivo_user(objetivo_id=objetivo_id, user_id=objetivo.user_id)

    return JSONResponse(status_code=200, content={"objetivo_id": objetivo_id})


@routes_objetivos.post("/objetivos/user")
async def get_objetivos_user(request: Request):
    body = await request.json()
    objetivos_user_model = ObjetivosUsuarioModel()
    objetivos = objetivos_user_model.get_objetivo_user(user_id=body.get("user_id"))
    return JSONResponse(status_code=200, content=objetivos)
