# coding=utf-8

import configparser
import os

envs = os.environ

config = configparser.ConfigParser()
config.read('config.ini')

# application configs
MAX_DEPTH = config['BASIC']['MaxDepth'] or 16
SEED_URL = envs.get('LINKFOLIO_SEED_URL') \
           or config['BASIC']['SeedUrl'] \
           or 'http://www.example.com'

# database configs
DB_HOST = config['DATABASE']['Host'] or '127.0.0.1'
DB_PORT = int(config['DATABASE']['Port']) or 3306
DB_USER = config['DATABASE']['User'] or 'root'
DB_PASSWORD = config['DATABASE']['Password'] or '123'
DB_DATABASE = config['DATABASE']['Database'] or 'linkfolio'
DB_CHARSET = config['DATABASE']['Charset'] or 'utf8mb4'
