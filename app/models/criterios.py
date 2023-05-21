from dataclasses import dataclass
from app.connections.arangodb import ArangoDB


@dataclass
class Criterio:
    nome: str
    descricao: str


class CriteriosModel(ArangoDB):
    def __init__(self):
        super().__init__(collection="Criterios")

    def create_criterio(self, criterio: Criterio):
        return self.insert(**criterio.__dict__)

    def find_criterio(self, criterio_key: str):
        if criterio := self.find(data={"_key": criterio_key}):
            return criterio[0]
        return criterio

    def delete_criterio(self, criteiro_key: str):
        self.delete_by_key(key=criteiro_key)
