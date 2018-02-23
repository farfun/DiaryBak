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


def solve_title(data, index):
    if "layout: page" in data:
        data = "layout: page\n"

    if "permalink" in data:
        data = data.replace("permalink", "title")
        data = data.replace("/", "")
    # 添加类目
    if index == 2:
        data = "categories: posts/cs231n-ch\nmath: y\n" + data

    return data


def solve_context(data):
    # 公式
    data = data.replace('\\\\(', '$')
    data = data.replace('\\\\)', '$')
    if ("/assets/" in data) and re.search("(jpg|png|jpeg|gif)", data):
        data = data.replace("/assets/", "/Diary/assets/images/cs231n/")
    return data


def solve(path):
    print path
    f1 = open(root + path, 'r')
    # f2 = open('/Users/weidian/Documents/Diary/_posts/cs231n/2018-02-21-' + path, 'w')
    f2 = open('/Users/weidian/Documents/Diary/_posts/cs231n-ch/2018-02-21-ch-' + path, 'w')

    index = 0
    index2 = 0
    for data in f1.readlines():
        if "---" in data:
            index2 = index2 + 1

        if index2 < 2:
            index = index + 1
            data = data
            data = solve_title(data, index)
        else:
            data = data
            data = solve_context(data)

        f2.write(data)
    f1.close()
    f2.close()


if __name__ == '__main__':
    for dir in os.listdir(root):

        if dir.endswith('md'):
            print dir
            solve(dir)

    data = "aaa233233bbb"
    data2 = "(23|333)"

    if re.search(data2, data):
        print 1
    else:
        print 0
