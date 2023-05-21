from app.models.users import UsersModel, User

user = UsersModel().create_user(user=User(
    name="Victor Augusto",
    email="victor.augustobarros@gmail.com",
    password="victor123",
    username="_vic_augusto"
))

print(user.__dict__)
