from unittest import TestCase
from app.models.users_amigos import UsersAmigosModel
from tests.shared.create_tests import CreateTests


class UsersTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.users_amigos_model = UsersAmigosModel()
        cls.create_tests = CreateTests()

    def test_create_user(self):
        # Criaçao User
        user1 = self.create_tests.create_user()
        user2 = self.create_tests.create_user()

        user_amigo = self.users_amigos_model.insert_user_amigos(user_id=user1.id, amigo_id=user2.id)

        # Verificando criação User
        user_amigos = self.users_amigos_model.find_amigos_by_user_id(user_id=user1.id)

        # Exclusão User
        self.create_tests.delete_user(user_key=user1.key)
        self.create_tests.delete_user(user_key=user2.key)
        self.users_amigos_model.delete_user_amigos(user_amigo_key=user_amigo.key)

        # Validação Testes
        self.assertIsNotNone(user_amigos)
