# coding=utf-8

import configparser
import os

envs = os.environ

config = configparser.ConfigParser()
config.read('config.ini')

# application configs
MAX_DEPTH = config['basic']['max_depth'] or 16
SEED_URL = envs.get('SEED_URL') \
           or config['basic']['seed_url'] \
           or 'http://www.example.com'
TIMEOUT = (envs.get('TIMEOUT') and int(envs.get('TIMEOUT'))) \
          or int(config['basic']['timeout']) or 10

# database configs
DB_HOST = envs.get('DB_HOST') \
          or config['database']['host'] \
          or '127.0.0.1'
DB_PORT = (envs.get('DB_PORT') and int(envs.get('DB_PORT'))) \
          or int(config['database']['port']) or 3306
DB_USER = envs.get('DB_USER') \
          or config['database']['user'] or 'root'
DB_PASSWORD = envs.get('DB_PASSWORD') \
              or config['database']['password'] or '123'
DB_DATABASE = envs.get('DB_DATABASE') or \
              config['database']['database'] or 'linkfolio'
DB_CHARSET = envs.get('DB_CHARSET') \
             or config['database']['charset'] or 'utf8mb4'
