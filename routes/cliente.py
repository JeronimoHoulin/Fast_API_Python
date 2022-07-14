from fastapi import APIRouter
from config.database import conn
from models.cliente import clientes

cliente = APIRouter()

#Al consultar por los usuarios, conectamos a la bd, y ejecutamos un "fetch_all" en sql.
@cliente.get('/clientes') 
def getClientes():
    return conn.execute(clientes.select()).fetchall()
