from celery import Celery


app = Celery('Allen_TASKS')

# 加载后端的设置以存储作业的结果
app.config_from_object('celeryconfig')

if __name__ == "__main__":
    app.start() 