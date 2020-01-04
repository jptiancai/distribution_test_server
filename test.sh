#!/usr/bin/bash
python test/test_tasks.py
pytest --junit-xml=junit.xml --html=reports/report.html test/test_pytest.py