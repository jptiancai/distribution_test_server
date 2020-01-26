import pytest
import csv
import os
import requests
import json
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to

'''
command 1: pytest test/test_pytest.py
command 2: pytest --junit-xml=reports/junit.xml test/test_pytest.py
command 3: 
    pytest --junit-xml=junit.xml --html=reports/report.html test/test_pytest.py
    dependes: conftest.py
'''


def test_data():
    assert_that(1, equal_to(2))


@pytest.mark.parametrize("actual, expect",[
    (1, 2),
    (2, 1),
    ("aaa", "bbb"),
    ("aaa", "aaa")
])
def test_parameter_1(actual, expect):
    assert_that(actual, equal_to(expect))


def read_values_from_excel():
    with open(os.getcwd() + '/test/file.csv', 'r') as f:
        reader = csv.reader(f, delimiter="	")
        next(reader, None)  # skip the headers
        values = list(map(tuple, reader)) # [(),(),()......]
    print(values)
    return values

values = read_values_from_excel()

@pytest.mark.parametrize(("id, is_exec, test_case, req_type,req_host, \
                req_interface, req_data, exp_result"),
                values)
def test_http_req(id, is_exec, test_case, req_type,req_host,
             req_interface, req_data, exp_result):
    act_result = ''
    req_url = req_host + req_interface

    print('用例编号：' + id)
    print('请求接口：' + req_url)
    print('请求参数：' + req_data)
    print('接口预期值：' + exp_result)

    if "YES" == is_exec:
        if "GET" == req_type:
            act_result = requests.get(req_url, data = req_data).text
        else:
            r = requests.post(req_url, json = json.loads(req_data))
            act_result = json.dumps(r.json())

    print('接口实际值：' + str(act_result))

    assert_that(act_result, equal_to(exp_result))




