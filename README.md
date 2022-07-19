# Banza-Challenge
### Examen técnico.

Este repositorio contiene una API REST escrita en Python 3.

Utilizando FastAPI y el paquete Uvicorn se generó la applicación vía la cual un cliente podrá hacer consultas, transferencias y modificaciones.

Uvicorn corre el cliente localmente desde el "localhost:8000" utilizando el comando: "uvicorn app:app --reload"

Con el paquete de SQL Alchemy podrán conectarse estas peticiones del cliente con nuestra base de datos relacionales (MySQL) y ejecutar ordenes de tipo put, get, post y delete. 

* **Para conetar la applicación con tu propia base MySQL deberás renombrar el archivo ".envSAMPLE" a ".env" y proporcionar tu usuario y contraseña (si no tienes un nombre de usuario espec[ifico el default es "root")**

La base de datos que se generará se llama "storedb", podrás verla con el comando "show databases;" desde la terminal de MySQL.

Toda la documentación está explícita en el endpoint: "localhost:8000/docs".
