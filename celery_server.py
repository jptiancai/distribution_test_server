from celery import Celery
import os
import tasks

# 指定要连接到的 mongodb 主机和数据库
mongo_host = '127.0.0.1'
try:
    docker_flag = os.environ.get('DOCKER', "")
    if docker_flag == '1':
        mongo_host = 'broker'
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

BROKER_URL = 'mongodb://{}:27017/jobs'.format(mongo_host)

app = Celery('Allen_TASKS',broker=BROKER_URL)

# 加载后端的设置以存储作业的结果
app.config_from_object('celeryconfig')

if __name__ == "__main__":
    app.start() 