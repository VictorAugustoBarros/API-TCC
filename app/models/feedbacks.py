from datetime import datetime
from dataclasses import dataclass
from app.connections.arangodb import ArangoDB


@dataclass
class Feedbacks:
    # @TODO -> Pensar no que é necessário salvar no feedback (5 questões???)
    objetivo_key: str
    descricao: str
    nota_geral: int
    data_feedback: str = datetime.strftime(datetime.now(), "%m/%d/%Y %H:%M:%S"),


class FeedbacksModel(ArangoDB):
    def __init__(self):
        self.collection_name = "Feedbacks"
        super().__init__(collection=self.collection_name)

    def create_feedback(self, feedback: Feedbacks):
        return self.insert(**feedback.__dict__)

    def delete_feedback(self, feedback_key: str):
        self.delete_by_key(key=feedback_key)
