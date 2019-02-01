#!/usr/bin/env python
# coding=utf-8

from urllib.parse import urlparse
from url_normalize import url_normalize
from urlobject import URLObject
import re

class Urls:

    def __init__(self, url):
        self.current_url = url

    def check_if_url(self):
        url_test_regexp = r'^((https|http|ftp|rtsp|mms)?://)' \
                          r'?(([0-9a-z_!~*"().&=+$%-]+: )' \
                          r'?[0-9a-z_!~*"().&=+$%-]+@)?(([0-9]{1,3}\.){3}[0-9]{1,3}|' \
                          r'([0-9a-z_!~*"()-]+\.)' \
                          r'*([0-9a-z][0-9a-z-]{0,61})?[0-9a-z]\.[a-z]{2,6})' \
                          r'(:[0-9]{1,4})?((/?)|' \
                          r'(/[0-9a-z_!~*"().;?:@&=+$,%#-]+)+/?)$'
        url_test = re.compile(url_test_regexp)
        if url_test.match(self.current_url):
            return True
        else:
            return False

    def inner_url(self, site_url):
        current_host = urlparse(url_normalize(self.current_url)).netloc
        site_host = urlparse(url_normalize(site_url)).netloc
        if current_host != '':
            if current_host == site_host:
                return True
            else:
                return False
        else:
            return True

    def prefix_url(self, site_url, parent_url):
        current_url_parse = URLObject(self.current_url)
        parent_url_parse = URLObject(url_normalize(parent_url + '/'))
        if current_url_parse.netloc == '':
            new_url = URLObject(site_url)\
                .with_path(parent_url_parse.path)\
                .relative(current_url_parse.path)
            return url_normalize(new_url)
        else:
            return url_normalize(self.current_url)
