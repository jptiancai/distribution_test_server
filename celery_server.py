from celery import Celery
import os
import tasks

# 指定要连接到的 mongodb 主机和数据库
BROKER_URL = 'mongodb://localhost:27017/jobs'

app = Celery('Allen_TASKS',broker=BROKER_URL)

# 加载后端的设置以存储作业的结果
app.config_from_object('celeryconfig')

if __name__ == "__main__":
    app.start() 