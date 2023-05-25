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
            FOR notificaco IN {self.collection_name}
            FILTER notificaco.user_key_destinatario == '{user_key}'
            RETURN notificaco
        """
        notificacoes_ok = []
        notificacoes = self.aql_query(aql=aql_query)
        for notificacao in notificacoes:
            notificacoes_ok.append({
                "key": notificacao.get("_key"),
                "amizade": notificacao.get("amizade"),
            })

        return notificacoes_ok

    def delete_notificacao(self, notificacao_key: str):
        self.delete_by_key(key=notificacao_key)
