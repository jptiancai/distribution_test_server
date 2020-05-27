import pytest
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to

'''
command 1: pytest test/test_pytest.py
command 2: 
    pytest --html=reports/report.html test/test_pytest.py

    dependes: conftest.py
'''

def test_sample():
    assert 1 == 2

def test_data():
    assert_that(1, equal_to(2))


@pytest.mark.parametrize(
    "actual, expect",
    [(1, 1),
    (2, 1),
    ("aaa", "bbb"),
    ("aaa", "aaa")])
def test_parameter(actual, expect):
    assert_that(actual, equal_to(expect))