# distribution_test_server
简易版分布式测试系统

## 准备环境

- Python 3.6.8 
- Anaconda 3
- MongoDB 4.2.1

## 运行指南
- 启动目标测试服，HttpServer

```
python server.py
```

- 启动flower 监听Celery服务，暴露Restful API

```
celery -A tasks flower
```

- 启动Celery worker，执行测试用例

```
celery -A tasks worker -l info
```

- 运行入口

```
curl -v -H 'Content-Type:application/json' -X 'POST' -d '{"aireplane_id":1}'  http://localhost:5555/api/task/apply/tasks.query_airplane
```
