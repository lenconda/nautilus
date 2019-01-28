#!/usr/bin/env python
# coding=utf-8

from linkfolio.main import LinkFolio
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    app = LinkFolio(config['BASIC']['URL'],
                    config['BASIC']['MaxDepth'])
    app.run()
