#!/usr/bin/env bash
# -*- coding:utf-8 -*-
mkdir -p logs

celery -A tasks worker -l info >./logs/start_worker.log 2>&1