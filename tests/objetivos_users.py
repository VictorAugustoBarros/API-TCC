from unittest import TestCase

from tests.shared.create_tests import CreateTests
from app.models.objetivos_users import ObjetivosUsuarioModel
from app.models.objetivos import Objetivo


class ObjetivosUsersTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.objetivos_user_model = ObjetivosUsuarioModel()
        cls.create_tests = CreateTests()

    def test_create_objetivo_user(self):
        # Criação User/Objetivo
        user = self.create_tests.create_user()
        objetivo = self.create_tests.create_objetivo()

        objetivo_user = self.objetivos_user_model.insert_objetivo_user(
            objetivo_id=user.id,
            user_id=objetivo.id
        )

        # Verificando criação ObjetivoUser
        objetivos = self.objetivos_user_model.get_objetivo_user(user_id=user.id)

        # Exclusão ObjetivoUser
        self.create_tests.delete_user(user_key=user.key)
        self.create_tests.delete_objetivo(objetivo_key=objetivo.key)
        self.objetivos_user_model.delete_objetivo_user(objetivo_user_key=objetivo_user.key)

        # Validação Testes
        self.assertIsNotNone(objetivos)
