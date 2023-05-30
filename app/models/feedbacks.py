from datetime import datetime
from dataclasses import dataclass
from app.connections.arangodb import ArangoDB


# Em termos de progresso diário, qual foi o seu desempenho hoje, em uma escala de 1 a 10?
# Avalie o nível de dificuldade dos desafios enfrentados hoje, em uma escala de 1 a 10.
# Em uma escala de 1 a 10, qual é a sua satisfação geral com o progresso feito até agora?
# Quão perto você está de atingir o objetivo, em uma escala de 1 a 10?
# Avalie a qualidade e a eficácia das ações tomadas hoje, em uma escala de 1 a 10.


@dataclass
class Questoes:
    questao_progresso: int
    questao_dificuldade: int
    questao_satisfacao: int
    questao_atingimento: int
    questao_eficacia: int


@dataclass
class Feedbacks:
    user_key: str
    objetivo_key: str
    questoes: Questoes
    observacao: str
    data_feedback: str
    data_insert: str = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")


class FeedbacksModel(ArangoDB):
    def __init__(self):
        self.collection_name = "Feedbacks"
        super().__init__(collection=self.collection_name)

    def create_feedback(self, feedback: Feedbacks):
        return self.insert(**feedback.__dict__)

    def find_user_feedbacks(self, user_key: str):
        aql_query = f"""
            FOR feedback IN {self.collection_name}
                FILTER feedback.user_key == '{user_key}' 
                RETURN feedback
        """
        documents = self.aql_query(aql=aql_query)
        return [document for document in documents]

    def find_feedback(self, objetivo_key: str):
        aql_query = f"""
            FOR feedback IN {self.collection_name}
                FILTER feedback.objetivo_key == '{objetivo_key}'
                RETURN feedback
        """
        documents = self.aql_query(aql=aql_query)
        return [document for document in documents]

    def delete_feedback(self, feedback_key: str):
        self.delete_by_key(key=feedback_key)
