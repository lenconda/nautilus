#!/usr/bin/env python
# coding=utf-8

from utils import queue, urls
from bs4 import BeautifulSoup
from urllib import request, error, parse
from dbhelper.main import DBHelper
import time

class LinkFolio:

    def __init__(self, url, max_depth):
        self.visited_queue = queue.Queue
        self.unvisited_queue = queue.Queue
        self.url = url
        self.max_depth = max_depth
        self.db = DBHelper

    def soup_generate(self, url):
        try:
            html_response = request.urlopen(url)
        except (error.HTTPError,
                error.URLError) as err:
            print(err)
        else:
            if html_response is None:
                print('URL is not correct...')
            else:
                soup = BeautifulSoup(html_response.read())
                return soup

    def get_all_links(self, link):
        soup = self.soup_generate(link)
        links = []
        for link in soup.find_all('a', { 'href': True }):
            links.append(link)
        return links

    def get_inner_links(self, all_links):
        inner_links = []
        for link in all_links:
            if parse.urlparse(link).hostname:
                inner_links.append(
                    urls.Urls(link).prefix_url(self.url))
            else:
                if urls.Urls(link).inner_url(self.url):
                    inner_links.append(link)
        return inner_links

    def get_link_page_content(self, link):
        soup = self.soup_generate(link)
        content = soup.body.get_text()
        return content

    def get_link_page_title(self, link):
        soup = self.soup_generate(link)
        title = soup.title.get_text()
        return title

    def fetch(self):
        url = self.unvisited_queue.dequeue()
        print('[+] Get URL: ' + url)
        if urls.Urls(url).check_if_url():
            self.visited_queue.enqueue(url)
            all_links = self.get_all_links(url)
            inner_links = self.get_inner_links(all_links)
            for link in inner_links:
                if self.visited_queue.has(link) \
                        and self.unvisited_queue.has(link):
                    content = self.get_link_page_content(link)[0: 100]
                    title = self.get_link_page_title(link)
                    timestamp = int(round(time.time()) * 1000)
                    values = (link, title, content, timestamp)
                    self.db.insert_item(values)
                    self.unvisited_queue.enqueue(link)
        else:
            print('URL is illegal...')
        if (self.unvisited_queue):
            self.fetch()

    def run(self):
        self.unvisited_queue.enqueue(self.url)
        self.fetch()