# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:03:46 2022

@author: Jerry H.
"""

from fastapi import FastAPI
from routes.cliente import cliente
from routes.movimiento import movimiento
from routes.cuenta import cuenta


app = FastAPI(
    title="Banza Challenge // Jerónimo H.",
    description="Este es un REST API para generar y registrar movimientos monetarios que utiliza FastAPI y MySQL!"
)

app.include_router(cliente)
app.include_router(cuenta)
app.include_router(movimiento)