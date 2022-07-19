from pydantic import BaseModel

class SchemaCuenta(BaseModel):
    id: int
    id_cliente: int
    categoria: str

#print("User schema correctly generated!")