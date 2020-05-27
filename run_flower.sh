#!/usr/bin/env bash
# -*- coding:utf-8 -*-
mkdir -p logs

celery flower -A celery_server -l info >./logs/start_flower.log 2>&1