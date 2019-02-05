# coding=utf-8

import configparser
import os

envs = os.environ

config = configparser.ConfigParser()
config.read('config.ini')

# application configs
MAX_DEPTH = config['application']['max_depth'] or 16
SEED_URL = envs.get('LINKFOLIO_SEED_URL') \
           or config['application']['seed_url'] \
           or 'http://www.example.com'

# database configs
DB_HOST = config['database']['host'] or '127.0.0.1'
DB_PORT = int(config['database']['port']) or 3306
DB_USER = config['database']['user'] or 'root'
DB_PASSWORD = config['database']['password'] or '123'
DB_DATABASE = config['database']['database'] or 'linkfolio'
DB_CHARSET = config['database']['charset'] or 'utf8mb4'
