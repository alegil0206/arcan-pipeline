from pendulum import datetime, duration

#DEFAULT ARGUMENTS
DEFAULT_OWNER = "Airflow"
DEFAULT_RETRIES = 5
DEFAULT_RETRY_DELAY = duration(minutes=15)
DEFAULT_RETRY_EXPONENTIAL_BACKOFF = True
DEFAULT_MAX_RETRY_DELAY = duration(hours=12)

#MYSQL TASK ARGUMENT
MYSQL_RETRIES = 10
MYSQL_RETRY_DELAY = duration(minutes=15)

#DOCKER TASK ARGUMENT
DOCKER_RETRIES = 2
DOCKER_RETRY_DELAY = duration(minutes=30)

#GIT REST API TASK ARGUMENT
GIT_REST_API_RETRIES = 10
GIT_REST_API_RETRY_DELAY = duration(minutes=15)
GIT_REST_API_MAX_RETRY_DELAY = duration(hours=24)
GIT_REST_API_POOL = 'git_rest_api_pool'

#FILE MANAGER TASK ARGUMENT
FILE_MANAGER_RETRIES = 10
FILE_MANAGER_RETRY_DELAY = duration(minutes=15)