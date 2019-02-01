#!/usr/bin/env python
# coding=utf-8

class Queue:

    def __init__(self):
        self.items = []

    def get(self):
        return self.items

    def enqueue(self, url):
        self.items.append(url)
        return url

    def dequeue(self):
        self.items.reverse()
        elem = self.items.pop()
        self.items.reverse()
        return elem

    def has(self, item):
        return item in self.items

    def empty(self):
        return len(self.items) == 0
