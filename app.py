# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:03:46 2022

@author: Jerry H.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hellouvicorn():
    return "hello Uvicorn"