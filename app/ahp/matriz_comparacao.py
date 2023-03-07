import numpy as np
from typing import Dict, List, Tuple
from app.models.users_model import generate_users
from app.models.criterios import Criterios


class MatrizComparacao:
    def __init__(self):
        self.criterios = Criterios.names()
        self.users = generate_users(total_usuarios=2)

        # @TODO -> Verificar necessidade de criação da escala saaty para N usuários
        self.saaty_scale = [
            [1, 3, 5, 7, 9],
            [1 / 3, 1, 3, 5, 7],
            [1 / 5, 1 / 3, 1, 3, 5],
            [1 / 7, 1 / 5, 1 / 3, 1, 3],
            [1 / 9, 1 / 7, 1 / 5, 1 / 3, 1],
        ]

    # Função para criar matriz de comparação entre dois usuários para cada critério
    def create_comparison_matrix(
        self,
        user1: Dict,
        user2: Dict,
        criteria: List[str],
        saaty_scale: List[List[int]],
    ):
        comparison_matrix = {}
        for criterion in criteria:
            values = [user1[criterion], user2[criterion]]
            matrix = []
            for i in range(2):
                row = []
                for j in range(2):
                    if i == j:
                        row.append(1)
                    else:
                        row.append(saaty_scale[values[j] - 1][values[i] - 1])
                matrix.append(row)
            comparison_matrix[criterion] = matrix
        return comparison_matrix

    def run(self):
        # Criar matriz de comparação entre os dois usuários para cada critério
        comparison_matrices = {}
        for user1, user2 in [
            (self.users["Usuário 1"], self.users["Usuário 2"]),
            (self.users["Usuário 2"], self.users["Usuário 1"]),
        ]:
            comparison_matrix = self.create_comparison_matrix(
                user1, user2, self.criterios, self.saaty_scale
            )
            comparison_matrices[f"{user1} vs {user2}"] = comparison_matrix

        # Imprimir as matrizes de comparação
        for key, matrix in comparison_matrices.items():
            print(key)
            for criterion, values in matrix.items():
                print(criterion)
                for row in values:
                    print(row)
                print("")

    def create_matriz_decisao(self):
        # Definindo as matrizes de comparação de pares para cada critério
        esforco = np.array(
            [
                [1, 3, 5, 7, 9],
                [1 / 3, 1, 3, 5, 7],
                [1 / 5, 1 / 3, 1, 3, 5],
                [1 / 7, 1 / 5, 1 / 3, 1, 3],
                [1 / 9, 1 / 7, 1 / 5, 1 / 3, 1],
            ]
        )

        periodo = np.array([[1, 3, 5], [1 / 3, 1, 3], [1 / 5, 1 / 3, 1]])

        idade = np.array(
            [
                [1, 3, 5, 7, 9],
                [1 / 3, 1, 3, 5, 7],
                [1 / 5, 1 / 3, 1, 3, 5],
                [1 / 7, 1 / 5, 1 / 3, 1, 3],
                [1 / 9, 1 / 7, 1 / 5, 1 / 3, 1],
            ]
        )

        experiencia = np.array(
            [
                [1, 3, 5, 7, 9],
                [1 / 3, 1, 3, 5, 7],
                [1 / 5, 1 / 3, 1, 3, 5],
                [1 / 7, 1 / 5, 1 / 3, 1, 3],
                [1 / 9, 1 / 7, 1 / 5, 1 / 3, 1],
            ]
        )

        avaliacao = np.array(
            [
                [1, 3, 5, 7, 9],
                [1 / 3, 1, 3, 5, 7],
                [1 / 5, 1 / 3, 1, 3, 5],
                [1 / 7, 1 / 5, 1 / 3, 1, 3],
                [1 / 9, 1 / 7, 1 / 5, 1 / 3, 1],
            ]
        )

        # Calculando os vetores de prioridades relativas para cada matriz
        esforco_prio_rel = np.sum(esforco, axis=1) / np.size(esforco, 0)
        periodo_prio_rel = np.sum(periodo, axis=1) / np.size(periodo, 0)
        idade_prio_rel = np.sum(idade, axis=1) / np.size(idade, 0)
        experiencia_prio_rel = np.sum(experiencia, axis=1) / np.size(experiencia, 0)
        avaliacao_prio_rel = np.sum(avaliacao, axis=1) / np.size(avaliacao, 0)

        # Imprimindo os vetores de prioridades relativas
        print(
            "Vetor de prioridades relativas para o critério de Nível de Esforço:",
            esforco_prio_rel,
        )
        print(
            "Vetor de prioridades relativas para o critério de Período do Dia: ",
            periodo_prio_rel,
        )
        print(
            "Vetor de prioridades relativas para o critério de Idade: ", idade_prio_rel
        )
        print(
            "Vetor de prioridades relativas para o critério de Experiência: ",
            experiencia_prio_rel,
        )
        print(
            "Vetor de prioridades relativas para o critério de Avaliação Usuários: ",
            avaliacao_prio_rel,
        )


if __name__ == "__main__":
    MatrizComparacao().run()
