from dataclasses import dataclass
from enum import Enum
import random
from app.models.criterios import Criterios


@dataclass
class UserModel:
    nivel_esforco: int
    periodo_dia: int
    faixa_idade: int
    nivel_experiencia: int
    avaliacao_usuarios: int

    def __dict__(self):
        return {
            Criterios.esforco.value: self.nivel_esforco,
            Criterios.periodo.value: self.periodo_dia,
            Criterios.faixa_idade.value: self.faixa_idade,
            Criterios.experiencia.value: self.nivel_experiencia,
            Criterios.avaliacao.value: self.avaliacao_usuarios,
        }


def generate_users(total_usuarios: int):
    """Geração de usuários para testes

    Args:
        total_usuarios ():

    Returns:

    """

    usuarios = {}

    for i in range(total_usuarios):
        level_of_effort = random.randint(1, 5)
        time_of_day = random.choice([1, 2, 3])
        age_range = random.choice([1, 2, 3, 4, 5])
        experience_level = random.randint(1, 5)
        user_rating = random.randint(1, 5)

        usuarios[f"Usuário {i + 1}"] = {
            Criterios.esforco.value: level_of_effort,
            Criterios.periodo.value: time_of_day,
            Criterios.faixa_idade.value: age_range,
            Criterios.experiencia.value: experience_level,
            Criterios.avaliacao.value: user_rating,
        }
    return usuarios
