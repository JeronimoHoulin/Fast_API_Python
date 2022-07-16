from fastapi import APIRouter, Response
from config.database import connection
from models.cuenta import cuentas
from models.movimiento import movimientos
from schemas.cuenta import SchemaCuenta

#Importo movimientos para sumar a la debida cuenta.

cuenta = APIRouter()

##################################################################################################################
"""Rutas de Cuentas"""
##################################################################################################################

@cuenta.get('/cuenta/{id}', tags=["Cuentas"], response_model=SchemaCuenta)
def get_Cuenta():
    return connection.execute(movimientos.select().where(movimientos.c.id_cuenta == id)).first()