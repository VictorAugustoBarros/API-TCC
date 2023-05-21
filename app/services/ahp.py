class Ahp:
    def __init__(self):
        pass


# from enum import Enum
#
# class Criterios(Enum):
#     """
#     "Nível de Esforço" -> 1, 2, 3, 4, 5 (1 - Baixo esforço, 5 - Alto esforço)
#     "Período do Dia" -> 1 (Manhã), 2 (Tarde), 3 (Noite)
#     "Faixa de Idade" -> 1 (15-20), 2 (20-25), 3 (25-30), 4 (30-40), 5 (40-50)
#     "Nível de Experiência" -> 1, 2, 3, 4, 5 (1 - Nenhuma experiência, 5 - Alta experiência)
#     "Avaliação de Usuários" -> 1, 2, 3, 4, 5 (1 - Não gostou, 5 - Adorou)
#     """
#
#     esforco = "Nível de Esforço"
#     periodo = "Período do Dia"
#     faixa_idade = "Faixa de Idade"
#     experiencia = "Nível de Experiência"
#     avaliacao = "Avaliação de Usuários"
#
#     @staticmethod
#     def names():
#         return [criterio.value for criterio in Criterios]
#
#     @staticmethod
#     def saaty():
#         return [
#             [1, 3, 5, 7, 9],
#             [1 / 3, 1, 3, 5, 7],
#             [1 / 5, 1 / 3, 1, 3, 5],
#             [1 / 7, 1 / 5, 1 / 3, 1, 3],
#             [1 / 9, 1 / 7, 1 / 5, 1 / 3, 1],
#         ]

# teste = {
#     "Nível Esforço": [{"criterio": "Período do Dia", "value": 7}],
#     "Período do Dia": [{"criterio": "Nível Esforço", "value": 5}],
# }
#
# teste2 = {
#     "Nível Esforço": [
#         {"criterio": "Período do Dia", "value": 7},
#         {"criterio": "Tempo Conclusão", "value": 2},
#         {"criterio": "Nível Experiência", "value": 5},
#         {"criterio": "Avaliação de Usuários", "value": 2},
#     ],
#     "Período do Dia": [
#         {"criterio": "Nível Esforço", "value": 2},
#         {"criterio": "Tempo Conclusão", "value": 2},
#         {"criterio": "Nível Experiência", "value": 2},
#         {"criterio": "Avaliação de Usuários", "value": 2},
#     ],
#     "Tempo Conclusão": [
#         {"criterio": "Nível Esforço", "value": 2},
#         {"criterio": "Período do Dia", "value": 5},
#         {"criterio": "Nível Experiência", "value": 2},
#         {"criterio": "Avaliação de Usuários", "value": 2},
#     ],
#     "Nível Experiência": [
#         {"criterio": "Nível Esforço", "value": 2},
#         {"criterio": "Período do Dia", "value": 5},
#         {"criterio": "Tempo Conclusão", "value": 3},
#         {"criterio": "Avaliação de Usuários", "value": 5},
#     ],
#     "Avaliação de Usuários": [
#         {"criterio": "Nível Esforço", "value": 2},
#         {"criterio": "Período do Dia", "value": 5},
#         {"criterio": "Tempo Conclusão", "value": 2},
#         {"criterio": "Nível Experiência", "value": 2},
#     ],
# }
