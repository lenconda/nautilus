#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import re

def check_if_url(url):
    url_test_regexp = r'^((https|http|ftp|rtsp|mms)?://)' \
                      r'?(([0-9a-z_!~*"().&=+$%-]+: )' \
                      r'?[0-9a-z_!~*"().&=+$%-]+@)?(([0-9]{1,3}\.){3}[0-9]{1,3}|' \
                      r'([0-9a-z_!~*"()-]+\.)' \
                      r'*([0-9a-z][0-9a-z-]{0,61})?[0-9a-z]\.[a-z]{2,6})' \
                      r'(:[0-9]{1,4})?((/?)|' \
                      r'(/[0-9a-z_!~*"().;?:@&=+$,%#-]+)+/?)$'
    url_test = re.compile(url_test_regexp)
    return url_test.match(url)

is_url = check_if_url('https://www.baidu.com')
print(is_url)

# if __name__ == '__main__':