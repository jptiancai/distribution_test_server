
from datetime import timedelta
from celery.schedules import crontab

conf = {
    "default": {
        "CELERY_BROKER_URL": "mongodb://localhost:27017/jobs",
        "CELERY_RESULT_BACKEND": "mongodb://localhost:27017",
        "CELERY_MONGODB_BACKEND_SETTINGS": {
            'host': '127.0.0.1',
            'port': 27017,
            'database': 'jobs',
            'taskmeta_collection': 'flask_tasks'},
        "CELERYD_CONCURRENCY": 4,
        "CELERY_DEFAULT_QUEUE": "work_queue",
        "CELERY_TIMEZONE": 'Asia/Shanghai',
        "CELERY_QUEUES": {
            'beat_tasks': {
                'exchange': 'beat_tasks',
                'exchange_type': 'direct',
                'binding_key': 'beat_tasks',
            },
            'work_queue': {
                'exchange': 'work_queue',
                'exchange_type': 'direct',
                'binding_key': 'work_queue',
            }
        },
        "CELERYBEAT_SCHEDULE": {
            # Execute every 10 sencond
            'add-every-10-second': {
                'task': 'tasks.Task1.add',
                'schedule': timedelta(seconds=10),
                'args': (8, 8),
                'options': {
                    'queue': 'beat_tasks'
                }
            }
        }
    }
}
