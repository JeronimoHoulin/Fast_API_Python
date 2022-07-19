from fastapi import APIRouter, Response
from config.database import connection
from models.movimiento import movimientos
from models.cuenta import cuentas
from schemas.movimiento import SchemaMovimiento

import requests

from datetime import date

movimiento = APIRouter()

##################################################################################################################
"""Rutas de Movimientos"""
##################################################################################################################

@movimiento.post('/movimiento/{id}', tags=["Movimientos"]) 
def create_Movimiento(id:int, movimiento: SchemaMovimiento):
    nuevo_mov = movimiento.dict()
    nuevo_mov["id_cuenta"] = id
    id_cliente = nuevo_mov["id_cuenta"]

    r = requests.get(f'http://localhost:8000/cuenta/{id_cliente}')
    response = r.json()
    saldo = response["SaldoActual"]

    ##################################### Validación de el tipo de movimiento:
    if nuevo_mov["fecha"] > date.today():
        nuevo_mov = {}
        nuevo_mov["error"] = "El campo de FECHA no se puede programar en el futuro!"

    elif nuevo_mov["importe"] < 0:
        nuevo_mov = {}
        nuevo_mov["error"] = "El campo de IMPORTE tiene que ser positivo!"

    ##################################### Validación de fondos para egresos:
    elif nuevo_mov["tipo"] == "egreso":
        if nuevo_mov["importe"] > saldo:
            nuevo_mov = {}
            nuevo_mov["error"] = "Egreso rechazado; fondos insuficientes!"
        else:
            pass

    ##################################### Si todo pasa.. registro el egreso:
    else:
        respuesta = connection.execute(movimientos.insert().values(nuevo_mov))
        print('Egresarán '+ str(nuevo_mov["importe"]) + ' pesos.')
    return nuevo_mov


@movimiento.get('/movimientos', tags=["Movimientos"], response_model=list[SchemaMovimiento]) 
def get_Movimientos():
    return connection.execute(movimientos.select()).fetchall()


#Consulta de un movimiento en particular:
@movimiento.get('/movimientos/{id}', tags=["Movimientos"], response_model=SchemaMovimiento)
def get_Movimiento(id:int):
    return connection.execute(movimientos.select().where(movimientos.c.id == id)).first()

#Borrar de un movimiento en particular:    
@movimiento.delete('/movimientos/{id}', tags=["Movimientos"])
def del_Movimiento(id:int):
    result = connection.execute(movimientos.delete().where(movimientos.c.id == id))
    return f"Movimiento id nro {id} fue eliminado correctamente!"