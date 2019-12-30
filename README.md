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
docker build -t http_server:http_server .
docker run -d -v /tmp/http_logs:/data/app/http_server/logs -p 5001:5001 http_server:http_server
```

- 启动flower 监听Celery服务，暴露Restful API

```
celery -A tasks flower
docker build -f Dockerfile_flower -t distribution_test_server:flower .
docker run -d -v /tmp/distribution_test_server_logs:/data/app/distribution_test_server/logs -p 5555:5555 distribution_test_server:flower
```

- 启动Celery worker，执行测试用例

```
celery -A tasks worker -l info
docker build -f Dockerfile_worker -t distribution_test_server:worker .
docker run -d -v /tmp/distribution_test_server_logs:/data/app/distribution_test_server/logs distribution_test_server:worker
```

- docker mongo

```
docker pull mongo:4.2.1
```

- docker compose

```
docker-compose build
docker-compose --verbose up
```

- 查看容器中的docker内容

```

mongo --host 127.0.0.1 --port 27018

```

- 查看docker 运行情况

```
# 当前运行
docker ps
# 所有运行过的列表
docker ps -a | more
```



- 运行入口

```
curl -v -H 'Content-Type:application/json' -X 'POST' -d '{"aireplane_id":1}'  http://localhost:5555/api/task/apply/tasks.query_airplane
```

- 输出测试报告HTML

    位于reports/*.html

    ![](/reports/img/TestResults___main__.TestMethods_2019-12-21_23-02-09.png)

## To-Do List
- [x] 第一版 v0.0.1
  - 核心框架搭建，可支持分布式
- [x] 第二版 v0.0.2
  - 输出html报告形式
- [x] 第三版 v0.0.3
  - [x] 目标测试服，docker化，[跳转链接：http_server](https://github.com/jptiancai/http_server)
- [x] 第四版 v0.0.4
  - [x] celery worker，执行测试用例服务，docker化
  - [x] celery flower 监听服务，docker化
- [x] 第四版 v0.0.5
  - [x] docker compose 
- [ ] 第五版 v0.0.6
  - [ ] 读取excel测试用例
- [ ] 第六版 v0.0.7
  - [ ] 任务发布者cURL方式，修改成界面调用


## celery source code

- [Source code for celery.platforms](https://docs.celeryproject.org/en/3.1/_modules/celery/platforms.html)
> run celery as root, you will receive warning msg.Above that is the source code, enjoy it!
