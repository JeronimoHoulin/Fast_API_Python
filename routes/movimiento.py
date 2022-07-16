from fastapi import APIRouter, Response
from config.database import connection
from models.movimiento import movimientos
from schemas.movimiento import SchemaMovimiento

movimiento = APIRouter()

##################################################################################################################
"""Rutas de Movimientos"""
##################################################################################################################

@movimiento.post('/movimiento', tags=["Movimiento"], response_model=SchemaMovimiento) 
def create_Movimiento(movimiento: SchemaMovimiento):
    nuevo_mov = movimiento.dict()
    
    return nuevo_mov