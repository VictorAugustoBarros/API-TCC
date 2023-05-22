# @TODO -> Refatorar
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from ahp.user_criterios import UserCriteriosModel, UserCriterio

from app.validatores.token_validator import token_validation

routes_user_criterios = APIRouter()


@routes_user_criterios.get("/user_criterios")
@token_validation
async def get_criterios(request: Request):
    user_data = request.state.token

    user_criterio_model = UserCriteriosModel()
    user_criterios = user_criterio_model.find_criterio_by_user(user_id=user_data.get("id"))

    return JSONResponse(
        status_code=200,
        content=user_criterios.get("criterios") if user_criterios else {},
    )


@routes_user_criterios.post("/user_criterios")
@token_validation
async def config_criterios(request: Request):
    criterios = await request.json()
    user_data = request.state.token

    user_criterio_model = UserCriteriosModel()

    if user_criterio_id := user_criterio_model.find_criterio_by_user(
            user_id=user_data.get("id")
    ):
        user_criterio_model.delete_criterio(key=user_criterio_id.get("_key"))

    user_criterio = UserCriterio(user_id=user_data.get("id"), criterios=criterios)

    user_criterio_model.insert_criterio(user_criterio=user_criterio)

    return JSONResponse(
        status_code=200,
        content={"success": True, "message": "Criterios inseridos com sucesso!"},
    )
