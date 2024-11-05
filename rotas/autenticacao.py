from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.login import Login
from database.database import get_connection
from config.auth import gerar_token, validar_token


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Função para fazer login com email e senha
@router.post("/login/")
async def login(usuario: Login):
    # Conecta ao banco de dados
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Verifica se o usuário e senha estão corretos
        cursor.execute("SELECT * FROM usuarios WHERE email =%s AND senha =%s", (usuario.email, usuario.senha))
        row = cursor.fetchone()

        if row:
            # Gera o token JWT com o e-mail como dado para o payload
            token = gerar_token({"sub": usuario.email})
            return {"token": token, "token_type": "bearer"}  # Adiciona token_type
        else:
            # Se o e-mail e senha não estão corretos, retorna um erro
            raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")
    finally:
        cursor.close()
        conn.close()

# Rota protegida (teste alterar depois)
@router.get("/protegido")
async def rota_protegida(token: str = Depends(oauth2_scheme)):
    payload = validar_token(token)  # Verifica o token
    return {"mensagem": "Você está autenticado!", "usuario": payload}
