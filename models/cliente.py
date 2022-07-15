from sqlalchemy import Table, Column, Integer, String

from config.database import meta, engine

#Una vez que se conecte MySQL creamos una tabla llamada Clientes

clientes = Table("Cientes", meta, Column(
    'id', Integer, primary_key=True),
    Column("nombre", String(225)), 
    Column("apellido", String(225)), 
    Column("email", String(225)), 
    Column("contrasena", String(450)))

meta.create_all(engine)