from fastapi import APIRouter, HTTPException
from models.histWonLose import HistWonLose
from database.database import get_connection
from typing import List

router = APIRouter()

# Create new historico
@router.post("/histWonLose")
async def create_historico(historico: HistWonLose):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO HistoricoGanhosPercas (idJogo, idUsuario, valorApostado, ganhou, valorFinalApostado, dataCadastro)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            historico.idJogo,
            historico.idUsuario,
            historico.valorApostado,
            historico.ganhou,
            historico.valorFinalApostado,
            historico.dataCadastro
        ))

        cursor.execute("SELECT SCOPE_IDENTITY()")
        new_id = cursor.fetchone()[0]

        conn.commit()
        return {
            "idHistoricoGanhos": new_id,
            "idJogo": historico.idJogo,
            "idUsuario": historico.idUsuario,
            "valorApostado": historico.valorApostado,
            "ganhou": historico.ganhou,
            "valorFinalApostado": historico.valorFinalApostado,
            "dataCadastro": historico.dataCadastro
        }

    finally:
        cursor.close()
        conn.close()

# Get all historico
@router.get("/histWonLose/all/", response_model=List[HistWonLose])
async def get_all_historico():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM HistoricoGanhosPercas")
        rows = cursor.fetchall()
        historico_array = []
        for row in rows:
            historico = HistWonLose(
                idJogo=row[0],
                idUsuario=row[1],
                valorApostado=row[2],
                ganhou=row[3],
                valorFinalApostado=row[4],
                dataCadastro=row[5]
            )
            historico_array.append(historico)
        return historico_array
    finally:
        cursor.close()
        conn.close()
