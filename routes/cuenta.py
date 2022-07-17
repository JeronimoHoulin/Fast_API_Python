from sqlalchemy.sql import func
from fastapi import APIRouter
from config.database import connection
from models.cuenta import cuentas
from models.cliente import clientes
from models.movimiento import movimientos

#For api and data manipulation
import requests

cuenta = APIRouter()

##################################################################################################################
"""Rutas de Cuentas"""
##################################################################################################################

@cuenta.get('/cuenta/{id}', tags=["Cuentas"])
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

    ############################################ FETCH DOLAR MEP A LA API DE DOLAR SI

    r = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    response = r.json()
    #print(response)

    cambio = 0

    for ele in response:
        #print(ele['casa']["nombre"])
        if ele["casa"]["nombre"] == "Dolar Bolsa":
            cambio += float(ele["casa"]["venta"].replace(",", "."))

    print(cambio)
    
    return respuesta