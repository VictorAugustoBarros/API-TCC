from pydantic import BaseModel
from app.connections.arangodb import ArangoDB


class UserLogin(BaseModel):
    email: str
    password: str


class User(BaseModel):
    email: str
    password: str
    username: str


class UsersModel(ArangoDB):
    def __init__(self):
        collection = "Users"
        super().__init__(collection=collection)

    def validate_user(self, email: str, password: str) -> dict:
        for user in self.collection.fetchAll():
            if user.email == email and user.password == password:
                return {"key": user._key, "username": user.username, "email": user.email, "login": True}

        return {
            "login": False
        }

    def get_user(self, user_key: str):
        user = self.collection[user_key]
        if user:
            return {"email": user.email, "username": user.username, "key": user._key}

        return {}

    def get_users(self):
        users = []
        for user in self.collection.fetchAll():
            users.append({"key": user._key, "username": user.username, "email": user.email, "password": user.password})

        return users

    def insert_user(self, email: str, username: str, password: str):
        user = self.collection.createDocument()
        user["email"] = email
        user["username"] = username
        user["password"] = password
        user.save()

    def update_user(self, user_key: str, email: str, username: str, password: str):
        user = self.collection[user_key]
        user["email"] = email
        user["username"] = username
        user["password"] = password
        user.save()

    def delete_user(self, user_key: str):
        user = self.collection[user_key]
        user.delete()
