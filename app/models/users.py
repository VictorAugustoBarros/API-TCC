from dataclasses import dataclass
from app.connections.arangodb import ArangoDB


@dataclass
class User:
    name: str
    email: str
    password: str
    username: str
    followers: int = 0
    following: int = 0
    user_icon: str = (
        "https://cdn.icon-icons.com/icons2/2468/PNG/512/user_icon_149329.png"
    )
    user_banner: str = "https://br.virbac.com/files/live/sites/virbac-br/files/predefined-files/banners/Cats/Banner_Gato.jpg"


class UsersModel(ArangoDB):
    def __init__(self):
        super().__init__(collection="Users")

    def create_user(self, user: User):
        return self.insert(**user.__dict__)

    def find_user_email(self, email: str):
        return self.find(data={"email": email})

    def find_all_usernames(self):
        users = self.find_all()
        return [user.get("username") for user in users]

    def find_user_username(self, username: str):
        user = self.find(data={"username": username})
        if user:
            return user[0]
        return user

    def find_user_by_key(self, user_key: str):
        user = self.find(data={"_key": user_key})
        if user:
            return user[0]
        return user

    def update_user(self, key: str, user: dict):
        self.update(key=key, data=user)

    def delete_user(self, key: str):
        self.delete_by_key(key=key)

    def find_user_login(self, email: str, password: str):
        user = self.find(data={"email": email, "password": password})
        if user:
            return user[0]
        return user
