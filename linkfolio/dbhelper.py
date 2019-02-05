#!/usr/bin/env python
# coding=utf-8

import pymysql
import sys
sys.path.append('..')
from utils.config import *

class DBHelper:

    def __init__(self):
        self.config = {
            'host': DB_HOST,
            'port': DB_PORT,
            'user': DB_USER,
            'password': DB_PASSWORD,
            'db': DB_DATABASE,
            'charset': DB_CHARSET,
            'cursorclass': pymysql.cursors.DictCursor
        }

    def insert_item(self, values):
        connection = pymysql.connect(**self.config)
        connection.ping(reconnect = True)
        try:
            with connection.cursor() as cursor:
                sql = '''
                    INSERT INTO `data` (`url`, `title`, `content`, `time`)
                    VALUES (%s, %s, %s, %s)
                '''
                cursor.execute(sql, values)
            connection.commit()
        except:
            pass
        finally:
            connection.close()
