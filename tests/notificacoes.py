from unittest import TestCase
from app.models.notificacoes import NotificacoesModel, Notificacao
from tests.shared.create_tests import CreateTests


class NotificacoesTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.notificacoes_model = NotificacoesModel()
        cls.create_tests = CreateTests()

    def test_create_notificacao(self):
        # Criação Notificação
        user1 = self.create_tests.create_user()
        user2 = self.create_tests.create_user()

        criterio = self.notificacoes_model.create_notificacao(
            Notificacao(
                user_key_origem=user1.key,
                user_key_destinatario=user2.key,
                amizade=True
            )
        )

        # Verificando criação Notificação
        notificacoes = self.notificacoes_model.find_notificacao(user_key=user2.key)

        # Exclusão Notificação
        self.notificacoes_model.delete_notificacao(notificacao_key=criterio.key)

        self.assertNotEquals(notificacoes, [])
