import itertools
import random


import pandas as pd
from ahpy import Compare


class AHP:
    def __init__(self):
        pass

    def create_matriz_comparacao(self):
        # Definindo as matrizes de comparação de pares para cada critério
        pass


ahp = AHP()
ahp.create_matriz_decisao()

print("pera ae")

# @TODO -> Definir um limite de usuários para comparação
# Ao cadastrar o objetivo os usuários deverão escolher um tema "genérico" sobre o seu objetivo (Corrida, programação)
# Para comparação, buscar N usuários com objetivos cadastrados no msm tema

# ----------------------------------------------------------------------------------------------------------------------
# PASSO A PASSO
# 1 -> Definir os Critérios
# 2 -> Definir o peso dos Critérios

# ----------------------------------------------------------------------------------------------------------------------
# CRITÉRIOS
criterios = [
    "Nível de Esforço",
    "Período do Dia",
    "Faixa de Idade",
    "Nível de Experiência",
    "Avaliação de Usuários",
]

# "Nível de Esforço" -> 1, 2, 3, 4, 5 (1 - Baixo esforço, 5 - Alto esforço)
# "Período do Dia" -> Manhã, Tarde, Noite
# "Faixa de Idade" -> 1 (15-20), 2 (20-25), 3 (25-30), 4 (30-40), 5 (40-50)
# "Nível de Experiência" -> 1, 2, 3, 4, 5 (1 - Nenhuma experiência, 5 - Alta experiência)
# "Avaliação de Usuários" -> 1, 2, 3, 4, 5 (1 - Não gostou, 5 - Adorou)

# ----------------------------------------------------------------------------------------------------------------------


# 'Usuário 1' = {'Nível de Esforço': 4, 'Período do Dia': 'Manhã', 'Faixa de Idade': 2, 'Nível de Experiência': 4, 'Avaliação de Usuários': 5}
# 'Usuário 2' = {'Nível de Esforço': 3, 'Período do Dia': 'Manhã', 'Faixa de Idade': 4, 'Nível de Experiência': 3, 'Avaliação de Usuários': 2}
# 'Usuário 3' = {'Nível de Esforço': 4, 'Período do Dia': 'Tarde', 'Faixa de Idade': 3, 'Nível de Experiência': 4, 'Avaliação de Usuários': 2}
# 'Usuário 4' = {'Nível de Esforço': 3, 'Período do Dia': 'Manhã', 'Faixa de Idade': 1, 'Nível de Experiência': 4, 'Avaliação de Usuários': 5}
# 'Usuário 5' = {'Nível de Esforço': 2, 'Período do Dia': 'Tarde', 'Faixa de Idade': 2, 'Nível de Experiência': 1, 'Avaliação de Usuários': 4}
user_pairs = list(itertools.combinations(tuple(usuarios.keys()), 2))

usuarios = {
    "Usuário 1": {
        "Nível de Esforço": 4,
        "Período do Dia": "Manhã",
        "Faixa de Idade": 2,
        "Nível de Experiência": 4,
        "Avaliação de Usuários": 5,
    },
    "Usuário 2": {
        "Nível de Esforço": 3,
        "Período do Dia": "Manhã",
        "Faixa de Idade": 4,
        "Nível de Experiência": 3,
        "Avaliação de Usuários": 2,
    },
    "Usuário 3": {
        "Nível de Esforço": 4,
        "Período do Dia": "Tarde",
        "Faixa de Idade": 3,
        "Nível de Experiência": 4,
        "Avaliação de Usuários": 2,
    },
    "Usuário 4": {
        "Nível de Esforço": 3,
        "Período do Dia": "Manhã",
        "Faixa de Idade": 1,
        "Nível de Experiência": 4,
        "Avaliação de Usuários": 5,
    },
    "Usuário 5": {
        "Nível de Esforço": 2,
        "Período do Dia": "Tarde",
        "Faixa de Idade": 2,
        "Nível de Experiência": 1,
        "Avaliação de Usuários": 4,
    },
}

