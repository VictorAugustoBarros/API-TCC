from dataclasses import dataclass
from app.connections.arangodb import ArangoDB


@dataclass
class RecuperacaoSenha:
    email: str
    hash: str


class RecuperacaoSenhaModel(ArangoDB):
    def __init__(self):
        super().__init__(collection="RecuperacaoSenha")

    def insert_recuperacao_senha(self, recuperacao_senha: RecuperacaoSenha):
        return self.insert(**recuperacao_senha.__dict__)

    def find_recuperacao_senha(self, email: str, hash: str):
        if hash_recuperacao := self.find(data={"email": email, "hash": hash}):
            return hash_recuperacao[0]

        return hash_recuperacao

    def delete_recuperacao_senha(self, key: str):
        self.delete_by_key(key=key)
