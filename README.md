# Jiujitsu application database

The database which will be used is [PostgreSQL](https://www.postgresql.org/). 

The database container will be managed by `Docker` using a `docker-compose.yml` file.

The migrations will be managed by `Python`. 

# Creating an running a virtual environment

To create a virtual environment, run the following command (make sure you have virtualenv installed!)

```
virtualenv venv-db
```

Activating the virtual environment:

```
source venv-db/bin/activate
```

Installing the requirements:

```
pip install -r requirements.txt
```

# Upping the database container

To up the database container, run the following command:

```
docker-compose up -d
```

# Managing the database with alembic 

To create a new migration, run the following command:

    ```
    alembic revision --autogenerate -m "migration message"
    ```

To apply the created migration, use the command: 
    
    ```
    alembic upgrade head
    ```