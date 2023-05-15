import json
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

routes_criterios = APIRouter()

from app.models.criterios import Criterio, CriteriosModel


@routes_criterios.post("/criterios")
async def insert(criterio: Criterio):
    criterio_model = CriteriosModel()
    criterio_model.insert_criterio(criterio=criterio)
    return JSONResponse(status_code=200, content={"success": True, "criterio": criterio.__dict__})


@routes_criterios.delete("/criterios/{key}")
async def delete(key: str):
    criterio_model = CriteriosModel()
    criterio_model.delete(key=key)
    return JSONResponse(
        status_code=200, content={"message": "Critério deletado com sucesso!"}
    )
