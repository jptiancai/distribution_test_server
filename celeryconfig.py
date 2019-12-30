from celery.schedules import crontab

BROKER_URL = 'mongodb://broker:27017/jobs'

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "broker",
    "port": 27017,
    "database": "jobs", 
    "taskmeta_collection": "stock_taskmeta_collection",
}

#Celery 定时任务设置
CELERYBEAT_SCHEDULE = {
    'every-minute': {
        'task': 'tasks.query_airplane',
        'schedule': crontab(minute='*/1')
        #'args': (1,2),
    },
}
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_IGNORE_RESULT = False
