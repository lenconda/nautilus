#!/usr/bin/env python
# coding=utf-8

import logging
import time
import os
from sys import stdout
from .path import project_path

def get_logger(name):
    file_path = project_path() +'/logs/log-' + time.strftime('%Y-%m-%d', time.localtime()) + '.log'
    if not os.path.exists(file_path):
        if not os.path.isdir(project_path() + '/logs'):
            os.mkdir('logs')
        touch_file = open(file_path, 'w')
        touch_file.close()
    logger = logging.getLogger(name)
    logger.setLevel(level = logging.INFO)
    stream_handler = logging.StreamHandler(stdout)
    stream_formatter = logging.Formatter(fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt = '%Y/%m/%d %H:%M:%S')
    stream_handler.setFormatter(stream_formatter)
    file_handler = logging.FileHandler(file_path)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger
