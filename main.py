import pyodbc
from fastapi import FastAPI, HTTPException
from fastapi_pagination import Page, paginate
from models.cliente import Cliente
from models.usuarios import Usuarios
from typing import List

app = FastAPI()

# Para testar API só usar a url: http://127.0.0.1:8000/docs
# caso esteja em outra url é só adicionar o /docs no final da url


def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=fatekinho-fatec.database.windows.net,1433;'
        'DATABASE=fatekinho;'
        'UID=admin1@fatekinho-fatec;'
        'PWD=Admin@2024;'
        'Encrypt=yes;'
        'TrustServerCertificate=no;'
        'Connection Timeout=30;'
    )
    return conn


# -----------------------------
# Operações da Tabela Clientes
# -----------------------------

# Create in Clientes
@app.post("/clientes/")
async def create_cliente(cliente: Cliente):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Inserção de todos os campos na tabela `clientes`
        cursor.execute("""
            INSERT INTO clientes (nome, data_nasc, cpf, cep, numero, complemento) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            cliente.nome,
            cliente.data_nasc,
            cliente.cpf,
            cliente.cep,
            cliente.numero,
            cliente.complemento
        ))

        conn.commit()
        return {
            "id_cliente": cursor.lastrowid,
            "nome": cliente.nome,
            "data_nasc": cliente.data_nasc,
            "cpf": cliente.cpf,
            "cep": cliente.cep,
            "numero": cliente.numero,
            "complemento": cliente.complemento}
    finally:
        cursor.close()
        conn.close()


# Read in Clientes
@app.get("/clientes/{id}")
async def get_cliente(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes WHERE id_cliente =?", (id,))
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
@app.put("/clientes/{id}")
async def update_cliente(id: int, cliente: Cliente):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Atualizar todos os campos do cliente
        cursor.execute("""
            UPDATE clientes 
            SET nome = ?, data_nasc = ?, cpf = ?, cep = ?, numero = ?, complemento = ? 
            WHERE id = ?
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
@app.delete("/clientes/{id}")
async def delete_cliente(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM clientes WHERE id =?", (id,))
        conn.commit()
        return {"mensagem": "Registro excluído com sucesso"}
    finally:
        cursor.close()
        conn.close()

# Get all cliente
@app.get("/clientes/all/", response_model=List[Cliente])
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



# -----------------------------
# Operações da Tabela Usuarios
# -----------------------------

# Create in Usuarios
@app.post("/usuarios/")
async def create_usuario(usuario: Usuarios):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Inserção de todos os campos na tabela `clientes`
        cursor.execute("""
            INSERT INTO usuarios (email, senha, tipo, idCliente) 
            VALUES (?, ?, ?, ?)
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
@app.get("/usuarios/{id}")
async def get_usuario(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM usuarios WHERE idUsuario =?", (id,))
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
@app.put("/usuarios/{id}")
async def update_usuario(id: int, usuario: Usuarios):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Atualizar todos os campos do cliente
        cursor.execute("""
            UPDATE clientes 
            SET email = ?, senha = ?, tipo = ?, idCliente = ? 
            WHERE idUsuario = ?
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
@app.delete("/usuarios/{id}")
async def delete_usuario(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM usuarios WHERE idUsuario =?", (id,))
        conn.commit()
        return {"mensagem": "Registro excluído com sucesso"}
    finally:
        cursor.close()
        conn.close()

# Get all usuarios
@app.get("/usuarios/all/", response_model=List[Usuarios])
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

