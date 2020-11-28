# Micro API 

Snippet of structure for microservice with aiohttp.  
Contains deferred tasks by faust.  
Draft api spec by Swagger in api-spec.yml  

# Usage
``` bash

pip install -e .
python -m micro_api 
```  
or  
``` bash
dicker-compose build api
docker-compose run -p 127.0.0.1:8080:8080 api
```  

# Settings  
Parametrize from arguments of running or values of environment:  
Advice: use file `.env` in root directory for docker-compose. 
``` 
`DEBUG`: Debug regime which set log level to debug level  
`LOG_LEVEL`: Python logging level [default: INFO]  
`POSTGRES_USER`: Postgres user  
`POSTGRES_PASSWORD`: Postgres password  
`POSTGRES_DB`: Target DB  
`POSTGRES_HOST`: DB host  
`POSTGRES_PORT`: DB port [default: 5432]  
`WEB_HOST`: example 0.0.0.0 for run in docker [default: localhost]  
`WEB_PORT`: published port for API [default: 8080]  
 

# Endpoints  
- `/` redirect to healthcheck endpoint 
- `/healthcheck` (returns status of running of service with requirements, example database)  
