from ahpy import Compare
import numpy as np


class AHP:
    def __init__(self):
        pass

    def build_matriz(self, user_criterios: dict, user_criterios_recomendacao: list):
        user_criterios_matriz = self.convert_criterios_saaty(
            criterios_user=user_criterios
        )

        for user_recomendacao in user_criterios_recomendacao:
            user_recomendacao_criterios_matriz = self.convert_criterios_saaty(
                criterios_user=user_recomendacao.get("criterios")
            )
            user_recomendacao.update(user_recomendacao_criterios_matriz)

        peso_user, soma_peso_user = self.calculate_peso(
            matriz=user_criterios_matriz.get("matriz"),
            soma_total=user_criterios_matriz.get("soma_por_criterio"),
        )

        for user in user_criterios_recomendacao:
            soma_por_criterio = user['soma_por_criterio']
            user['soma_ponderada'] = sum([peso * valor for peso, valor in zip(soma_peso_user, soma_por_criterio)])

        # Exibir os resultados
        # print("-----------------")
        # for user in user_criterios_recomendacao:
        #     print(f"Usuário: {user['username']}")
        #     print("Soma Ponderada:")
        #     print(user['soma_ponderada'])
        #     print()

        return [{"user_id": user.get("user_id"), "username": user.get("username"), "resultado": round(user.get("soma_ponderada"), 2)} for user in user_criterios_recomendacao]

    def calculate_peso(self, matriz, soma_total):
        matrix = np.array(matriz)
        soma_total = np.array(soma_total)

        pesos = np.zeros_like(matrix, dtype=float)
        soma_linha = np.zeros(matrix.shape[0])

        for i in range(matrix.shape[0]):
            pesos[i] = matrix[i] / soma_total

        for i, peso in enumerate(pesos):
            soma_linha[i] = sum(peso)

        # Calcular os pesos para cada registro
        return list(pesos), list(soma_linha)

    def convert_criterios_saaty(self, criterios_user):
        importancias = {
            "Importância igual": 1,
            "Importância moderada": 3,
            "Importância forte": 5,
            "Importância muito forte": 7,
            "Importância extrema": 9,
        }

        # Criar uma lista com todas as chaves únicas presentes no dicionário
        keys = list(criterios_user.keys())

        # Criar uma matriz preenchida com valores zero
        matriz = [[1] * (len(keys)) for _ in range(len(keys))]

        for i, criterioI in enumerate(criterios_user):
            for j, criterioJ in enumerate(criterios_user):
                if i != j:
                    criterios_keys = [
                        criterios.get("criterio")
                        for criterios in criterios_user[criterioI]
                    ]
                    criterios_values = [
                        criterios for criterios in criterios_user[criterioI]
                    ]
                    if criterioI in criterios_user and criterioJ in criterios_keys:
                        value = criterios_values[criterios_keys.index(criterioJ)][
                            "value"
                        ]
                        importancia = importancias[value]
                        matriz[j][i] = importancia
                        matriz[i][j] = 1 / importancia

        # print("\t".join(criterios_user))
        # for row in matriz:
        #     print("\t".join([str(value) for value in row]))

        return {
            "criterios": criterios_user.keys(),
            "soma_por_criterio": list(np.sum(matriz, axis=0)),
            "matriz": matriz,
        }


if __name__ == "__main__":
    AHP().build_matriz(
        user_criterios={
            "Esforço": [
                {"criterio": "Período", "value": "Importância moderada"},
                {"criterio": "Tempo Conclusão", "value": "Importância forte"},
                {"criterio": "Experiência", "value": "Importância extrema"},
                {"criterio": "Avaliação de Usuários", "value": "Importância igual"},
            ],
            "Período": [
                {"criterio": "Tempo Conclusão", "value": "Importância muito forte"},
                {"criterio": "Experiência", "value": "Importância extrema"},
                {"criterio": "Avaliação de Usuários", "value": "Importância forte"},
            ],
            "Tempo Conclusão": [
                {"criterio": "Experiência", "value": "Importância extrema"},
                {"criterio": "Avaliação de Usuários", "value": "Importância forte"},
            ],
            "Experiência": [
                {"criterio": "Avaliação de Usuários", "value": "Importância igual"}
            ],
            "Avaliação de Usuários": [],
        },
        user_criterios_recomendacao=[
            {
                "user_id": "Users/689653",
                "username": "Guilherme",
                "criterios": {
                    "Esforço": [
                        {"criterio": "Período", "value": "Importância extrema"},
                        {
                            "criterio": "Tempo Conclusão",
                            "value": "Importância moderada",
                        },
                        {"criterio": "Experiência", "value": "Importância extrema"},
                    ],
                    "Período": [
                        {"criterio": "Tempo Conclusão", "value": "Importância forte"},
                        {"criterio": "Experiência", "value": "Importância extrema"},
                    ],
                    "Tempo Conclusão": [
                        {"criterio": "Experiência", "value": "Importância forte"}
                    ],
                    "Experiência": [],
                },
            },
            {
                "user_id": "Users/689687",
                "username": "Julia",
                "criterios": {
                    "Esforço": [
                        {"criterio": "Período", "value": "Importância forte"},
                        {"criterio": "Experiência", "value": "Importância muito forte"},
                        {
                            "criterio": "Avaliação de Usuários",
                            "value": "Importância igual",
                        },
                    ],
                    "Período": [
                        {"criterio": "Experiência", "value": "Importância muito forte"},
                        {
                            "criterio": "Avaliação de Usuários",
                            "value": "Importância extrema",
                        },
                    ],
                    "Experiência": [
                        {
                            "criterio": "Avaliação de Usuários",
                            "value": "Importância muito forte",
                        }
                    ],
                    "Avaliação de Usuários": [],
                },
            },
        ],
    )
