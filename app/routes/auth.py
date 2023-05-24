from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.services.jwt_manager import JwtManager
from app.utils.errors import APIErrors
from app.validatores.token_validator import token_validation

routes_auth = APIRouter()

from app.services.login import Login


@routes_auth.post("/api/auth/login")
async def auth_user(request: Request):
    request_body = await request.json()
    if not (email := request_body.get("email")):
        return JSONResponse(
            status_code=200, content={"error": APIErrors.EMAIL_NOT_FOUND.value}
        )

    if not (password := request_body.get("password")):
        return JSONResponse(
            status_code=200, content={"error": APIErrors.PASSWORD_NOT_FOUND.value}
        )

    login = Login()
    login_user = login.login_user(email=email, password=password)
    if not login_user.get("success"):
        return JSONResponse(status_code=200, content=login_user)

    return JSONResponse(status_code=200, content=login_user)


@routes_auth.get("/api/auth/verify")
@token_validation
async def check_token(request: Request):
    return JSONResponse(status_code=200, content={"success": True})
