from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.criterios import Criterio, CriteriosModel

routes_criterios = APIRouter()


@routes_criterios.post("/criterios")
async def insert(criterio: Criterio):
    criterio_model = CriteriosModel()
    criterio_database = criterio_model.create_criterio(criterio=criterio)
    return JSONResponse(
        status_code=200, content={"success": True, "criterio_key": criterio_database.key}
    )


@routes_criterios.delete("/criterios/{key}")
async def delete(key: str):
    criterio_model = CriteriosModel()
    criterio_model.delete_criterio(criteiro_key=key)
    return JSONResponse(
        status_code=200, content={"message": "Critério deletado com sucesso!"}
    )
