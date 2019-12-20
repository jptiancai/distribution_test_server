from celery_server import app
from test.test_tasks import test_query_airplane
import subprocess
import os
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def query_airplane():
    ret = subprocess.call(["/bin/bash", os.getcwd() + '/test.sh'])
    logger.info(f'call test.sh result: {ret}')
    # 此方式不建议
    # os.system('nosetests')
    