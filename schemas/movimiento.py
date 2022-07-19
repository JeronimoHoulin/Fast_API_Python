from datetime import date
from pydantic import BaseModel
from typing import Optional

class SchemaMovimiento(BaseModel):
    id: Optional[int]
    tipo: str
    importe: int
    fecha: date

#print("Schema de movimiento generado correctamente!")