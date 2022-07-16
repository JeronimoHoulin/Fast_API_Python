from sqlalchemy import Table, Column, Integer, String, Date
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

#Una vez que se conecte MySQL creamos una tabla llamada Clientes

movimientos = Table("movimientos", meta, 
    Column('id', Integer, primary_key=True),
    Column("id_cuenta", Integer, nullable=False),
    Column("tipo", String(225), nullable=False), 
    Column("importe", Integer, nullable=False), 
    Column("fecha", Date, nullable=False))
    
meta.create_all(engine)
#print("DB's metadata correctly generated!")