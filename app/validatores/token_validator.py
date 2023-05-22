from functools import wraps
from fastapi import Request
from fastapi.responses import JSONResponse
from app.services.jwt_manager import JwtManager


def token_validation(func):
    @wraps(func)
    async def decorated_func(*args, **kwargs):
        token = kwargs.get("request").headers.get("Authorization")
        if token is None:
            return JSONResponse(
                status_code=200,
                content={"success": False, "error": "Token não informado!"},
            )

        jwt_manager = JwtManager()
        token_data = jwt_manager.verify_token(token=token)
        kwargs["request"].state.token = token_data

        return await func(*args, **kwargs)

    return decorated_func
