from app.utils.utils import remove_critical_data
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.objetivos import ObjetivosModel, Objetivo
from app.models.objetivos_users import ObjetivosUsuarioModel
from services.jwt_manager import JwtManager

routes_objetivos = APIRouter()


@routes_objetivos.post("/objetivos")
async def create_objetivo(request: Request):
    if not (token := request.headers.get("token")):
        return JSONResponse(
            status_code=401, content={"message": "Favor informar o token!"}
        )

    jwt_manager = JwtManager()
    user_data = jwt_manager.verify_token(token=token)

    body = await request.json()
    objetivo = Objetivo(**body)

    objetivos_model = ObjetivosModel()
    objetivo_id = objetivos_model.insert_objetivo(objetivo=objetivo)

    objetivos_user_model = ObjetivosUsuarioModel()
    objetivos_user_model.insert_objetivo_user(
        objetivo_id=objetivo_id, user_id=user_data.get("id")
    )

    return JSONResponse(status_code=200, content={"success": True})


@routes_objetivos.get("/objetivos")
async def get_objetivos_user(request: Request):
    if not (token := request.headers.get("token")):
        return JSONResponse(
            status_code=401, content={"message": "Favor informar o token!"}
        )

    jwt_manager = JwtManager()
    user_data = jwt_manager.verify_token(token=token)

    objetivos_user_model = ObjetivosUsuarioModel()
    objetivos = objetivos_user_model.get_objetivo_user(user_id=user_data.get("id"))

    for objetivo in objetivos:
        objetivo.update(remove_critical_data(data=objetivo, remove_data=["_rev"]))
    return JSONResponse(status_code=200, content={"objetivos": objetivos})
