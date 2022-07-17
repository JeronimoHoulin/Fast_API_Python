from fastapi import APIRouter, Response
from config.database import connection
from models.cliente import clientes
from schemas.cliente import SchemaCliente
from cryptography.fernet import Fernet

#Libreria para cifrar contrasenas
key = Fernet.generate_key()
funcion_cifrar = Fernet(key)

cliente = APIRouter()


##################################################################################################################
"""Rutas de Clientes"""
##################################################################################################################

@cliente.get('/', tags=["Index"]) 
def index():
    return "Hola Cliente!"

#Al consultar por los usuarios, conectamos a la bd, y ejecutamos un "fetch_all" en sql... por ahora un array vacio:
@cliente.get('/clientes', tags=["Clientes"], response_model=list[SchemaCliente]) 
def get_Clientes():
    return connection.execute(clientes.select()).fetchall()

#Post genera una entrada nueva:
@cliente.post('/clientes', tags=["Clientes"], response_model=SchemaCliente) 
def create_Cliente(cliente: SchemaCliente):
    #convertir datos en diccionario que conlleve llave valor acorde al schema del cliente.
    nuevo_cliente = cliente.dict()
    #Quiero cifrar la contrasena que recibimos:
    nuevo_cliente["contrasena"] = funcion_cifrar.encrypt(cliente.contrasena.encode("utf-8"))
    #print(nuevo_cliente) y ahora agregamos a la base de datos:
    respuesta = connection.execute(clientes.insert().values(nuevo_cliente))
    print(f"Cliente agregado correctamente con id: {respuesta.lastrowid}")
    #devolvemos un comando de sql que tome el usuario en la db:
    return connection.execute(clientes.select().where(clientes.c.id == respuesta.lastrowid)).first()

#Consulta de un usuario en particular:
@cliente.get('/cliente/{id}', tags=["Clientes"], response_model=SchemaCliente)
def get_Cliente(id:int):
    return connection.execute(clientes.select().where(clientes.c.id == id)).first()

#Borrar de un usuario en particular:    //aca el response status lo dejo en srt.. aunque podriamos meter un codigo de estado https
@cliente.delete('/cliente/{id}', tags=["Clientes"])
def del_Cliente(id:int):
    result = connection.execute(clientes.delete().where(clientes.c.id == id))
    return f"Cliente nro {id} fue eliminado correctamente!"

#Editar un usuario en particular:
@cliente.put('/cliente/{id}', tags=["Clientes"], response_model=SchemaCliente)
def edit_Cliente(id: int, cliente: SchemaCliente):
    #Dnvo genero el dict a actualizar en mysql:
    update_cliente = cliente.dict()
    update_cliente["contrasena"] = funcion_cifrar.encrypt(cliente.contrasena.encode("utf-8"))

    connection.execute(clientes.update().values(update_cliente).where(clientes.c.id == id))
    return f"Cliente nro {cliente.id} fue actualizado correctamente!"

