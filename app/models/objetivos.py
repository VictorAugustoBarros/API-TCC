from dataclasses import dataclass
from app.connections.arangodb import ArangoDB

from datetime import datetime


class ObjetivoBase:
    titulo: str
    categoria: str
    descricao: str
    imagem: str
    data_fim: str
    data_inicio: str = datetime.now()


@dataclass
class Objetivo:
    titulo: str
    categoria: str
    descricao: str
    imagem: str
    data_fim: str
    data_inicio: str = datetime.now()
    key: str = None


class ObjetivosModel(ArangoDB):
    def __init__(self):
        super().__init__(collection="Objetivos")

    def find_objetivo(self, objetivo_key: str):
        objetivo = self.find(data={"_key": objetivo_key})
        if objetivo:
            return objetivo[0]
        return objetivo

    def insert_objetivo(self, objetivo: Objetivo):
        return self.insert(**objetivo.__dict__)

    def update_objetivo(self, objetivo_key, objetivo: Objetivo):
        return self.update(objetivo_key, objetivo.__dict__)

    def delete_objetivo(self, objetivo_key: str):
        self.delete_by_key(key=objetivo_key)
