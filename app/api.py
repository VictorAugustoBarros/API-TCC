"""API STEVIE."""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.routes.users import routes_users
from app.routes.criterios import routes_criterios
from app.routes.user_criterios import routes_user_criterios
from app.routes.user_amigos import routes_user_amigos
from app.routes.objetivos import routes_objetivos
from app.routes.auth import routes_auth
from app.routes.info import routes_info
from app.routes.notiticacoes import routes_notificacoes

app = FastAPI()
origins = [
    "http://localhost:3001",
    "http://interlinker.com.br",
    "http://54.232.148.69/",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_app():
    """create_app function."""
    app.include_router(routes_users)
    app.include_router(routes_auth)
    app.include_router(routes_user_amigos)
    app.include_router(routes_criterios)
    app.include_router(routes_objetivos)
    app.include_router(routes_user_criterios)
    app.include_router(routes_info)
    app.include_router(routes_notificacoes)

    @app.get("/api/healthcheck")
    def health_check():
        """Função para checar a saúde da api."""
        return JSONResponse(status_code=200, content={"status": "active"})

    return app


create_app()

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081)
