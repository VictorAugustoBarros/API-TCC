from pydantic import BaseModel
from app.connections.arangodb import ArangoDB


class UserAmigos(BaseModel):
    user_id: str
    amigo_user_id: str


class UsersAmigosModel(ArangoDB):
    def __init__(self):
        self.collection_name = "UsersAmigos"
        super().__init__(collection=self.collection_name, edge=True)

    def insert_user_amigos(self, user_id: str, amigos_user_id: str):
        aresta = {
            "_from": user_id,
            "_to": amigos_user_id
        }
        return self.insert(**aresta)

    def get_amigos_by_user_id(self, user_id: str):
        aql_query = f"""
                        FOR doc IN {self.collection_name}
                        FILTER doc._from == '{user_id}'
                        FOR user IN Users
                            FILTER user._id == doc._to
                            RETURN user
                    """
        documents = self.aql_query(aql=aql_query)
        return [document for document in documents]
