from pydantic import BaseModel
from typing import Optional

class SchemaCliente(BaseModel):
    id: Optional[int]
    nombre: str
    apellido: str
    email: str
    contrasena: str

#print("User schema correctly generated!")