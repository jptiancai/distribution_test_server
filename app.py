# import time
# from tasks_sample import add


# def add(x, y):
#     print('enter call func...')
#     time.sleep(4)
#     return x + y

# if __name__ == "__main__":
    
#     print('start task...')
#     result = add.delay(2, 8)
#     print('end task...')
#     print('result...' + str(result))

from celery_app import task1
from celery_app import task2

task1.add.delay(2, 8)
task2.multiply.delay(2, 8)

print("end...")

