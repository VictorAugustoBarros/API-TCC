from app.models.users import UsersModel, User
from services.jwt_manager import JwtManager
from dataclasses import dataclass


class Register:
    def __init__(self):
        self.users_model = UsersModel()
        self.jwt_manager = JwtManager()

    def register_user(self, user: User):
        email = self.users_model.find_user_email(email=user.email)
        if email:
            return {"success": False, "error": "Email já existe!"}

        username = self.users_model.find_user_username(username=user.username)
        if username:
            return {"success": False, "error": "Username já existe!"}

        user = self.users_model.create_user(user=user)
        return {
            "success": True,
            "user": {
                "key": user.key,
            },
        }
