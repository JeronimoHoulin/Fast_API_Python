from pydantic import BaseModel

class SchemaCuenta(BaseModel):
    id: int
    id_cliente: int

#print("User schema correctly generated!")