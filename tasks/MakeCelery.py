from __future__ import absolute_import
from celery import Celery

        
def make_celery(app, include):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'], include=include)
 
    celery.conf.update(app.config)
    TaskBase = celery.Task
    
    class ContextTask(TaskBase):
        abstract = True
        
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    
    celery.Task = ContextTask
    return celery
