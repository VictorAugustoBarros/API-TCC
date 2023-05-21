from datetime import datetime, timedelta

from app.models.objetivos import ObjetivosModel, Objetivo
from app.models.users import UsersModel, User


class CreateTests:

    def create_user(self):
        users_model = UsersModel()
        user = User(
            name="UserTest",
            email="teste@teste.com",
            password="teste123",
            username="teste",
            followers=10,
            following=50,
        )
        return users_model.create_user(user=user)

    def delete_user(self, user_key: str):
        users_model = UsersModel()
        users_model.delete_by_key(key=user_key)

    def create_objetivo(self):
        objetivos_model = ObjetivosModel()
        objetivo = Objetivo(
            titulo="Objetivo_Test",
            categoria="Gatos",
            descricao="gato de teste",
            imagem="https://i0.statig.com.br/bancodeimagens/2n/y9/zl/2ny9zlk3myviabfr6wd6k8ccz.jpg",
            data_fim=datetime.strftime(datetime.now() + timedelta(days=1), "%m/%d/%Y %H:%M:%S"),
        )
        return objetivos_model.insert_objetivo(objetivo=objetivo)

    def delete_objetivo(self, objetivo_key: str):
        objetivos_model = ObjetivosModel()
        objetivos_model.delete_objetivo(objetivo_key=objetivo_key)
