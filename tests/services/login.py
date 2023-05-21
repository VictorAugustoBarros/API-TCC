from unittest import TestCase

from tests.shared.create_tests import CreateTests
from app.services.login import Login
from app.models.users import UsersModel, User


class LoginTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.create_tests = CreateTests()
        cls.user_model = UsersModel()
        cls.login = Login()

    def test_login_user(self):
        email = "teste@teste.com"
        password = "teste123"
        user = User(
            name="UserTest",
            email=email,
            password=password,
            username="teste",
            followers=10,
            following=50,
        )
        user_database = self.user_model.create_user(user=user)

        login_success = self.login.login_user(email=email, password=password)
        self.user_model.delete_user(key=user_database.key)

        self.assertTrue(login_success.get("success"))

    def test_login_user_error(self):
        email = "teste@teste.com"
        user = User(
            name="UserTest",
            email=email,
            password="teste123",
            username="teste",
            followers=10,
            following=50,
        )
        user_database = self.user_model.create_user(user=user)

        login_success = self.login.login_user(email=email, password="passwordError")
        self.user_model.delete_user(key=user_database.key)

        self.assertFalse(login_success.get("success"))
        self.assertEqual(login_success.get("error"), "Usuário não encontrado!")

