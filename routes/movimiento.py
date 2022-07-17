from fastapi import APIRouter, Response
from config.database import connection
from models.movimiento import movimientos
from schemas.movimiento import SchemaMovimiento

from datetime import date

movimiento = APIRouter()

##################################################################################################################
"""Rutas de Movimientos"""
##################################################################################################################

@movimiento.post('/movimiento', tags=["Movimientos"]) 
def create_Movimiento(movimiento: SchemaMovimiento):
    nuevo_mov = movimiento.dict()
    #print(nuevo_mov["importe"])
    ##################################### Validación de el tipo de movimiento:
    respuesta = {}

    if nuevo_mov["fecha"] > date.today():
        nuevo_mov = {}
        nuevo_mov["error"] = "El campo de FECHA no puede estar en el futuro!"

    elif nuevo_mov["importe"] < 0:
        nuevo_mov = {}
        nuevo_mov["error"] = "El campo de IMPORTE tiene que ser positivo!"

    else:
        respuesta = connection.execute(movimientos.insert().values(nuevo_mov))
        
    return nuevo_mov


@movimiento.get('/movimientos', tags=["Movimientos"], response_model=list[SchemaMovimiento]) 
def get_Movimientos():
    return connection.execute(movimientos.select()).fetchall()