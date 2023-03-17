import json
from pydantic import BaseModel
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

routes_criterios = APIRouter()


class Criterios(BaseModel):
    email: str
    password: str


teste = {
    "Nível Esforço": [{"criterio": "Período do Dia", "value": 7}],
    "Período do Dia": [{"criterio": "Nível Esforço", "value": 5}],
}

teste2 = {
    "Nível Esforço": [
        {"criterio": "Período do Dia", "value": 7},
        {"criterio": "Tempo Conclusão", "value": 2},
        {"criterio": "Nível Experiência", "value": 5},
        {"criterio": "Avaliação de Usuários", "value": 2},
    ],
    "Período do Dia": [
        {"criterio": "Nível Esforço", "value": 2},
        {"criterio": "Tempo Conclusão", "value": 2},
        {"criterio": "Nível Experiência", "value": 2},
        {"criterio": "Avaliação de Usuários", "value": 2},
    ],
    "Tempo Conclusão": [
        {"criterio": "Nível Esforço", "value": 2},
        {"criterio": "Período do Dia", "value": 5},
        {"criterio": "Nível Experiência", "value": 2},
        {"criterio": "Avaliação de Usuários", "value": 2},
    ],
    "Nível Experiência": [
        {"criterio": "Nível Esforço", "value": 2},
        {"criterio": "Período do Dia", "value": 5},
        {"criterio": "Tempo Conclusão", "value": 3},
        {"criterio": "Avaliação de Usuários", "value": 5},
    ],
    "Avaliação de Usuários": [
        {"criterio": "Nível Esforço", "value": 2},
        {"criterio": "Período do Dia", "value": 5},
        {"criterio": "Tempo Conclusão", "value": 2},
        {"criterio": "Nível Experiência", "value": 2},
    ],
}


@routes_criterios.post("/criterios")
async def criterios(request: Request):
    body = await request.body()
    request = json.loads(body.decode("utf-8"))

    # @TODO -> Inserir toda a lógica de inserção no ArangoDB
    return JSONResponse(status_code=200, content={"success": True, "request": request})
