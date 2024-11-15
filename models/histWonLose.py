from datetime import datetime
from pydantic import BaseModel


class HistWonLose(BaseModel):
    idJogo: int
    idUsuario: int
    valorApostado: float
    ganhou: int
    valorFinalApostado: float
    dataCadastro: datetime
