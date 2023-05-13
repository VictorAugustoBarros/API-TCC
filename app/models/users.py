from pydantic import BaseModel
from app.connections.arangodb import ArangoDB


class User(BaseModel):
    name: str
    email: str
    password: str
    username: str
    _key: str = None


class UsersModel(ArangoDB):
    def __init__(self):
        super().__init__(collection="Users")

    def insert_user(self, user: User):
        self.insert(**user.__dict__)

    def find_user_by_name(self, username: str):
        return self.find(data={"name": username})

    def find_user_by_email(self, email: str):
        return self.find(data={"email": email})

    def find_user_by_username(self, username: str):
        return self.find(data={"username": username})

    def find_user_by_key(self, key: str):
        return self.find(data={"_key": key})

    def update_user(self, key: str, user: dict):
        self.update(key=key, data=user.__dict__)

    def delete_user(self, key: str):
        self.delete(key=key)

    def find_user_login(self, user: User):
        return self.find(data={"email": user.email, "password": user.password})
