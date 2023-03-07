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

users_esforco = {
    ("User1", "User1"): 1,
    ("User1", "User2"): 9,
    ("User1", "User3"): 1,
    ("User2", "User1"): 1 / 9,
    ("User2", "User2"): 1,
    ("User2", "User3"): 1 / 9,
    ("User3", "User1"): 1,
    ("User3", "User2"): 9,
    ("User3", "User3"): 1,
}
esforco = ahpy.Compare(
    "Esforco", users_esforco, random_index="saaty"
)

users_periodo = {
    ("User1", "User1"): 1,
    ("User1", "User2"): 1,
    ("User1", "User3"): 3,
    ("User2", "User1"): 1,
    ("User2", "User2"): 1,
    ("User2", "User3"): 3,
    ("User3", "User1"): 1 / 3,
    ("User3", "User2"): 1 / 3,
    ("User3", "User3"): 1,
}
periodo = ahpy.Compare(
    "Periodo", users_periodo, random_index="saaty"
)

users_idade = {
    ("User1", "User1"): 1,
    ("User1", "User2"): 1 / 5,
    ("User1", "User3"): 1 / 3,
    ("User2", "User1"): 5,
    ("User2", "User2"): 1,
    ("User2", "User3"): 3,
    ("User3", "User1"): 3,
    ("User3", "User2"): 1 / 3,
    ("User3", "User3"): 1,
}
idade = ahpy.Compare(
    "Idade", users_idade, random_index="saaty"
)

users_experiencia = {
    ("User1", "User1"): 1,
    ("User1", "User2"): 3,
    ("User1", "User3"): 3,
    ("User2", "User1"): 1 / 3,
    ("User2", "User2"): 1,
    ("User2", "User3"): 1,
    ("User3", "User1"): 1 / 3,
    ("User3", "User2"): 1,
    ("User3", "User3"): 1,
}
experiencia = ahpy.Compare(
    "Experiencia", users_experiencia, random_index="saaty"
)

users_avaliacao = {
    ("User1", "User1"): 1,
    ("User1", "User2"): 1 / 5,
    ("User1", "User3"): 1 / 9,
    ("User2", "User1"): 5,
    ("User2", "User2"): 1,
    ("User2", "User3"): 1 / 3,
    ("User3", "User1"): 9,
    ("User3", "User2"): 3,
    ("User3", "User3"): 1,
}
avaliacao = ahpy.Compare(
    "Avaliacao", users_avaliacao, random_index="saaty"
)

criterias = {
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
criteria = ahpy.Compare(
    "Criteria", criterias, random_index="saaty"
)

criteria.add_children([esforco, periodo, idade, experiencia, avaliacao])

report = criteria.report(show=True)

print("-------------------------------------------------------------------")
print(criteria.target_weights)

maior_valor = max(criteria.target_weights.values())
for chave, valor in criteria.target_weights.items():
    if valor == maior_valor:
        print({
            "message": "Usuário a recomendar",
            "usuario": chave,
            "valor": valor
        })
