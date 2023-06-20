from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.users_amigos import UsersAmigosModel
from app.models.users import UsersModel
from app.utils.errors import APIErrors
from app.validatores.token_validator import token_validation
from models.user_criterios import UserCriteriosModel
from app.ahp.ahp_method import AHP

routes_user_amigos = APIRouter()


@routes_user_amigos.post("/api/amigos")
@token_validation
async def create_amizade(request: Request):
    request_body = await request.json()
    if not (amigo_username := request_body.get("username")):
        return JSONResponse(
            status_code=200, content={"error": APIErrors.USER_ID_NOT_FOUND.value}
        )

    user_data = request.state.token
    users_amigos_model = UsersAmigosModel()

    amigo = UsersModel().find_user_username(username=amigo_username)

    amizade_existente = users_amigos_model.find_user_amigo(
        user_id=user_data.get("id"), amigo_id=amigo.get("_id")
    )
    if amizade_existente:
        return JSONResponse(
            status_code=200, content={"error": "Usuários já são amigos"}
        )

    user_amigo_key = users_amigos_model.insert_user_amigos(
        user_id=user_data.get("id"), amigo_id=amigo.get("_id")
    )

    users_amigos_model.insert_user_amigos(
        user_id=amigo.get("_id"), amigo_id=user_data.get("id")
    )

    return JSONResponse(
        status_code=200,
        content={
            "message": "Amizade criada com sucesso!",
            "user_amigo_key": user_amigo_key.key,
        },
    )


@routes_user_amigos.get("/api/amigos")
@token_validation
async def buscar_amizade(request: Request):
    user_data = request.state.token

    users_amigos_model = UsersAmigosModel()
    amigos = users_amigos_model.find_amigos_by_user_id(user_id=user_data.get("id"))
    return JSONResponse(status_code=200, content=amigos)


@routes_user_amigos.get("/api/amigos_relacionamentos")
@token_validation
async def buscar_relacionamentos(request: Request):
    user_data = request.state.token

    users_amigos_model = UsersAmigosModel()
    user_amigos_recomendacoes = users_amigos_model.find_relacionamentos_sugestao(
        user_id=user_data.get("id")
    )

    user_criterio_model = UserCriteriosModel()

    user_criterios = user_criterio_model.find_criterio_by_user(
        user_id=user_data.get("id")
    )

    user_criterios_recomendacao = []
    user_model = UsersModel()
    for user_recomendacao in user_amigos_recomendacoes:
        criterio_result = user_criterio_model.find_criterio_by_user(
            user_id=user_recomendacao.get("id")
        )
        if not criterio_result:
            continue

        user_recomendacao_data = user_model.find_user_by_id(
            user_id=criterio_result.get("user_id")
        )

        if criterio_result:
            user_criterios_recomendacao.append(
                {
                    "user_id": criterio_result.get("user_id"),
                    "username": user_recomendacao_data.get("username"),
                    "criterios": criterio_result.get("criterios"),
                    "name": user_recomendacao_data.get("name"),
                    "user_icon": user_recomendacao_data.get("user_icon"),
                }
            )

    if not user_criterios_recomendacao:
        return JSONResponse(status_code=200, content=[])

    resultado_ahp = AHP().build_matriz(
        user_criterios=user_criterios.get("criterios"),
        user_criterios_recomendacao=user_criterios_recomendacao,
    )

    concatenated_list = []
    for item1 in user_criterios_recomendacao:
        for item2 in resultado_ahp:
            if item1['user_id'] == item2['user_id']:
                concatenated_item = item2
                concatenated_item.update({
                    "user_icon": item1.get("user_icon"),
                    "name": item1.get("name"),
                    "enviarSolicitacaoAtivo": True,
                })

                concatenated_list.append(concatenated_item)

    maior_resultado = max(concatenated_list, key=lambda x: x['resultado'])

    for item in concatenated_list:
        if item == maior_resultado:
            item['recomendado'] = True
        else:
            item['recomendado'] = False

    return JSONResponse(status_code=200, content=concatenated_list)
