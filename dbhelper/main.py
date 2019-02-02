#!/usr/bin/env python
# coding=utf-8

import pymysql
import configparser

class DBHelper:

    def __init__(self):
        config_file = configparser.ConfigParser()
        config_file.read('config.ini')
        configs = config_file['DATABASE']
        self.config = {
            'host': configs['Host'],
            'port': int(configs['Port']),
            'user': configs['User'],
            'password': configs['Password'],
            'db': configs['Database'],
            'charset': configs['Charset'],
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
