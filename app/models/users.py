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

    def get_all_users(self):
        return self.fetch_all()

    def get_user_by_key(self, key):
        return self.fetch_one(key=key)

    def get_user_by_document(self, document: dict):
        rows = self.fetch_one_document(document=document)
        for row in rows:
            return row

    def insert_user(self, email: str, username: str, password: str):
        self.insert_document(
            document={
                "email": email,
                "username": username,
                "password": password,
            }
        )

    def update_user(self, key: str, user: dict):
        self.update_document(document_key=key, new_data=user)

    def delete_user(self, key: str):
        self.delete_document(document_key=key)

    def validate_login(self, user: dict) -> dict:
        result = self.fetch_one_document(document=user)
        print(result)
