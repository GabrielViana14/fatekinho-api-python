from fastapi import APIRouter, HTTPException
from models.usuarios import Usuarios
from database.database import get_connection
from config.auth import gerar_token


router = APIRouter()


# Função para fazer login com email e senha
@router.post("/login/")
async def login(usuario: Usuarios):
    # Conecta ao banco de dados
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Verifica se o usuário e senha estão corretos
        cursor.execute("SELECT * FROM usuarios WHERE email =? AND senha =?", (usuario.email, usuario.senha))
        row = cursor.fetchone()

        if row:
            # Gera o token JWT com o e-mail como dado para o payload
            token = gerar_token({"sub": usuario.email})
            return {"token": token}
        else:
            # Se o e-mail e senha não estão corretos, retorna um erro
            raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")
    finally:
        cursor.close()
        conn.close()
