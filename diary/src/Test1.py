#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/19 16:44
# @Author  : niuliangtao
# @Site    : 
# @File    : Test1.py
# @Software: PyCharm

import os
import re

root = '/Users/weidian/workspace/gouye/cs231n.github.io/'


def solve(path):
    print path
    f1 = open(root + path, 'r')
    f2 = open('/Users/weidian/Documents/Diary/_posts/cs231n/2018-02-21-' + path, 'w')

    index = 0
    for data in f1.readlines():

        index = index + 1
        if index == 4:
            data = "categories: posts\n" + data
        data = data.replace('\\\\(', '$')
        data = data.replace('\\\\)', '$')
        if ("/assets/" in data) and re.search("jpg|png|jpeg", data):
            data = data.replace("/assets/", "{{site.baseurl}}{{site.images}}/cs231n/")
        f2.write(data)
    f1.close()
    f2.close()


if __name__ == '__main__':
    for dir in os.listdir(root):

        if dir.endswith('md'):
            print dir
            solve(dir)
