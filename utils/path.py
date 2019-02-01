#!/usr/bin/env python
# coding=utf-8

import os

def project_path():
    abs_path = os.path.join(__file__, '../../')
    project_path = os.path.abspath(abs_path)
    return project_path
