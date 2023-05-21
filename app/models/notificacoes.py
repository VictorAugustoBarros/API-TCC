from dataclasses import dataclass
from app.connections.arangodb import ArangoDB


@dataclass
class Notificacao:
    user_key_origem: str
    user_key_destinatario: str
    descricao: str = ""
    amizade: bool = False


class NotificacoesModel(ArangoDB):
    def __init__(self):
        self.collection_name = "Notificacoes"
        super().__init__(collection=self.collection_name)

    def create_notificacao(self, notificacao: Notificacao):
        return self.insert(**notificacao.__dict__)

    def find_notificacao(self, user_key: str):
        aql_query = f"""
            FOR doc IN {self.collection_name}
            FILTER doc.user_key_destinatario == '{user_key}'
            FOR user IN Users
                FILTER user._key == doc.user_key_destinatario
                RETURN doc
        """
        documents = self.aql_query(aql=aql_query)
        return [document for document in documents]

    def delete_notificacao(self, notificacao_key: str):
        self.delete_by_key(key=notificacao_key)
