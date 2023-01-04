import uvicorn
from fastapi import FastAPI
from app.routes.users import routes_users
from fastapi.middleware.cors import CORSMiddleware


class Api:
    def __init__(self):
        self.app = FastAPI()
        self.port = 8000
        self.create_routes()
        self.cors()

    def create_routes(self):
        self.app.include_router(routes_users)

    def cors(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def run(self):
        uvicorn.run(app=self.app, port=self.port)


api = Api()

if __name__ == "__main__":
    api.run()
