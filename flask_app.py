from flask import Flask
from tasks.MakeCelery import make_celery
from tasks.CeleryConf import conf

celery_conf = conf["default"]

app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL=celery_conf['CELERY_BROKER_URL'],
    CELERY_RESULT_BACKEND=celery_conf['CELERY_RESULT_BACKEND'],
    CELERY_MONGODB_BACKEND_SETTINGS=celery_conf['CELERY_MONGODB_BACKEND_SETTINGS'],
    CELERYD_CONCURRENCY=celery_conf['CELERYD_CONCURRENCY'],
    CELERY_DEFAULT_QUEUE=celery_conf['CELERY_DEFAULT_QUEUE'],
    CELERY_TIMEZONE=celery_conf['CELERY_TIMEZONE'],
    CELERY_QUEUES=celery_conf['CELERY_QUEUES'],
    CELERYBEAT_SCHEDULE=celery_conf['CELERYBEAT_SCHEDULE']
)

app.logger.info('start the app....')

celery_app = make_celery(app, ['tasks.Task1'])
