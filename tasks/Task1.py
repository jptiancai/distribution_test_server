from flask_app import celery_app
import time

class Task1(object):

    @staticmethod
    @celery_app.task(name="tasks.Task1.add")
    def add(x, y):
        time.sleep(4)
        return x + y