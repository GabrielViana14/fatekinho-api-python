from pydantic import BaseModel
from typing import List

class tabelaCombinada(BaseModel):
    id: int
    tipo: str
    data: str


class tabelaCombinadaResponse(BaseModel):
    items: List[tabelaCombinada]