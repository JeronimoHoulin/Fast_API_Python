from sqlalchemy import Table, Column, Integer, String

from config.database import meta, engine

#Una vez que se conecte MySQL creame una tabla llamada Clientes

clientes = Table("Clientes", meta, Column(
    'id', Integer, primary_key=True),
    Column("Nombre", String(225)))

meta.create_all(engine)