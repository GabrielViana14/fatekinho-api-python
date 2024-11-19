from pydantic import BaseModel
from datetime import date
from models.cliente import Cliente
from typing import Optional


class Usuarios(BaseModel):
    email: str
    senha: str
    tipo: Optional[str] = None


class UsuariosRead(BaseModel):
    idUsuario: int
    email: str
    senha: str
    tipo: Optional[str] = None


