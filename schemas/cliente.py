from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    id: Optional[str]
    nombre: str
    apellido: str
    email: str
    contrasena: str