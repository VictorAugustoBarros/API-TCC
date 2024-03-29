from datetime import datetime
from app.connections.arangodb import ArangoDB
from app.utils.utils import remove_critical_data


class UsersAmigosModel(ArangoDB):
    def __init__(self):
        self.collection_name = "UsersAmigos"
        super().__init__(collection=self.collection_name, edge=True)

    def insert_user_amigos(self, user_id: str, amigo_id: str):
        aresta = {
            "_from": user_id,
            "_to": amigo_id,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        return self.insert(**aresta)

    def delete_user_amigos(self, user_amigo_key: str):
        self.delete_by_key(key=user_amigo_key)

    def find_user_amigo(self, user_id: str, amigo_id: str):
        aql_query = f"""
            FOR doc IN {self.collection_name}
            FILTER doc._from == '{user_id}' AND doc._to == '{amigo_id}' 
                RETURN doc
        """
        documents = self.aql_query(aql=aql_query)
        if len([document for document in documents]) > 0:
            return True

        return False

    def is_friend(self, user_id: str, user_id_find: str):
        aql_query = f"""
                    FOR user_amigo IN {self.collection_name}
                    FILTER user_amigo._from == '{user_id}' && user_amigo._to == '{user_id_find}' 
                    RETURN user_amigo
                """
        documents = self.aql_query(aql=aql_query)
        if documents:
            return True
        return False

    def find_amigos_by_user_id(self, user_id: str):
        aql_query = f"""
            FOR doc IN {self.collection_name}
            FILTER doc._from == '{user_id}'
            FOR user IN Users
                FILTER user._id == doc._to
                RETURN {{user, data: doc.data}}
        """
        documents = self.aql_query(aql=aql_query)
        for document in documents:
            document.get("user")["data"] = document.get("data")

            document_ok = remove_critical_data(
                data=document.get("user"),
                remove_data=["_id", "_rev", "__pydantic_initialised__"],
            )

            document.clear()
            document.update(document_ok)

        return [document for document in documents]

    def find_relacionamentos_sugestao(self, user_id: str):
        aql_query = f"""
            LET startVertex = '{user_id}'
            FOR v, e, p IN 1..2 OUTBOUND startVertex {self.collection_name}
                LIMIT 5
                FILTER e._to == v._id 
                FILTER v._id != startVertex
                RETURN DISTINCT v
        """
        documents = self.aql_query(aql=aql_query)
        amigos = []
        for document in documents:
            document_ok = remove_critical_data(
                data=document,
                remove_data=[
                    "_key",
                    "_rev",
                    "password",
                    "followers",
                    "following",
                    "user_banner",
                ],
            )

            document_ok.update({"enviarSolicitacaoAtivo": True})

            amigos.append(document_ok)

        return amigos
