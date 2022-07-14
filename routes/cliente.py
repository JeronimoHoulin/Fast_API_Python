from fastapi import APIRouter
from config.database import conn
from models.cliente import clientes
from schemas.cliente import Cliente
from cryptography.fernet import Fernet

#Libreria para cifrar contrasenas
key = Fernet.generate_key()
funcion_cifrar = Fernet(key)

cliente = APIRouter()

#Al consultar por los usuarios, conectamos a la bd, y ejecutamos un "fetch_all" en sql... por ahora un array vacio:
@cliente.get('/clientes') 
def getClientes():
    return conn.execute(clientes.select()).fetchall()


#Post genera una entrada nueva:
@cliente.post('/clientes') 
def createClientes(cliente: Cliente):
    nuevo_cliente = {"nombre": cliente.nombre, "apellido": cliente.apellido, "email": cliente.email}
    #Sumar al objeto creado una contrasena cirfada
    nuevo_cliente["contrasena"] = funcion_cifrar.encrypt(cliente.contrasena.encode("utf-8"))
    print(nuevo_cliente)
    #un poco mas de sql para sumar el cliente como entrada nueva:
    sumar_entrada = conn.execute(clientes.insert().values([nuevo_cliente]))
    print(type(sumar_entrada))
    return print(f"Respuesta del usuario en la base de datos: {sumar_entrada}")
