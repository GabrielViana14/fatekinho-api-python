from pydantic import BaseModel
from datetime import date
from models.cliente import Cliente
from typing import Optional


class Usuarios(BaseModel):
    idUsuario: int
    email: str
    senha: str
    tipo: int
    idCliente: int  # Ensure this field is included
    cliente: Optional[Cliente] = None  # Optional field if you have a nested model


