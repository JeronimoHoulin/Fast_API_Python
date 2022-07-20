from sqlalchemy.sql import func
from fastapi import APIRouter
from config.database import connection
from models.cuenta import cuentas
from schemas.cuenta import SchemaCuenta
from models.cliente import clientes
from models.movimiento import movimientos

# For api and data manipulation
import requests

cuenta = APIRouter()

##################################################################################################################
"""Rutas de Cuentas"""


##################################################################################################################
@cuenta.get('/cuentas', tags=["Cuentas"], response_model=list[SchemaCuenta])
def get_Cuentas():
    return connection.execute(cuentas.select()).fetchall()


# Post genera una cuenta nueva:
@cuenta.post('/cuentas', tags=["Cuentas"])
def create_Cuenta(cuenta: SchemaCuenta):
    nueva_cuenta = cuenta.dict()
    # Validacion de categoria existente:
    id_cliente = nueva_cuenta['id_cliente']
    categ = nueva_cuenta['categoria']

    r = requests.get(f'http://localhost:8000/cuentas/{id_cliente}')
    response = r.json()
    result = {}

    for row in response:
        if categ == row["categoria"]:
            result[
                'error'] = f"El cliente ya tiene una cta con categoria {categ}"
        else:
            pass
    if 'error' not in result.keys():
        respuesta = connection.execute(cuentas.insert().values(nueva_cuenta))
        result["sucess"] = f"Cuenta agregada correctamente!"

    return result


# Borrar de un usuario en particular:    //aca el response status lo dejo en srt.. aunque podriamos meter un codigo de estado https
@cuenta.delete('/cuenta/{id}', tags=["Cuentas"])
def del_Cuenta(id: int):
    #valido que el usuario tenga otras cuentas:
    r = requests.get(f'http://localhost:8000/cuentas/{id}')
    response = r.json()

    if len(response) == 0:
        result = {}
        result["error"] = f"El cliente no tiene cuenta con id: {id}. Creá una cuenta!"

    #Si tiene solo una cuenta deberá retirar sus fondos:
    elif len(response) == 1:
        #print("solo tiene una cta")
        for row in response:
            cliente = row["id_cliente"]
            categ = row["categoria"]
        result = {}
        result["error"] = f"El cliente {cliente} tiene una sola cuenta. Deberá retirar sus fondos de su cuenta {categ} con id: {id}"

    elif len(response) > 1: 
        for row in response:
            cliente = row["id_cliente"]
            categ = row["categoria"]
        result = {}
        result["sucess"] = f"El cliente {cliente} deberá retirar sus fondos de su cuenta con id: {id} hacia una cuenta de otra categoría!"
        result["cta_eliminada"] = connection.execute(cuentas.delete().where(cuentas.c.id == id))

    return result
    

@cuenta.get('/cuentas/{id}', tags=["Cuentas"],
            response_model=list[SchemaCuenta])
def get_Cuentas_cliente(id: int):
    return connection.execute(
        cuentas.select().where(cuentas.c.id_cliente == id)).fetchall()


@cuenta.get('/cuenta/{id}', tags=["Cuentas"])
def get_Cuenta(id: int):
    dueno = connection.execute(
        clientes.select().where(clientes.c.id == id)).first()
    historial = connection.execute(
        movimientos.select().where(movimientos.c.id_cliente == id)).fetchall()

    ingresos = 0
    egresos = 0
    for row in historial:
        # print(row["tipo"])
        if row["tipo"] == "ingreso":
            ingresos += row["importe"]
        if row["tipo"] == "egreso":
            egresos += row["importe"]
        else:
            pass
    print(f"Movimientos de cliente nro {id}:")
    print("--------0--------")
    print(f"ingresos netos: {ingresos}")
    print(f"egresos netos: {egresos}")
    print("----------------")
    print(f"Saldo: {ingresos - egresos}")

    respuesta = {}
    respuesta["SaldoActual"] = ingresos - egresos
    respuesta["Historial"] = historial

    return respuesta


@cuenta.get('/cuenta/{id}/get_total_usd', tags=["Cuentas"])
def get_Cuenta_USD(id: int):
    historial = connection.execute(
        movimientos.select().where(movimientos.c.id_cliente == id)).fetchall()

    ingresos = 0
    egresos = 0
    for row in historial:
        # print(row["tipo"])
        if row["tipo"] == "ingreso":
            ingresos += row["importe"]
        if row["tipo"] == "egreso":
            egresos += row["importe"]
        else:
            pass

    respuesta = {}

    ############################################ FETCH DOLAR MEP A LA API DE DOLAR SI
    r = requests.get(
        'https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    response = r.json()

    cambio = 0

    for ele in response:
        # print(ele['casa']["nombre"])
        if ele["casa"]["nombre"] == "Dolar Bolsa":
            cambio += float(ele["casa"]["venta"].replace(",", "."))

    # print(cambio)
    respuesta["Saldo_USD"] = (ingresos - egresos) / cambio

    return respuesta
