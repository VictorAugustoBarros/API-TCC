from datetime import datetime, timedelta
from unittest import TestCase
from app.models.users import UsersModel, User
from tests.shared.create_tests import CreateTests


class UsersTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.users_model = UsersModel()
        cls.create_tests = CreateTests()

    def test_create_user(self):
        # Criaçao User
        user = self.create_tests.create_user()

        # Verificando criação User
        user_database = self.users_model.find_user_by_key(user_key=user.key)

        # Exclusão User
        self.users_model.delete_user(key=user_database.get("_key"))

        # Validação Testes
        self.assertEqual(user.key, user_database.get("_key"))
