from app.utils.utils import remove_critical_data
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.objetivos import ObjetivosModel, Objetivo
from app.models.objetivos_users import ObjetivosUsuarioModel

routes_objetivos = APIRouter()

from app.validatores.token_validator import token_validation


@routes_objetivos.post("/api/objetivos")
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


@routes_objetivos.put("/api/objetivos")
@token_validation
async def update_objetivo(request: Request):
    try:
        body = await request.json()

        objetivos_model = ObjetivosModel()

        objetivo = Objetivo(
            titulo=body.get("titulo"),
            categoria=body.get("categoria"),
            descricao=body.get("descricao"),
            imagem=body.get("imagem"),
            data_fim=body.get("dataFim"),
            key=body.get("key"),
        )
        objetivos_model.update_objetivo(objetivo_key=objetivo.key, objetivo=objetivo)
        return JSONResponse(status_code=200, content={"success": True})

    except Exception as error:
        print(error)
        return JSONResponse(
            status_code=400,
            content={"message": "Falha ao atualizar Objetivo!"},
        )


@routes_objetivos.get("/api/objetivos")
@token_validation
async def get_objetivos_user(request: Request):
    user_data = request.state.token
    objetivos_user_model = ObjetivosUsuarioModel()
    objetivos = objetivos_user_model.get_objetivo_user(user_id=user_data.get("id"))

    for objetivo in objetivos:
        objetivo.update(
            remove_critical_data(data=objetivo, remove_data=["_rev", "_id"])
        )

    return JSONResponse(status_code=200, content=objetivos if objetivos else [])


@routes_objetivos.get("/api/objetivos/{objetivo_key}")
@token_validation
async def get_objetivos_user(request: Request):
    objetivo_key = request.path_params.get("objetivo_key")

    objetivos_model = ObjetivosModel()
    objetivo = objetivos_model.find_objetivo(objetivo_key=objetivo_key)

    return JSONResponse(
        status_code=200,
        content={
            "titulo": objetivo.get("titulo"),
            "categoria": objetivo.get("categoria"),
            "dataFim": objetivo.get("data_fim"),
            "imagem": objetivo.get("imagem"),
            "descricao": objetivo.get("descricao"),
        },
    )


@routes_objetivos.delete("/api/objetivos/{objetivo_key}")
@token_validation
async def remove_objetivos_user(request: Request):
    try:
        objetivo_key = request.path_params.get("objetivo_key")

        objetivos_model = ObjetivosModel()
        objetivos_model.delete_objetivo(objetivo_key=objetivo_key)

        return JSONResponse(
            status_code=200,
            content={"success": True},
        )

    except Exception:
        return JSONResponse(
            status_code=400,
            content={"error": "Falha ao remover objetivo"},
        )
