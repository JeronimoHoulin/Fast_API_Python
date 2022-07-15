from sqlalchemy import Table, Column, Integer, String, false
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

#Una vez que se conecte MySQL creamos una tabla llamada Clientes

clientes = Table("clientes", meta, 
    Column('id', Integer, primary_key=True),
    Column("nombre", String(225), nullable=false), 
    Column("apellido", String(225), nullable=false), 
    Column("email", String(225), nullable=false), 
    Column("contrasena", String(450), nullable=false))

meta.create_all(engine)