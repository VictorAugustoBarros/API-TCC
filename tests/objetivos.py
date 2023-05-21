from tests.shared.create_tests import CreateTests
from unittest import TestCase
from app.models.objetivos import ObjetivosModel, Objetivo


class ObjetivosTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.objetivos_model = ObjetivosModel()
        cls.create_tests = CreateTests()

    def test_create_objetivo(self):
        # Criação Objetivo
        objetivo = self.create_tests.create_objetivo()

        # Verificando criação Objetivo
        objetivo_database = self.objetivos_model.find_objetivo(objetivo_key=objetivo.key)

        # Exclusão Objetivo
        self.objetivos_model.delete_objetivo(objetivo_key=objetivo.key)

        # Validação Testes
        self.assertEqual(objetivo.key, objetivo_database.get("_key"))
