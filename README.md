# Banza-Challenge
### Examen técnico.

Este repositorio contiene una API REST escrita en Python 3.

Utilizando FastAPI y el paquete Uvicorn se generó la applicación vía la cual un cliente podrá hacer consultas, transferencias y modificaciones.

**Para correr la aplicación localmente, después de haber cloneado el repositorio en un Entorno Virtual de Python3 vacío, se deberá correr: "cd Banza-Challenge" y "pip install -r requirments.txt"**

Uvicorn corre el cliente localmente desde el "localhost:8000" utilizando el comando: "uvicorn app:app --reload"

Con el paquete de SQL Alchemy podrán conectarse estas peticiones del cliente con nuestra base de datos relacionales (MySQL) y ejecutar ordenes de tipo put, get, post y delete ó CRUD. 

**Para conetar la applicación con una base de datos MySQL propia deberás renombrar el archivo ".envEXAMPLE" a ".env" y proporcionar tu usuario y contraseña (si no tienes un nombre de usuario especiífico el default es "root")**

La base de datos que se generará se llama "storedb", podrás verla con el comando "SHOW databases;" desde MySQL (CLI ó GUI).

Toda la documentación está explícita en: "localhost:8000/docs", en donde se implementaron los tests para validar todos los endpoints.

https://user-images.githubusercontent.com/79488175/180074800-e5bb473a-fe94-49cd-8ca5-bdf5f64f3694.mp4

La applicación está organizada de la siguiente manera:
*Crear un usuario,
*Crear diferentes cuentas para cada usuario, estas se diferencian con el nombre de la categoría (ej: Usuario X puede tener cuenta #1: "Gold", Cuenta #2: "Silver", Cuenta #3: "Platinum"... etc. pero no puede tener dos cuentas de categoría "Platinum").

Únicamente los endponts que terminan en "{id}" requieren ingresar el id del cliente creado, no es necesario ingresar el campo "id" para los demás ya que se generan automaticamente en la base de datos relacional con la lógica de la función "Increment".

Notar la diferencia entre el "Schema" de un movimiento y el "Modelo" del mismo ya que el primero refiere a la estructura que debe ingresar el cliente y el segundo la que se registra en la base de datos. Al crear un nuevo movimiento se requiere el id del usuario en cuestion, y el nombre de la categoria de la cuenta, MySQL almacenará este movimiento en su respectiva cuenta mientas que le id del movimiento se genera automaticamente.

Finalmente se debe apreciar aunque cada cliente puede tener diferentes cuentas, y estas pueden ser consultadas individualmente, al consultar el estado de la cuenta de un cliente la respuesta incluirá el saldo en pesos como conjunto de todas sus cuentas. Lo mismo para ña funcion "get_total_usd". Esta estructura hará que los movimientos y las cuentas se registren en tablas separadas y que, al borrar una cuenta, sigan existiendo los movimientos de cada usuario. 

*Al borrar una cuenta, existe una lógica de validar si es la única cuenta del cliente, ó este tiene otras cuentas en nuestra base de datos donde podría enviar los fondos. NO existe la lógica que ejecute esta transferencia de fondos de una cuenta a otra... podrá ser agregada en un futuro.
