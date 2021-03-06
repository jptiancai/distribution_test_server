from celery_app import app
import subprocess
import os
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def query_airplane():
    ret = subprocess.call(["sh", os.getcwd() + '/test.sh'])
    logger.info(f'call test.sh result: {ret}')
    