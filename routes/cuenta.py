import sqlalchemy as db
from fastapi import APIRouter
from config.database import connection
from models.cuenta import cuentas
from models.cliente import clientes
from models.movimiento import movimientos


#Importo movimientos para sumar a la debida cuenta.

cuenta = APIRouter()

##################################################################################################################
"""Rutas de Cuentas"""
##################################################################################################################

@cuenta.get('/cuenta/{id}', tags=["Cuentas"])
def get_Cuenta(id: int):
    dueno = connection.execute(clientes.select().where(clientes.c.id == id)).first()
    historial = connection.execute(movimientos.select().where(movimientos.c.id_cuenta == id)).fetchall()
    print(dueno)
    print("----------------")
    print(historial)
    sum_ingresos = 0
    print(sum_ingresos)
    return "helloooooo"