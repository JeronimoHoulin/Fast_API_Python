from sqlalchemy import String, Table, Column, Integer
from sqlalchemy.sql.sqltypes import Integer
from config.database import meta, engine

#Una vez que se conecte MySQL creamos una tabla llamada Clientes

cuentas = Table("cuentas", meta, 
    Column('id', Integer, primary_key=True),
    Column('id_cliente', Integer, nullable = False),
    Column('categoria', String(225), nullable = False)
    )
    
meta.create_all(engine)