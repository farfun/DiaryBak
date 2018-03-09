#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/03/08 22:33
# @Author  : niuliangtao
# @Site    : 
# @File    : GetAll.py
# @Software: PyCharm
import codecs
import os

import yaml

pjoin = os.path.join
_BLOG_ROOT = os.path.abspath(pjoin(os.path.dirname(__file__), os.path.pardir))
_DEFAULT_CATEGORY = 'Home'
root = '/Users/weidian/Documents/Diary/'
yml_path_bak = root+"mkdocs.bak.yml"
yml_path = root+"mkdocs.yml"
doc_path = root+"docs/"


def getPath():
    pages = {}
    home = []
    pages["Home"] = home
    for file_name in os.listdir(doc_path):
        file_path = doc_path + file_name
        if ".md" in file_name:
            home.append(file_name.title())
        elif os.path.isdir(file_path):
            cate = file_name
            cate_list = []
            pages[cate] = cate_list
            for file2 in os.listdir(file_path):
                if ".md" in file2:
                    text = cate + "/" + file2
                    cate_list.append(text)
    return pages


def output_post_save(path):
    print ("output_post_save")

    fr = open(yml_path_bak, "r")
    fw = open(yml_path, "w")

    for line in fr.readlines():
        fw.write(line)
        print line
        if "pages" in line:
            break

    fr.close()

    for key in path:
        line = "- " + key + ": "
        print (type(line))
        print (isinstance(line, str))
        print line

        fw.write(str(line))
    fw.close()
    print (isinstance(path, dict))

    data=[1,2]
    print (isinstance(data, list))

def dict_str(records):
    res = ""
    for record in records:
        res


def output_post_save2():
    print ("\n\noutput_post_save\n\n")

    fp = codecs.open(yml_path_bak, "r", "utf-8")
    document = fp.read()
    fp.close()
    mkdocs = yaml.load_all(document)

    # 遍历迭代器
    for data in mkdocs:
        print(type(data))
        print(data)

        print("---" * 25)
        # 将python对象转换成为yaml格式文档
        output = yaml.dump(data)
        print(type(output))
        print(output.decode("unicode-escape"))

        #pages = []
        #data['pages'] = pages
        pages=data['pages']

        home = []
        pages.append({"Home": home})
        for file_name in os.listdir(doc_path):
            file_path = doc_path + file_name
            if ".md" in file_name:
                home.append(file_name.title())
            elif os.path.isdir(file_path):
                cate = file_name.decode('utf8')
                cate_list = []
                pages.append({cate: cate_list})
                for file2 in os.listdir(file_path):
                    if ".md" in file2:
                        cate_list.append(cate+"/"+file2.decode('utf8'))
        print data
        "dfasdfa".replace(" ","")
        with codecs.open(yml_path, 'w', "utf-8") as config:
            print(type(data))
            yaml_text = yaml.dump(data).decode("unicode-escape").replace(" ","").replace("\"","")
            print(yaml_text)
            config.write(yaml_text)


if __name__ == '__main__':
    path = getPath()
    print path
    output_post_save(path)
    #output_post_save2()
