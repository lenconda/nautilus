#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.parse import urlparse
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
    if url_test.match(url):
        return True
    else:
        return False

def inner_url(current_url, site_url):
    current_host = urlparse(current_url).hostname
    site_host = urlparse(site_url).hostname
    if current_host:
        if current_host == site_host:
            return True
        else:
            return False
    return True

def prefix_url(current_url, site_url_prefix):
    current_url_parse = urlparse(current_url)
    if current_url_parse.hostname == None \
            and current_url_parse.path[0] == '/':
        return site_url_prefix + current_url_parse.path
    else:
        return site_url_prefix + '/' + current_url_parse.path


if __name__ == '__main__':
    print(check_if_url('path/to/file.html'))