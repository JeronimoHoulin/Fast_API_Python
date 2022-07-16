from pydantic import BaseModel
from typing import Optional

class SchemaMovimiento(BaseModel):
    id: Optional[str]
    id_cuenta: int
    id_cliente: int
    tipo: str
    importe: int
    fecha: str

#print("Schema de movimiento generado correctamente!")