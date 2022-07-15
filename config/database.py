# La documentacion de FastAPI tiene un ejemplo usando SQL Alchemy:
# https://fastapi.tiangolo.com/tutorial/sql-databases/?h=sql
### Como no tengo muchisima experiencia usando una base de datos relacional, 
### aunque un poco de SQL conozca, voy a basarme en esto.

" *Segun entendi el ORM es una biblioteca que permite interactuar con una db sql"

"""
Test w/ mysql-connector library
import mysql.connector

mydb = mysql.connector.connect(user='root', password='Password0!', port='3306',
                              host='127.0.0.1', database='storedb')

----0----

prefered with PyMySQL
from sqlalchemy import create_engine, MetaData

create_engine("mysql+pymysql://root:Password0!@localhost:3306/")

"""

from sqlalchemy import create_engine, MetaData, Table

engine = create_engine("mysql+pymysql://root:Password0!@localhost:3306/storedb")

meta = MetaData()

connection = engine.connect()