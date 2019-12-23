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

- 输出测试报告HTML

    位于reports/*.html

    ![](/reports/img/TestResults___main__.TestMethods_2019-12-21_23-02-09.png)

## To-Do List
- [x] 第一版 v0.0.1
  - 核心框架搭建，可支持分布式
- [x] 第二版 v0.0.2
  - 输出html报告形式
- [ ] 第三版 v0.0.3
  - [x] 目标测试服，docker化，[跳转链接：http_server](https://github.com/jptiancai/http_server)
  - [ ] celery worker，执行测试用例服务，docker化
  - [ ] celery flower 监听服务，docker化

- [ ] 第四版 v0.0.4
  - [ ] 任务发布者cURL方式，修改成界面调用
