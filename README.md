# Banza-Challenge
### Examen técnico.

Este repositorio contiene una API REST escrita en Python 3.

Utilizando FastAPI y el paquete Uvicorn se generó la applicación vía la cual un cliente podrá hacer consultas, transferencias y modificaciones.

Uvicorn corre el cliente localmente desde el "localhost:8000" utilizando el comando: "uvicorn app:app --reload"

Con el paquete de SQL Alchemy podrán conectarse estas peticiones del cliente con nuestra base de datos relacionales (MySQL) y ejecutar ordenes de tipo put, get, post y delete. 

* **Para conetar la applicación con tu propia base MySQL deberás proporcionar tu usuario y contraseña en el archivo .ENV**

Toda la documentación está explícita en el endpoint: "localhost:8000/docs".
