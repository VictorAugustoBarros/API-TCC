from datetime import datetime
from unittest import TestCase
from app.models.feedbacks import Feedbacks, Questoes, FeedbacksModel
from tests.shared.create_tests import CreateTests


class FeedbacksTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.feedbacks_model = FeedbacksModel()
        cls.create_tests = CreateTests()

    def test_create_feedback(self):
        # Criação Feedback
        user = self.create_tests.create_user()
        objetivo = self.create_tests.create_objetivo()

        feedback = self.feedbacks_model.create_feedback(
            Feedbacks(
                user_key=user.key,
                objetivo_key=objetivo.key,
                data_feedback=datetime.strftime(datetime.now(), "%m/%d/%Y %H:%M:%S"),
                questoes=Questoes(
                    questao_dificuldade=3,
                    questao_progresso=2,
                    questao_satisfacao=7,
                    questao_atingimento=1,
                    questao_eficacia=8
                ),
                observacoes="Hoje foi um dia bem tranquilo"
            )
        )
        # Verificando criação
        feedback_database = self.feedbacks_model.find_feedback(user_key=user.key, objetivo_key=objetivo.key)

        # Exclusão Notificação
        self.feedbacks_model.delete_feedback(feedback_key=feedback.key)

        self.assertNotEqual(feedback_database, [])
