from pydantic import BaseModel
from typing import Optional

class SchemaCliente(BaseModel):
    id: Optional[str]
    nombre: str
    apellido: str
    email: str
    contrasena: str

#print("User schema correctly generated!")