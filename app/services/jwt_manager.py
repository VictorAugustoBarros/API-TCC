import jwt
from datetime import datetime, timedelta

class JwtManager:
    def __init__(self):
        self.secret_key = "vamosverseissofunciona"

    def create_token(self, payload: dict):
        payload.update({"exp": datetime.utcnow() + timedelta(hours=1)})
        return jwt.encode(payload, self.secret_key, algorithm='HS256')

    def verify_token(self, token: str):
        try:
            return jwt.decode(token, self.secret_key, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            pass
        except jwt.InvalidTokenError:
            pass

        return None


