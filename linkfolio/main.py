#!/usr/bin/env python
# coding=utf-8

from utils.urls import Urls
from utils.queue import Queue
from bs4 import BeautifulSoup
from dbhelper.main import DBHelper
import time
import requests
from utils.logger import get_logger

class LinkFolio:

    def __init__(self, url, max_depth):
        self.seed_url = url
        self.result_urls = []
        self.queue = Queue()
        self.max_depth = int(max_depth)
        self.cur_depth = 1
        self.db = DBHelper()
        self.logger = get_logger(__name__)

    def bfs_traverse(self):
        self.queue.enqueue(self.seed_url)
        while len(self.queue.get()) != 0 and self.cur_depth < 6:
            for i in range(0, len(self.queue.get())):
                current_url = self.queue.dequeue()
                time.sleep(1)
                html_response = requests.get(current_url).text
                soup = BeautifulSoup(html_response, 'html.parser')
                links = soup.find_all('a', { 'href': True })

                for item in links:
                    link = item.get('href')
                    url_resolver = Urls(link)
                    if url_resolver.check_if_url() \
                        and url_resolver.inner_url(self.seed_url):
                        prefixed_url = url_resolver.prefix_url(self.seed_url, link)
                        if prefixed_url not in self.result_urls:
                            response_text = requests.get(prefixed_url).text
                            response_parse = BeautifulSoup(response_text, 'html.parser')
                            title = response_parse.title.get_text().strip()
                            [s.extract() for s in response_parse('script')]
                            [s.extract() for s in response_parse('style')]
                            content = response_parse.body.get_text().replace(' ', '')[0: 4096]
                            timestamp = str(int(round(time.time()) * 1000))
                            values = (prefixed_url, title, content, timestamp)
                            self.db.insert_item(values)
                            self.result_urls.append(prefixed_url)
                            self.queue.enqueue(prefixed_url)
                            self.logger.info('GET URL: ' + prefixed_url)
            self.cur_depth += 1
