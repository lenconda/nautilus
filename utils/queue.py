#!/usr/bin/env python
# coding=utf-8

class Queue:

    def __init__(self):
        self.queue = []

    def get(self):
        return self.queue

    def enqueue(self, url):
        return self.visited.append(url)

    def dequeue(self):
        self.visited.reverse()
        self.visited.pop()
        self.visited.reverse()
        return self.visited
