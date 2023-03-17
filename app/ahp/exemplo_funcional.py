import ahpy

user1 = {
    "Nivel de Esforco": 5,
    "Periodo do Dia": 1,
    "Faixa de Idade": 1,
    "Nivel de Experiencia": 2,
    "Avaliacao de Usuários": 1,
}

user2 = {
    "Nivel de Esforco": 1,
    "Periodo do Dia": 1,
    "Faixa de Idade": 3,
    "Nivel de Experiencia": 1,
    "Avaliacao de Usuários": 3,
}

user3 = {
    "Nivel de Esforco": 5,
    "Periodo do Dia": 2,
    "Faixa de Idade": 2,
    "Nivel de Experiencia": 1,
    "Avaliacao de Usuários": 5,
}

user_1_criterias = {
    ("Esforco", "Esforco"): 1,
    ("Esforco", "Periodo"): 7,
    ("Esforco", "Idade"): 5,
    ("Esforco", "Experiencia"): 1,
    ("Esforco", "Avaliacao"): 3,
    ("Periodo", "Esforco"): 1 / 7,
    ("Periodo", "Periodo"): 1,
    ("Periodo", "Idade"): 3,
    ("Periodo", "Experiencia"): 1 / 5,
    ("Periodo", "Avaliacao"): 1 / 3,
    ("Idade", "Esforco"): 1 / 5,
    ("Idade", "Periodo"): 1 / 3,
    ("Idade", "Idade"): 1,
    ("Idade", "Experiencia"): 1 / 7,
    ("Idade", "Avaliacao"): 1 / 5,
    ("Experiencia", "Esforco"): 1 / 3,
    ("Experiencia", "Periodo"): 5,
    ("Experiencia", "Idade"): 7,
    ("Experiencia", "Experiencia"): 1,
    ("Experiencia", "Avaliacao"): 3,
    ("Avaliacao", "Esforco"): 1,
    ("Avaliacao", "Periodo"): 3,
    ("Avaliacao", "Idade"): 5,
    ("Avaliacao", "Experiencia"): 1 / 3,
    ("Avaliacao", "Avaliacao"): 1,
}
criteria1 = ahpy.Compare("User1", user_1_criterias, random_index="saaty")

user_2_criterias = {
    ("Esforco", "Esforco"): 1,
    ("Esforco", "Periodo"): 7,
    ("Esforco", "Idade"): 3,
    ("Esforco", "Experiencia"): 1,
    ("Esforco", "Avaliacao"): 3,
    ("Periodo", "Esforco"): 1 / 7,
    ("Periodo", "Periodo"): 1,
    ("Periodo", "Idade"): 3,
    ("Periodo", "Experiencia"): 1 / 5,
    ("Periodo", "Avaliacao"): 1 / 3,
    ("Idade", "Esforco"): 1 / 7,
    ("Idade", "Periodo"): 1 / 3,
    ("Idade", "Idade"): 1,
    ("Idade", "Experiencia"): 1 / 7,
    ("Idade", "Avaliacao"): 1 / 5,
    ("Experiencia", "Esforco"): 1 / 3,
    ("Experiencia", "Periodo"): 5,
    ("Experiencia", "Idade"): 5,
    ("Experiencia", "Experiencia"): 1,
    ("Experiencia", "Avaliacao"): 3,
    ("Avaliacao", "Esforco"): 1,
    ("Avaliacao", "Periodo"): 1,
    ("Avaliacao", "Idade"): 1,
    ("Avaliacao", "Experiencia"): 1 / 3,
    ("Avaliacao", "Avaliacao"): 1,
}
criteria2 = ahpy.Compare("User2", user_2_criterias, random_index="saaty")

user_3_criterias = {
    ("Esforco", "Esforco"): 1,
    ("Esforco", "Periodo"): 7,
    ("Esforco", "Idade"): 5,
    ("Esforco", "Experiencia"): 1,
    ("Esforco", "Avaliacao"): 3,
    ("Periodo", "Esforco"): 1 / 7,
    ("Periodo", "Periodo"): 1,
    ("Periodo", "Idade"): 3,
    ("Periodo", "Experiencia"): 1 / 5,
    ("Periodo", "Avaliacao"): 1 / 3,
    ("Idade", "Esforco"): 1 / 5,
    ("Idade", "Periodo"): 1 / 3,
    ("Idade", "Idade"): 1,
    ("Idade", "Experiencia"): 1 / 7,
    ("Idade", "Avaliacao"): 1 / 5,
    ("Experiencia", "Esforco"): 1 / 3,
    ("Experiencia", "Periodo"): 5,
    ("Experiencia", "Idade"): 3,
    ("Experiencia", "Experiencia"): 1,
    ("Experiencia", "Avaliacao"): 3,
    ("Avaliacao", "Esforco"): 1,
    ("Avaliacao", "Periodo"): 3,
    ("Avaliacao", "Idade"): 5,
    ("Avaliacao", "Experiencia"): 1 / 3,
    ("Avaliacao", "Avaliacao"): 1,
}
criteria3 = ahpy.Compare("User3", user_3_criterias, random_index="saaty")

print("-------------------------------------------------------------------")
print(criteria1.target_weights)
print(criteria2.target_weights)
print(criteria3.target_weights)

users = [
    {
        "user": "user1",
        "weights": sum([criteria for criteria in criteria1.target_weights.values()]),
        "consistency": criteria1.consistency_ratio,
    },
    {
        "user": "user2",
        "weights": sum([criteria for criteria in criteria2.target_weights.values()]),
        "consistency": criteria2.consistency_ratio,
    },
    {
        "user": "user3",
        "weights": sum([criteria for criteria in criteria3.target_weights.values()]),
        "consistency": criteria3.consistency_ratio,
    },
]

maior_valor = max([user.get("weights") for user in users])
for user in users:
    if user.get("weights") == maior_valor:
        print(user)
