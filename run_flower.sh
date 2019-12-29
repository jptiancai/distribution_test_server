#!/usr/bin/env bash
# -*- coding:utf-8 -*-
mkdir -p logs

celery -A tasks flower -l info >./logs/start_flower.log 2>&1