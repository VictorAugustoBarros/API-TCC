from pydantic import BaseModel
from app.connections.arangodb import ArangoDB


class LoginUser(BaseModel):
    email: str
    password: str


class User(BaseModel):
    name: str
    email: str
    password: str
    username: str
    followers: int = 0
    following: int = 0
    _key: str = None


class UsersModel(ArangoDB):
    def __init__(self):
        super().__init__(collection="Users")

    def insert_user(self, user: User):
        return self.insert(**user.__dict__)

    def find_user_by_name(self, username: str):
        return self.find(data={"name": username})

    def find_user_by_email(self, email: str):
        return self.find(data={"email": email})

    def find_user_by_username(self, username: str):
        return self.find(data={"username": username})

    def find_user_by_id(self, user_id: str):
        user = self.find(data={"_id": user_id})
        if user:
            return user[0]
        return user

    def update_user(self, key: str, user: dict):
        self.update(key=key, data=user.__dict__)

    def delete_user(self, key: str):
        self.delete(key=key)

    def find_user_login(self, login_user: LoginUser):
        user = self.find(data={"email": login_user.email, "password": login_user.password})
        if user:
            return user[0]
        return user

