from sqlalchemy.sql import func
from fastapi import APIRouter
from config.database import connection
from models.cuenta import cuentas
from schemas.cuenta import SchemaCuenta
from models.cliente import clientes
from models.movimiento import movimientos

#For api and data manipulation
import requests

cuenta = APIRouter()

##################################################################################################################
"""Rutas de Cuentas"""
##################################################################################################################
@cuenta.get('/cuentas', tags=["Cuentas"], response_model=list[SchemaCuenta]) 
def get_Cuentas():
    return connection.execute(cuentas.select()).fetchall()

#Post genera una cuenta nueva:
@cuenta.post('/cuentas', tags=["Clientes"], response_model=SchemaCuenta) 
def create_Cuenta(cuenta: SchemaCuenta):
    nueva_cuenta = cuenta.dict()
    respuesta = connection.execute(cuentas.insert().values(nueva_cuenta))
    print(f"Cuenta agregado correctamente con id: {respuesta.lastrowid}")
    return connection.execute(cuentas.select().where(cuentas.c.id == respuesta.lastrowid)).first()


@cuenta.get('/cuentas/{id}', tags=["Cuentas"])
def get_Cuenta(id: int):
    dueno = connection.execute(clientes.select().where(clientes.c.id == id)).first()
    historial = connection.execute(movimientos.select().where(movimientos.c.id_cuenta == id)).fetchall()

    ingresos = 0
    egresos = 0
    for row in historial:
        #print(row["tipo"])
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


@cuenta.get('/cuentas/{id}/usd', tags=["Cuentas"])
def get_Cuenta_USD(id: int):
    historial = connection.execute(movimientos.select().where(movimientos.c.id_cuenta == id)).fetchall()

    ingresos = 0
    egresos = 0
    for row in historial:
        #print(row["tipo"])
        if row["tipo"] == "ingreso":
            ingresos += row["importe"]
        if row["tipo"] == "egreso":
            egresos += row["importe"]
        else:
            pass

    respuesta = {}

    ############################################ FETCH DOLAR MEP A LA API DE DOLAR SI
    r = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    response = r.json()

    cambio = 0

    for ele in response:
        #print(ele['casa']["nombre"])
        if ele["casa"]["nombre"] == "Dolar Bolsa":
            cambio += float(ele["casa"]["venta"].replace(",", "."))

    #print(cambio)
    respuesta["Saldo_USD"] = (ingresos - egresos)/cambio

    return respuesta