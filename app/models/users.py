from app.connections.arangodb import ArangoDB
from dataclasses import dataclass, asdict


@dataclass
class User:
    email: str
    username: str
    password: str

    key: str = None


class UsersModel(ArangoDB):
    def __init__(self):
        collection = "Users"
        super().__init__(collection=collection)

    def get_user(self, user_key: str):
        user = self.collection[user_key]
        user = User(
            email=user.email,
            username=user.username,
            password=user.password,
            key=user._key,
        )
        return asdict(user)

    def get_users(self):
        users = []
        for user in self.collection.fetchAll():
            users.append(
                asdict(
                    User(
                        key=user._key,
                        email=user.email,
                        username=user.username,
                        password=user.password,
                    )
                )
            )
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
