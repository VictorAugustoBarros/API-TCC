from pydantic import BaseModel
from app.connections.arangodb import ArangoDB

from datetime import datetime


class Objetivo(BaseModel):
    titulo: str
    categoria: str
    descricao: str
    imagem: str
    data_fim: str
    data_inicio: str = datetime.now()


class ObjetivosModel(ArangoDB):
    def __init__(self):
        super().__init__(collection="Objetivos")

    def insert_objetivo(self, objetivo: Objetivo):
        return self.insert(**objetivo.__dict__)
