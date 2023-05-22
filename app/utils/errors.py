from enum import Enum


class APIErrors(Enum):
    EMAIL_NOT_FOUND = "Email não informado!"
    PASSWORD_NOT_FOUND = "Password não informado!"
    USER_ID_NOT_FOUND = "UserId não informado!"
