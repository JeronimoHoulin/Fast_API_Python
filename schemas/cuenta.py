from pydantic import BaseModel

class SchemaCuenta(BaseModel):
    id: int
    id_cliente: str

#print("User schema correctly generated!")