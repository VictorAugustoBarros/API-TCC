import uvicorn
from fastapi import FastAPI
from app.routes.users import routes_users


class Api:
    def __init__(self):
        self.app = FastAPI()
        self.port = 6000
        self.create_routes()

    def create_routes(self):
        self.app.include_router(routes_users)

    def run(self):
        uvicorn.run(app=self.app, port=self.port)


api = Api()

if __name__ == "__main__":
    api.run()
