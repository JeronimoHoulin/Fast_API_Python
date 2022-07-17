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


#Consulta de un movimiento en particular:
@movimiento.get('/movimientos/{id}', tags=["Movimientos"], response_model=SchemaMovimiento)
def get_Movimiento(id:int):
    return connection.execute(movimientos.select().where(movimientos.c.id == id)).first()

#Borrar de un movimiento en particular:    
@movimiento.delete('/movimientos/{id}', tags=["Movimientos"])
def del_Movimiento(id:int):
    result = connection.execute(movimientos.delete().where(movimientos.c.id == id))
    return f"Movimiento id nro {id} fue eliminado correctamente!"