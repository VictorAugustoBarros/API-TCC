from pydantic import BaseModel
from app.connections.arangodb import ArangoDB


class Objetivo(BaseModel):
    titulo: str
    categoria: str
    descricao: str
    user_key: str
    data_criacao: str = None
    _key: str = None


class ObjetivosModel(ArangoDB):
    def __init__(self):
        super().__init__(collection="Objetivos")

    def insert_objetivo(self, objetivo: Objetivo):
        self.insert(**objetivo.__dict__)
