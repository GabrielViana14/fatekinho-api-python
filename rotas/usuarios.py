from fastapi import APIRouter, HTTPException
from database.database import get_connection
from models.usuarios import Usuarios
from typing import List

router = APIRouter()


# Create in Usuarios
@router.post("/usuarios/")
async def create_usuario(usuario: Usuarios):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Inserção de todos os campos na tabela `clientes`
        cursor.execute("""
            INSERT INTO usuarios (email, senha, tipo, idCliente) 
            VALUES (%s, %s, %s, %s)
        """, (
            usuario.email,
            usuario.senha,
            usuario.tipo,
            usuario.idCliente
        ))

        conn.commit()
        return {
            "idUsuario": cursor.lastrowid,
            "email": usuario.email,
            "senha": usuario.senha,
            "tipo": usuario.tipo,
            "idCliente": usuario.idCliente

        }
    finally:
        cursor.close()
        conn.close()


# Read in Usuarios
@router.get("/usuarios/{id}")
async def get_usuario(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM usuarios WHERE idUsuario =%s", (id,))
        row = cursor.fetchone()

        if row:
            return {
                "idUsuario": row[0],
                "email": row[1],
                "senha": row[2],
                "tipo": row[3],
                "idCliente": row[4]
            }
        else:
            raise HTTPException(status_code=404, detail="Registro não encontrado.")
    finally:
        cursor.close()
        conn.close()

# Update in Usuarios
@router.put("/usuarios/{id}")
async def update_usuario(id: int, usuario: Usuarios):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Atualizar todos os campos do cliente
        cursor.execute("""
            UPDATE clientes 
            SET email = %s, senha = %s, tipo = %s, idCliente = %s 
            WHERE idUsuario = %s
        """, (
            usuario.email,
            usuario.senha,
            usuario.tipo,
            usuario.idCliente,
            id
        ))

        conn.commit()

        # Verifica se a atualização foi bem-sucedida
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuario não encontrado")

        return {
            "idUsuario": id,
            "email": usuario.email,
            "senha": usuario.senha,
            "tipo": usuario.tipo,
            "idCliente": usuario.idCliente
        }

    finally:
        cursor.close()
        conn.close()

# Delete in Usuarios
@router.delete("/usuarios/{id}")
async def delete_usuario(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM usuarios WHERE idUsuario =%s", (id,))
        conn.commit()
        return {"mensagem": "Registro excluído com sucesso"}
    finally:
        cursor.close()
        conn.close()

# Get all usuarios
@router.get("/usuarios/all/", response_model=List[Usuarios])
async def get_all_usuarios():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        usuarios = []
        for row in rows:
            usuario = Usuarios(
                idUsuario=row[0],
                email=row[1],
                senha=row[2],
                tipo=row[3],
                idCliente=row[4]
            )
            usuarios.append(usuario)
        return usuarios
    finally:
        cursor.close()
        conn.close()