from unittest import TestCase
from app.models.criterios import CriteriosModel, Criterio


class CriteriosTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.criterios_model = CriteriosModel()

    def test_create_objetivo(self):
        # Criação Objetivo
        criterio = self.criterios_model.create_criterio(criterio=Criterio(
            nome="Criterio Teste",
            descricao="Teste123"
        ))

        # Verificando criação Objetivo
        criterio_database = self.criterios_model.find_criterio(criterio_key=criterio.key)

        # Exclusão Objetivo
        self.criterios_model.delete_criterio(criteiro_key=criterio.key)

        # Validação Testes
        self.assertEqual(criterio.key, criterio_database.get("_key"))
