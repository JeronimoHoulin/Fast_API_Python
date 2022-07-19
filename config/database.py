# La documentacion de FastAPI tiene un ejemplo usando SQL Alchemy:
# https://fastapi.tiangolo.com/tutorial/sql-databases/?h=sql
### Como no tengo muchisima experiencia usando una base de datos relacional, 
### aunque un poco de SQL conozca, voy a basarme en esto.

" *Segun entendi el ORM es una biblioteca que permite interactuar con una db SQL sin necesariamente ejecutar comandos SQL"

"""
Tested w/ mysql-connector library
----0----
import mysql.connector

mydb = mysql.connector.connect(user='username', password='password!', port='3306',
                              host='127.0.0.1', database='storedb')

----0----

prefered with PyMySQL
from sqlalchemy import create_engine, MetaData

create_engine("mysql+pymysql://root:Password0!@localhost:3306/")

"""

import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

print('Connected to Username: ' + os.getenv('USUARIO_MYSQL'))

username = os.getenv('USUARIO_MYSQL')
password = os.getenv('CONTRASENA_MYSQL')

from sqlalchemy import create_engine, MetaData

engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost:3306/storedb")

meta = MetaData()

connection = engine.connect()