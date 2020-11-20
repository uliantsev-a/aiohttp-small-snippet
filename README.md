# Micro API 

Example API for microservice by aiohttp 

# Usage
``` bash

pip install -e .
python -m micro_api 
```
# Settings
Optional from settings file or env properties:

`DEBUG`: Debug regime which set log level to debug level
`LOG_LEVEL`: Python logging level [default: INFO]

# Endpoints
- `/v1/healthcheck` (returns status of running of service with requirements, example database)
