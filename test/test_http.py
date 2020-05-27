import pytest
import csv
import os
import requests
import json
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to

'''
command 1: pytest test/test_http.py
command 2: 
    pytest --html=reports/report.html test/test_http.py
    
    dependes: conftest.py
'''

def read_values_from_excel():
    with open(os.getcwd() + '/test/file.csv', 'r') as f:
        reader = csv.reader(f, delimiter="	") # csv delimiter replace default comma
        next(reader, None)  # skip the headers
        values = list(map(tuple, reader)) # [(),(),()......]
    need_exec_list = list()
    for v in values:
        if "YES" in v:
            need_exec_list.append(v)
    print(need_exec_list)
    return need_exec_list

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

    if "GET" == req_type:
        act_result = requests.get(req_url, data = req_data).text
    else:
        r = requests.post(req_url, json = json.loads(req_data))
        act_result = json.dumps(r.json())

    print('接口实际值：' + str(act_result))

    assert_that(act_result, equal_to(exp_result))

if __name__ == "__main__":
    pass
    