import json
from flask import request
from flask import jsonify
from werkzeug.exceptions import HTTPException
from flask_app import app
from tasks.Task1 import Task1
import logging

@app.route("/add", methods=['POST'])
def add():
    if request.method == 'POST':
        result=Task1.add.delay(2, 8)
        return json.dumps({'code': 0, 'msg': 'ok', 'data': str(result)})

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    logging.exception('error:{},code:{}'.format(str(e), code))
    return jsonify(error=str(e)), code
