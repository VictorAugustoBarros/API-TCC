from app.models.users import UsersModel
from services.jwt_manager import JwtManager


class Login:
    def __init__(self):
        self.users_model = UsersModel()
        self.jwt_manager = JwtManager()

    def login_user(self, email: str, password: str):
        user = self.users_model.find_user_login(email=email, password=password)
        if not user:
            return {"success": False, "error": "Usuário não encontrado!"}

        token = self.jwt_manager.create_token(
            payload={
                "id": user.get("_id"),
                "key": user.get("_key"),
                "email": user.get("email"),
                "password": user.get("password"),
            }
        )

        return {"success": True, "token": token}