# Matriz de decisão para Nível de Esforço
nivel_esforco = pd.DataFrame(columns=usuarios.keys(), index=usuarios.keys())
for i in usuarios.keys():
    for j in usuarios.keys():
        nivel_esforco.loc[i, j] = (
            usuarios[i]["Nível de Esforço"] / usuarios[j]["Nível de Esforço"]
        )

# ----------------------------------------------------------------------------------------------------------------------
# Nível de Esforço
alternatives = [
    "Baixo esforço",
    "Moderado esforço",
    "Alto esforço",
    "Muito alto esforço",
    "Extremamente alto esforço",
]

nivel_de_esforco = {
    ("1 (Baixo esforço)", "1 (Baixo esforço)"): 1,
    ("1 (Baixo esforço)", "2 (Esforço um pouco maior)"): 3,
    ("1 (Baixo esforço)", "3 (Esforço moderado)"): 5,
    ("1 (Baixo esforço)", "4 (Esforço alto)"): 7,
    ("1 (Baixo esforço)", "5 (Muito alto esforço)"): 9,
    ("2 (Esforço um pouco maior)", "1 (Baixo esforço)"): 1 / 3,
    ("2 (Esforço um pouco maior)", "2 (Esforço um pouco maior)"): 1,
    ("2 (Esforço um pouco maior)", "3 (Esforço moderado)"): 1 / 3,
    ("2 (Esforço um pouco maior)", "4 (Esforço alto)"): 1 / 5,
    ("2 (Esforço um pouco maior)", "5 (Muito alto esforço)"): 1 / 7,
    ("3 (Esforço moderado)", "1 (Baixo esforço)"): 1 / 5,
    ("3 (Esforço moderado)", "2 (Esforço um pouco maior)"): 3,
    ("3 (Esforço moderado)", "3 (Esforço moderado)"): 1,
    ("3 (Esforço moderado)", "4 (Esforço alto)"): 1 / 3,
    ("3 (Esforço moderado)", "5 (Muito alto esforço)"): 1 / 5,
    ("4 (Esforço alto)", "1 (Baixo esforço)"): 1 / 7,
    ("4 (Esforço alto)", "2 (Esforço um pouco maior)"): 5,
    ("4 (Esforço alto)", "3 (Esforço moderado)"): 3,
    ("4 (Esforço alto)", "4 (Esforço alto)"): 1,
    ("4 (Esforço alto)", "5 (Muito alto esforço)"): 1 / 3,
    ("5 (Muito alto esforço)", "1 (Baixo esforço)"): 1 / 9,
    ("5 (Muito alto esforço)", "2 (Esforço um pouco maior)"): 7,
    ("5 (Muito alto esforço)", "3 (Esforço moderado)"): 5,
    ("5 (Muito alto esforço)", "4 (Esforço alto)"): 3,
    ("5 (Muito alto esforço)", "5 (Muito alto esforço)"): 1,
}

nivel_de_esforco_compare = Compare(
    alternatives, nivel_de_esforco, precision=3, random_index="saaty"
)

price_values = (
    9,
    9,
    1,
    1 / 2,
    5,
    1,
    1 / 9,
    1 / 9,
    1 / 7,
    1 / 9,
    1 / 9,
    1 / 7,
    1 / 2,
    5,
    6,
)
price_comparisons = dict(zip(user_pairs, price_values))
print(price_comparisons)

# ----------------------------------------------------------------------------------------------------------------------
# "Período do Dia" -> Manhã, Tarde, Noite

alternatives_periodo_dia = ["Manhã", "Tarde", "Noite"]

periodo_dia = {
    ("Manhã", "Manhã"): 1,
    ("Manhã", "Tarde"): 3,
    ("Manhã", "Noite"): 4,
    ("Tarde", "Manhã"): 1 / 3,
    ("Tarde", "Tarde"): 1,
    ("Tarde", "Noite"): 2,
    ("Noite", "Manhã"): 1 / 4,
    ("Noite", "Tarde"): 1 / 2,
    ("Noite", "Noite"): 1,
}

periodo_dia_compare = Compare(
    alternatives_periodo_dia, periodo_dia, precision=3, random_index="saaty"
)

print("pera ae")
