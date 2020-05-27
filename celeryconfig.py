
BROKER_URL = 'mongodb://broker:27017/jobs'

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "broker",
    "port": 27017,
    "database": "jobs", 
    "taskmeta_collection": "pytest_tasks",
}

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_POOL_RESTARTS = True

CELERY_IMPORTS = {
    'task_query_airplane'
}
