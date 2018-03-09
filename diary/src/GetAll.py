#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/03/08 22:33
# @Author  : niuliangtao
# @Site    : 
# @File    : GetAll.py
# @Software: PyCharm
import io
import os

import yaml

pjoin = os.path.join
_BLOG_ROOT = os.path.abspath(pjoin(os.path.dirname(__file__), os.path.pardir))
_DEFAULT_CATEGORY = 'Home'
root = '/Users/weidian/Documents/Diary/'
yml_path_bak = root + "mkdocs.bak.yml"
yml_path = root + "mkdocs.yml"
doc_path = root + "docs/"


def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def encode(check_str):
    if check_contain_chinese(check_str):
        return unicode(check_str, "utf-8")
    else:
        return check_str


def output_post_save2():
    print ("\n\noutput_post_save\n\n")
    with io.open(yml_path_bak, "r", encoding="utf-8") as docs:
        data = yaml.safe_load(docs)

    pages = data['pages']

    home = []
    pages.append({"Home": home})
    for file_name in os.listdir(doc_path):
        file_path = doc_path + file_name
        if ".md" in file_name:
            home.append(encode(file_name))
        elif os.path.isdir(file_path):
            cate = encode(file_name)
            cate_list = []
            pages.append({cate: cate_list})
            for file2 in os.listdir(file_path):
                if ".md" in file2:
                    cate_list.append(cate + "/" + encode(file2))

    with io.open(yml_path, 'w+', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)


def test():
    # 开档
    data = []
    with io.open("data1.yml", "r", encoding="utf-8") as docs:
        try:
            data = yaml.safe_load(docs)
        except yaml.YAMLError as exc:
            print(exc)
    data[unicode("人生苦短", "utf-8")] = {"山大": "发的是"}
    # 写档
    with io.open('data2.yml', 'w+', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)


if __name__ == '__main__':
    output_post_save2()
