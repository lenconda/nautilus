#!/usr/bin/env python
# coding=utf-8

from linkfolio.linkfolio import LinkFolio
from utils.config import SEED_URL, MAX_DEPTH

if __name__ == '__main__':
    app = LinkFolio(url = SEED_URL, max_depth = MAX_DEPTH)
    app.run()
