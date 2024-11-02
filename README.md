### Create a Postgres DB
- Download postgresql: https://www.postgresql.org/download/
- Download pgadmin to visualize data in a dashboard: https://www.pgadmin.org
- Create a db and insert the connection string in DATABASE_URL environment variable (.env file). Connection string structure: postgresql+psycopg2://\<username\>:\<password\>@\<host\>:\<port\>/\<db_name\>

### Install requirements for the project
- install conda https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html
- create conda environment with ``` conda create -n <env-name> ```
- activate conda environment with ``` conda activate <env-name> ```
- execute ``` pip install  -r requirements.txt```

### Import data into Postgres DB
- execute ``` python import_data.py```

### Project structure
- ``` model\model.py ``` contains a ORM definition (https://docs.sqlalchemy.org/en/20/orm/quickstart.html) of the tables in the DB
- ``` src\config\db.py ``` contains the code to connect at the db and other useful db functions
- ``` src\plugin\repository.py ``` contains all the db queries

- ``` src\plugin\service.py ``` calls the repository functions and it applies some logics to obtain the desired result

- ```src\plugin\controller.py ``` creates the session for quering the db and it handles error

- ```.env``` file contains environment variables
- In ```requirements.txt``` there is a list of the project dependencies