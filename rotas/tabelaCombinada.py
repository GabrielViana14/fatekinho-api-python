from fastapi import APIRouter, HTTPException
from database.database import get_connection
from models.tabelaCombinada import tabelaCombinada, tabelaCombinadaResponse
from typing import List
from datetime import datetime

router = APIRouter()



async def get_combined_items(id: int) -> List[tabelaCombinada]:
    conn = get_connection()
    cursor = conn.cursor()
    # Query para buscar dados de ambas as tabelas, unindo com UNION ALL
    query = """
        SELECT 'HistoricoGanhosPercas' AS origem, dataCadastro FROM HistoricoGanhosPercas WHERE idUsuario = %s
        UNION ALL
        SELECT 'fatecoins' AS origem, qtd FROM fatecoins WHERE idUsuario = %s
        """

    try:
        cursor.execute(query, (id, id))
        rows = cursor.fetchall()
        itens = []
        id_cont = 1

        for row in rows:
            origem = row[0]
            data_cadastro = row[1]
            # Se data_cadastro for um objeto datetime, converta para string
            if isinstance(data_cadastro, datetime):
                data_cadastro = data_cadastro.strftime('%Y-%m-%d %H:%M:%S')  # Formato desejado
            itens.append(
                tabelaCombinada(
                    id= id_cont,
                    tipo=origem,
                    data=data_cadastro
                )
            )
            id_cont += 1
        return itens
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar os dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

# Read in table combin
@router.get("/table-comb/{id}",response_model=tabelaCombinadaResponse)
async def get_table_combined_items(id: int):
    try:
        itens = await get_combined_items(id)
        return tabelaCombinadaResponse(items=itens)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar os dados: {str(e)}")
