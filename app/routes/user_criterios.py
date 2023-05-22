# @TODO -> Refatorar
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from ahp.user_criterios import UserCriteriosModel, UserCriterio
from services.jwt_manager import JwtManager

routes_user_criterios = APIRouter()


@routes_user_criterios.get("/criterios")
async def get_criterios(request: Request):
    if not (token := request.headers.get("Authorization")):
        return JSONResponse(
            status_code=401, content={"message": "Favor informar o token!"}
        )

    # Buscar os dados do usuário pelo Token
    jwt_manager = JwtManager()
    user = jwt_manager.verify_token(token=token)

    user_criterio_model = UserCriteriosModel()
    user_criterios = user_criterio_model.find_criterio_by_user(user_id=user.get("id"))

    return JSONResponse(
        status_code=200,
        content={"success": True, "criterios": user_criterios.get("criterios")},
    )


@routes_user_criterios.post("/criterios/user")
async def config_criterios(request: Request):
    if not (token := request.headers.get("Authorization")):
        return JSONResponse(
            status_code=401, content={"message": "Favor informar o token!"}
        )

    criterios = await request.json()

    # Buscar os dados do usuário pelo Token
    jwt_manager = JwtManager()
    user = jwt_manager.verify_token(token=token)

    user_criterio_model = UserCriteriosModel()

    if user_criterio_id := user_criterio_model.find_criterio_by_user(
            user_id=user.get("id")
    ):
        user_criterio_model.delete_criterio(key=user_criterio_id.get("_key"))

    user_criterio = UserCriterio(user_id=user.get("id"), criterios=criterios)

    user_criterio_model.insert_criterio(user_criterio=user_criterio)

    return JSONResponse(
        status_code=200,
        content={"success": True, "message": "Criterios inseridos com sucesso!"},
    )
