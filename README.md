# Banza-Challenge
### Examen técnico.

Este repositorio contiene una API REST escrita en Python 3.

Utilizando FastAPI y el paquete Uvicorn se generó la applicación vía la cual un cliente podrá hacer consultas, transferencias y modificaciones.

Uvicorn corre el cliente localmente desde el "localhost:8000" utilizando el comando: "uvicorn app:app --reload"

Con el paquete de SQL Alchemy podrán conectarse estas peticiones del cliente con nuestra base de datos relacionales (MySQL) y ejecutar ordenes de tipo put, get, post y delete. 

**Para conetar la applicación con tu propia base MySQL deberás renombrar el archivo ".envSAMPLE" a ".env" y proporcionar tu usuario y contraseña (si no tienes un nombre de usuario espec[ifico el default es "root")**

La base de datos que se generará se llama "storedb", podrás verla con el comando "show databases;" desde la terminal de MySQL.

Toda la documentación está explícita en el endpoint: "localhost:8000/docs", en donde se implementaron los tests para validar los endpoints.

Unicamente los endponts que terminan en "{id}" requieren ingresar el id del cliente, no es necesario ingresar el campo "id" para los demas ya que se genera automaticamente en la base de datos relacional con la función Increment.

Notar la diferencia entre el Schema de un movimiento y el Modelo del mismo donde el primero refiere a la estructura que debe ingresar el cliente y el segundo la que se registra en la base de datos. 