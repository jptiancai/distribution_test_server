
from datetime import timedelta
from celery.schedules import crontab

# Example configuration
# https://docs.celeryproject.org/en/3.1/configuration.html#example-configuration-file


# Broker settings
# https://docs.celeryproject.org/en/3.1/configuration.html#broker-url

BROKER_URL = 'mongodb://localhost:27017/jobs'


# MongoDB backend settings
# https://docs.celeryproject.org/en/3.1/configuration.html#conf-mongodb-result-backend
# requires pymongo library

CELERY_RESULT_BACKEND = 'mongodb://localhost:27017'
CELERY_MONGODB_BACKEND_SETTINGS = {
    'host': '127.0.0.1',
    'port': 27017,
    'database': 'jobs', 
    'taskmeta_collection': 'celery_tasks',
}


# Time zone
# https://docs.celeryproject.org/en/3.1/configuration.html#celery-timezone

CELERY_TIMEZONE = 'Asia/Shanghai'

# Woker settings
# https://docs.celeryproject.org/en/3.1/configuration.html#celery-imports
# List of modules to import when celery starts.
CELERY_IMPORTS = {
    'celery_app.task1',
    'celery_app.task2'
}

CELERYBEAT_SCHEDULE = {
    # Execute every 10 sencond
    'add-every-10-second': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 8)
    },
    # Execute daily at specific time
    'multiply-at-specific-time': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=21, minute=36),
        'args': (4, 6)
    },
}
