from unittest import TestCase

from tests.shared.create_tests import CreateTests
from app.services.register import Register
from app.models.users import UsersModel, User


class RegisterTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.create_tests = CreateTests()
        cls.user_model = UsersModel()
        cls.register = Register()

    def test_register_user(self):
        user = User(
            name="UserTest",
            email="teste@teste.com",
            password="teste123",
            username="teste",
            followers=10,
            following=50,
        )
        register = self.register.register_user(user=user)

        self.user_model.delete_user(key=register.get("user")["key"])

        self.assertTrue(register.get("success"))

    def test_register_email_error(self):
        user1 = User(
            name="UserTest",
            email="teste2@teste.com",
            password="teste123",
            username="teste",
            followers=10,
            following=50,
        )
        register1 = self.register.register_user(user=user1)

        user2 = User(
            name="UserTest",
            email="teste2@teste.com",
            password="teste123",
            username="asdasdsada",
            followers=10,
            following=50,
        )
        register2 = self.register.register_user(user=user2)

        self.user_model.delete_user(key=register1.get("user")["key"])

        self.assertFalse(register2.get("success"))
        self.assertEqual(register2.get("error"), "Email já existe!")

    def test_register_username_error(self):
        user1 = User(
            name="UserTest",
            email="teste_user1@teste.com",
            password="teste123",
            username="teste3",
            followers=10,
            following=50,
        )
        register1 = self.register.register_user(user=user1)

        user2 = User(
            name="UserTest",
            email="teste_user2@teste.com",
            password="teste123",
            username="teste3",
            followers=10,
            following=50,
        )
        register2 = self.register.register_user(user=user2)

        self.user_model.delete_user(key=register1.get("user")["key"])

        self.assertFalse(register2.get("success"))
        self.assertEqual(register2.get("error"), "Username já existe!")
