from fastapi import APIRouter
from config.database import connection
from models.cliente import clientes
from schemas.cliente import SchemaCliente
from cryptography.fernet import Fernet

#Libreria para cifrar contrasenas
key = Fernet.generate_key()
funcion_cifrar = Fernet(key)

cliente = APIRouter()

@cliente.get('/') 
def index():
    return "Hello Client!"

#Al consultar por los usuarios, conectamos a la bd, y ejecutamos un "fetch_all" en sql... por ahora un array vacio:
@cliente.get('/clientes') 
def getClientes():
    return connection.execute(clientes.select()).fetchall()


#Post genera una entrada nueva:
@cliente.post('/clientes') 
def createClientes(cliente: SchemaCliente):
    #convertir datos en diccionario que conlleve llave valor acorde al schema del cliente.
    nuevo_cliente = cliente.dict()
    #Quiero cifrar la contrasena que recibimos:
    nuevo_cliente["contrasena"] = funcion_cifrar.encrypt(cliente.contrasena.encode("utf-8"))
    #print(nuevo_cliente) y ahora agregamos a la base de datos:
    respuesta = connection.execute(clientes.insert().values(nuevo_cliente))
    return f"Cliente agregado correctamente!"

