from celery import Celery


app = Celery('Allen_TASKS')

app.config_from_object('celeryconfig')