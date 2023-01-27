"""API STEVIE."""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes.users import routes_users

app = FastAPI()


def create_app():
    """create_app function."""
    app.include_router(routes_users)

    @app.get("/healthcheck")
    def health_check():
        """Função para checar a saúde da api."""
        return JSONResponse(status_code=200, content={"status": "active"})

    return app


create_app()

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000)
