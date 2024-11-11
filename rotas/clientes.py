from fastapi import APIRouter, HTTPException
from models.cliente import Cliente
from database.database import get_connection
from typing import List

router = APIRouter()


# Create in Clientes
@router.post("/clientes/")
async def create_cliente(cliente: Cliente):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Inserção de todos os campos na tabela `clientes`
        cursor.execute("""
            INSERT INTO clientes (nome, data_nasc, cpf, cep, numero, complemento) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            cliente.nome,
            cliente.data_nasc,
            cliente.cpf,
            cliente.cep,
            cliente.numero,
            cliente.complemento
        ))
        # Obtém o último id inserido usando SCOPE_IDENTITY()
        cursor.execute("SELECT SCOPE_IDENTITY()")
        new_id = cursor.fetchone()[0]

        conn.commit()
        return {
            "id_cliente": new_id,
            "nome": cliente.nome,
            "data_nasc": cliente.data_nasc,
            "cpf": cliente.cpf,
            "cep": cliente.cep,
            "numero": cliente.numero,
            "complemento": cliente.complemento
        }
    finally:
        cursor.close()
        conn.close()


# Read in Clientes
@router.get("/clientes/{id}")
async def get_cliente(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id,))
        row = cursor.fetchone()

        if row:
            return {
                "id_cliente": row[0],
                "nome": row[1],
                "data_nasc": row[2],
                "cpf": row[3],
                "cep": row[4],
                "numero": row[5],
                "complemento": row[6]
            }
        else:
            raise HTTPException(status_code=404, detail="Registro não encontrado.")
    finally:
        cursor.close()
        conn.close()


# Update in Clientes
@router.put("/clientes/{id}")
async def update_cliente(id: int, cliente: Cliente):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Atualizar todos os campos do cliente
        cursor.execute("""
            UPDATE clientes 
            SET nome = %s, data_nasc = %s, cpf = %s, cep = %s, numero = %s, complemento = %s 
            WHERE id = %s
        """, (
            cliente.nome,
            cliente.data_nasc,
            cliente.cpf,
            cliente.cep,
            cliente.numero,
            cliente.complemento,
            id
        ))

        conn.commit()

        # Verifica se a atualização foi bem-sucedida
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")

        return {
            "id": id,
            "nome": cliente.nome,
            "data_nasc": cliente.data_nasc,
            "cpf": cliente.cpf,
            "cep": cliente.cep,
            "numero": cliente.numero,
            "complemento": cliente.complemento
        }

    finally:
        cursor.close()
        conn.close()


# Delete in Clientes
@router.delete("/clientes/{id}")
async def delete_cliente(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM clientes WHERE id =%s", (id,))
        conn.commit()
        return {"mensagem": "Registro excluído com sucesso"}
    finally:
        cursor.close()
        conn.close()


# Get all cliente
@router.get("/clientes/all/", response_model=List[Cliente])
async def get_all_clientes():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        clientes = []
        for row in rows:
            cliente = Cliente(
                id_cliente=row[0],
                nome=row[1],
                data_nasc=row[2],
                cpf=row[3],
                cep=row[4],
                numero=row[5],
                complemento=row[6]
            )
            clientes.append(cliente)
        return clientes
    finally:
        cursor.close()
        conn.close()

