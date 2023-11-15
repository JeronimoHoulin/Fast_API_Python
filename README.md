# FAST API (Python REST API library).
## Bank / Fintech Backend API simulation. 

This repository contains a REST API written in Python 3.

Using FastAPI and the Uvicorn package, an application was generated through which a client can make queries, transfers, and modifications.

To run the application locally, after cloning the repository into an empty Python3 Virtual Environment, run: "cd Banza-Challenge" and "pip install -r requirements.txt"

Uvicorn runs the client locally from "localhost:8000" using the command: "uvicorn app:app --reload"

The SQL Alchemy package connects these client requests to our relational database (MySQL) and executes CRUD operations such as put, get, post, and delete.

To connect the application to your own MySQL database, you should rename the ".envEXAMPLE" file to ".env" and provide your username and password (if you don't have a specific username, the default is "root").

The generated database is named "storedb," and you can view it with the command "SHOW databases;" from MySQL (CLI or GUI).

All documentation is available at: "localhost:8000/docs," where tests have been implemented to validate all endpoints. Below is a video demonstrating the first three actions that must be taken to generate Users, Accounts, and transactions:

https://user-images.githubusercontent.com/79488175/180074800-e5bb473a-fe94-49cd-8ca5-bdf5f64f3694.mp4

The application is organized as follows:

Create a user,
Create different accounts for each user, distinguished by category names (e.g., User X can have account #1: "Gold," Account #2: "Silver," Account #3: "Platinum," etc., but cannot have two accounts of the "Platinum" category).
Only endpoints ending in "{id}" require entering the created client's id; it is not necessary to enter the "id" field for the others as they are generated automatically in the relational database with the logic of the "Increment" function.

Note the difference between the "Schema" of a movement and its "Model," as the former refers to the structure that the client must enter, and the latter is what is recorded in the database. When creating a new movement, the id of the user in question and the name of the account category are required; MySQL will store this movement in its respective account, while the movement id is generated automatically.

Finally, although each client can have different accounts, and these can be queried individually, when checking the status of a client's account, the response will include the balance in pesos as the sum of all their accounts. The same applies to the "get_total_usd" function. This structure ensures that movements and accounts are recorded in separate tables, and when deleting an account, the movements of each user will still exist.

*When deleting an account, there is logic to validate if it is the only account for the client or if the client has other accounts in our database where funds could be transferred. There is currently no logic to execute this fund transfer from one account to another, but it may be added in the future.
