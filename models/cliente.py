from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Cliente(BaseModel):
    id_cliente: Optional[int] = None  # `id` é opcional durante a criação
    nome: str
    data_nasc: datetime  # Data de nascimen
    cpf: int
    cep: str
    numero: int
    complemento: Optional[str] = Field(default="")
