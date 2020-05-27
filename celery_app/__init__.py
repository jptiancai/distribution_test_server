from celery import Celery

app = Celery('config_celery')

app.config_from_object('celery_app.celeryconfig')