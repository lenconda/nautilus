#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
import time
import requests
from utils.urls import Urls
from utils.queue import Queue
from utils.logger import get_logger
from utils.config import TIMEOUT
from .dbhelper import DBHelper
import re
from urllib.parse import unquote

class Nautilus:

    def __init__(self, url, max_depth):
        self.seed_url = url
        self.result_urls = []
        self.queue = Queue()
        self.max_depth = int(max_depth)
        self.cur_depth = 1
        self.db = DBHelper()
        self.logger = get_logger(__name__)

    def is_file_link(self, url):
        file_url_test = re.compile(r'^.*?\.(pdf|docx|doc|rtf|mobi|azw3|epub)$')
        if file_url_test.match(url.lower()):
            return True
        else:
            return False

    def insert_links(self, file_url, parent_url):
        with requests.get(parent_url, timeout = TIMEOUT) as html_response:
            response_parse = BeautifulSoup(html_response.text, 'html.parser')
            filename = unquote(file_url).split('/').pop()
            [s.extract() for s in response_parse('script')]
            [s.extract() for s in response_parse('style')]
            content = response_parse.body.get_text() \
                .replace(' ', '') \
                .replace('\n', '') \
                .replace('\r', '')
            timestamp = str(int(round(time.time()) * 1000))
            values = (file_url, filename, content, timestamp)
            self.db.insert_item(values)
            self.logger.info('GET: ' + filename + ' AT ' + file_url)

    def resolve_links(self, item, parent_url):
        link = item.get('href')
        url_resolver = Urls(link)
        if url_resolver.check_if_url() \
                and url_resolver.inner_url(self.seed_url):
            prefixed_url = url_resolver.prefix_url(self.seed_url, link)
            if prefixed_url not in self.result_urls:
                if self.is_file_link(prefixed_url):
                    self.insert_links(prefixed_url, parent_url)
                else:
                    self.result_urls.append(prefixed_url)
                    self.queue.enqueue(prefixed_url)
                    self.logger.info('FETCH: ' + prefixed_url)

    def get_url(self):
        for i in range(0, len(self.queue.get())):
            current_url = self.queue.dequeue()
            time.sleep(1.5)
            with requests.get(current_url, timeout = TIMEOUT) as html_response:
                soup = BeautifulSoup(html_response.text, 'html.parser')
                links = soup.find_all('a', {'href': True})
                for item in links:
                    time.sleep(1.5)
                    self.resolve_links(item, current_url)

    def bfs_traverse(self):
        self.queue.enqueue(self.seed_url)
        while self.cur_depth < self.max_depth:
            try:
                self.get_url()
                self.cur_depth += 1
            except Exception as e:
                self.logger.error(str(e))
                pass

    def run(self):
        self.logger.info('START BFS FROM: ' + self.seed_url)
        time.sleep(1)
        self.bfs_traverse()
