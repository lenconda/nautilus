#!/usr/bin/env python
# coding=utf-8

class Queue:

    def __init__(self):
        self.queue = []

    def get(self):
        return self.queue

    def enqueue(self, url):
        return self.queue.append(url)

    def dequeue(self):
        elem = self.queue[0]
        self.queue.reverse()
        self.queue.pop()
        self.queue.reverse()
        return elem

    def has(self, item):
        return item in self.queue