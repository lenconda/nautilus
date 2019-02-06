#!/usr/bin/env python
# coding=utf-8

from nautilus.nautilus import Nautilus as App
from utils.config import SEED_URL, MAX_DEPTH
from utils.logger import get_logger

if __name__ == '__main__':
    logger = get_logger('main')
    try:
        app = App(url = SEED_URL, max_depth = MAX_DEPTH)
        app.run()
    except KeyboardInterrupt as e:
        logger.info('Exit after KeyboardInterrupt...')
        exit(0)
