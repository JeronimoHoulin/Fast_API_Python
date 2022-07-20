# Banza-Challenge
### Examen técnico.

Este repositorio contiene una API REST escrita en Python 3.

Utilizando FastAPI y el paquete Uvicorn se generó la applicación vía la cual un cliente podrá hacer consultas, transferencias y modificaciones.

**Para correr la aplicación localmente, después de haber cloneado el repositorio en un Entorno Virtual de Python3 vacío, se deberá correr: "cd Banza-Challenge" y "pip install -r requirments.txt"**

Uvicorn corre el cliente localmente desde el "localhost:8000" utilizando el comando: "uvicorn app:app --reload"

Con el paquete de SQL Alchemy podrán conectarse estas peticiones del cliente con nuestra base de datos relacionales (MySQL) y ejecutar ordenes de tipo put, get, post y delete ó CRUD. 

**Para conetar la applicación con tu propia base de datos MySQL deberás renombrar el archivo ".envEXAMPLE" a ".env" y proporcionar tu usuario y contraseña (si no tienes un nombre de usuario especiífico el default es "root")**

La base de datos que se generará se llama "storedb", podrás verla con el comando "SHOW databases;" desde la terminal MySQL CLI ó GUI.

Toda la documentación está explícita en: "localhost:8000/docs", en donde se implementaron los tests para validar todos los endpoints.

La applicación está organizada de la siguiente manera:
*Crear un usuario,
*Crear diferentes cuentas para cada usuario, estas se diferencian con el nombre de la categoría (ej: Usuario X puede tener cuenta #1: "Gold", Cuenta #2: "Silver", Cuenta #3: "Platinum"... etc. pero no puede tener dos cuentas de categoría "Platinum").

Unicamente los endponts que terminan en "{id}" requieren ingresar el id del cliente creado, no es necesario ingresar el campo "id" para los demas ya que se genera automaticamente en la base de datos relacional con la función Increment.

Notar la diferencia entre el Schema de un movimiento y el Modelo del mismo donde el primero refiere a la estructura que debe ingresar el cliente y el segundo la que se registra en la base de datos. Al crear un nuevo movimiento se requiere el id del usuario en cuestion, y el nombre de la categoria de la cuenta, MySQL almacenará este valor en su respectiva cuenta mientas que le id del movimiento se genera con la funcion Increment de MySQL.

Finalmente se debe apreciar aunque cada cliente puede tener diferentes cuentas, y estas pueden ser consultadas individualmente, al consultar el estado de la cuenta de un cliente la respuesta incluirá el saldo en pesos como conjunto de todas sus cuentas. Lo mismo para ña funcion "get_total_usd".
