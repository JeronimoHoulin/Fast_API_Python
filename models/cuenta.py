from sqlalchemy import Table, Column, Integer
from sqlalchemy.sql.sqltypes import Integer
from config.database import meta, engine

#Una vez que se conecte MySQL creamos una tabla llamada Clientes

cuentas = Table("cuentas", meta, 
    Column('id', Integer, primary_key=True),
    Column('id_cliente', Integer, nullable = False)
    )
    
meta.create_all(engine)