from pydantic import BaseModel
from app.connections.arangodb import ArangoDB

from app.models.objetivos import Objetivo


class ObjetivosUsuarioModel(ArangoDB):
    def __init__(self):
        self.collection_name = "ObjetivosUsuario"
        super().__init__(collection="ObjetivosUsuario", edge=True)

    def insert_objetivo_user(self, objetivo_id: str, user_id: str):
        aresta = {"_from": objetivo_id, "_to": user_id}
        return self.insert(**aresta)

    def delete_objetivo_user(self, objetivo_user_key: str):
        self.delete_by_key(key=objetivo_user_key)

    def get_objetivo_user(self, user_id: str):
        aql_query = f"""
            FOR doc IN {self.collection_name}
            FILTER doc._from == '{user_id}'
            FOR objetivo IN Objetivos
                FILTER objetivo._id == doc._to
                RETURN objetivo
        """
        documents = self.aql_query(aql=aql_query)
        return [document for document in documents]
