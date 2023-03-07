from enum import Enum


class Criterios(Enum):
    """
    "Nível de Esforço" -> 1, 2, 3, 4, 5 (1 - Baixo esforço, 5 - Alto esforço)
    "Período do Dia" -> 1 (Manhã), 2 (Tarde), 3 (Noite)
    "Faixa de Idade" -> 1 (15-20), 2 (20-25), 3 (25-30), 4 (30-40), 5 (40-50)
    "Nível de Experiência" -> 1, 2, 3, 4, 5 (1 - Nenhuma experiência, 5 - Alta experiência)
    "Avaliação de Usuários" -> 1, 2, 3, 4, 5 (1 - Não gostou, 5 - Adorou)
    """

    esforco = "Nível de Esforço"
    periodo = "Período do Dia"
    faixa_idade = "Faixa de Idade"
    experiencia = "Nível de Experiência"
    avaliacao = "Avaliação de Usuários"

    @staticmethod
    def names():
        return [criterio.value for criterio in Criterios]

    @staticmethod
    def saaty():
        return [
            [1, 3, 5, 7, 9],
            [1 / 3, 1, 3, 5, 7],
            [1 / 5, 1 / 3, 1, 3, 5],
            [1 / 7, 1 / 5, 1 / 3, 1, 3],
            [1 / 9, 1 / 7, 1 / 5, 1 / 3, 1],
        ]
