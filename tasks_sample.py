import time
from celery import Celery


# mq broker
broker = 'mongodb://localhost:27017/jobs'

# db result
backend = 'mongodb://localhost:27017/jobs'

# refer to link: https://github.com/celery/celery/blob/a7c74d7d91ebab9b386760df1d4230c27127decc/celery/app/base.py#L145
app = Celery('my_task', broker=broker, backend=backend)

@app.task
def add(x, y):
    print('enter call func...')
    time.sleep(4)
    return x + y
