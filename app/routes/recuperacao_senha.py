from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.recuperacao_senha import RecuperacaoSenhaModel, RecuperacaoSenha
from app.models.users import UsersModel
import secrets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

recuperacao_senha_route = APIRouter()


@recuperacao_senha_route.post("/api/recuperacao/enviar")
async def enviar_email(request: Request):
    body = await request.json()
    email = body.get("email")

    # Configurações do servidor SMTP
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'interlinker.social@gmail.com'
    smtp_password = 'oszteyiztrxomonm'

    # Configurações do email
    from_address = 'interlinker.social@gmail.com'
    to_address = email
    subject = 'Interlinker - Recuperação Senha'

    random_hash = secrets.token_hex(16)

    message = f'''
        <html>
          <body>
            <h3>Código de recuperação de senha</h3>
            <h2>{random_hash}</h2>
          </body>
        </html>
        '''

    # Criação do objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Adiciona o conteúdo do email como uma parte de texto
    html_part = MIMEText(message, 'html')
    msg.attach(html_part)

    # Conexão com o servidor SMTP
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Envio do email
    server.send_message(msg)
    server.quit()

    recuperacao_model_senha = RecuperacaoSenhaModel()
    recuperacao_model_senha.insert_recuperacao_senha(
        recuperacao_senha=RecuperacaoSenha(email=email, hash=random_hash)
    )

    return JSONResponse(status_code=200, content={"success": True})


@recuperacao_senha_route.post("/api/recuperacao/validar")
async def validar_hash(request: Request):
    body = await request.json()
    email = body.get("email")
    hash = body.get("hash")

    recuperacao_model_senha = RecuperacaoSenhaModel()
    result = recuperacao_model_senha.find_recuperacao_senha(email=email, hash=hash)
    if result:
        recuperacao_model_senha.delete_recuperacao_senha(key=result.get("_key"))
        return JSONResponse(status_code=200, content={"success": True})

    return JSONResponse(status_code=200, content={"success": False})


@recuperacao_senha_route.post("/api/recuperacao/atualizar")
async def validar_hash(request: Request):
    body = await request.json()
    email = body.get("email")
    password = body.get("password")

    users_model = UsersModel()
    user = users_model.find_user_email(email=email)
    users_model.update_password(user_key=user.get("_key"), password=password)

    return JSONResponse(status_code=200, content={"success": True})
