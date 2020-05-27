from celery_app import task1
from celery_app import task2

#task1.add.delay(2, 8)
task1.add.apply_async(args=(2, 8), queue='work_queue')
#task2.multiply.delay(4, 6)

print('end......')
