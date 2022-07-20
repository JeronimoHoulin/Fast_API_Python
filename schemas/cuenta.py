from pydantic import BaseModel
from typing import Optional


class SchemaCuenta(BaseModel):
    id: Optional[int]
    id_cliente: int
    categoria: str

# print("Cuenta schema correctly generated!")
