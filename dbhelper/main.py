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
        self.connection = pymysql.connect(**self.config)
        self.cursor = self.connection.cursor()

    def insert_item(self, values):
        sql = '''
            INSERT INTO `data` (`url`, `title`, `content`, `time`)
            VALUES (%s, %s, %s, %s)
        '''
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
        except:
            self.connection.rollback()
        self.connection.close()
