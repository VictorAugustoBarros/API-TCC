from pydantic import BaseModel
from app.connections.arangodb import ArangoDB

from datetime import datetime


class Objetivo(BaseModel):
    titulo: str
    categoria: str
    descricao: str
    user_id: str
    imagem: str = None
    data_criacao: str = None
    _key: str = None


class ObjetivosModel(ArangoDB):
    def __init__(self):
        super().__init__(collection="Objetivos")

    def insert_objetivo(self, objetivo: Objetivo):
        objetivo.data_criacao = datetime.now()
        return self.insert(**objetivo.__dict__)
