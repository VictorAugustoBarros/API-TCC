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

    def find_notificacao(self, user_key: str, amizade: bool = False):
        aql_query = f"""
            FOR notificacao IN {self.collection_name}
            FILTER notificacao.user_key_destinatario == '{user_key}' && notificacao.amizade == {amizade}
            RETURN notificacao
        """
        notificacoes_ok = []
        notificacoes = self.aql_query(aql=aql_query)
        for notificacao in notificacoes:
            notificacoes_ok.append(
                {
                    "key": notificacao.get("_key"),
                    "amizade": notificacao.get("amizade"),
                    "descricao": notificacao.get("descricao"),
                }
            )

        return notificacoes_ok

    def has_send_notificao(self, user_key: str):
        aql_query = f"""
            FOR notificaco IN {self.collection_name}
            FILTER notificaco.user_key_destinatario == '{user_key}'
            RETURN notificaco
        """
        notificacoes = self.aql_query(aql=aql_query)
        if notificacoes:
            return True

        return False

    def find_friend_requests(self, user_from_key: str):
        aql_query = f"""
            FOR notificaco IN Notificacoes
                FILTER notificaco.user_key_destinatario == '{user_from_key}' &&  notificaco.amizade == true
                LET user = (
                    FOR user IN Users
                    FILTER user._key == notificaco.user_key_origem
                    RETURN user
                )
                RETURN {{notificaco, username: user[0].username}}
        """
        friend_requests_ok = []
        friend_requests = self.aql_query(aql=aql_query)
        for friend_request in friend_requests:
            friend_requests_ok.append(
                {
                    "key": friend_request.get("notificaco").get("_key"),
                    "username": friend_request.get("username"),
                }
            )

        return friend_requests_ok

    def delete_notificacao(self, notificacao_key: str):
        self.delete_by_key(key=notificacao_key)

    def delete_all_notificacao(self, user_key: str):
        aql_query = f"""
                    FOR notificaco IN {self.collection_name}
                    FILTER notificaco.user_key_destinatario == '{user_key}'
                    REMOVE notificaco IN {self.collection_name}
                """
        self.aql_query(aql=aql_query)
