# coding=utf-8

import os

envs = os.environ

# application configs
MAX_DEPTH = (envs.get('MAX_DEPTH') and int(envs.get('MAX_DEPTH'))) or 16
SEED_URL = envs.get('SEED_URL') or 'http://www.example.com'
TIMEOUT = (envs.get('TIMEOUT') and int(envs.get('TIMEOUT'))) or 60

# database configs
DB_HOST = envs.get('DB_HOST') or '127.0.0.1'
DB_PORT = (envs.get('DB_PORT') and int(envs.get('DB_PORT'))) or 3306
DB_USER = envs.get('DB_USER') or 'root'
DB_PASSWORD = envs.get('DB_PASSWORD') or '123'
DB_DATABASE = envs.get('DB_DATABASE') or 'nautilus'
DB_CHARSET = envs.get('DB_CHARSET') or 'utf8mb4'
