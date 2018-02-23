#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/23 11:38
# @Author  : niuliangtao
# @Site    : 
# @File    : MoveFileFromQuiver.py
# @Software: PyCharm
import os
import shutil
import time

root = "/Users/weidian/Documents/Diary/"

temp_path = root + "_posts/temp/"
post_path = root + "_posts/"
image_path = root + "assets/images/"


def move_md_file(from_path, to_path, dir_path):
    fr = open(from_path, 'r')
    fw = open(to_path, 'w')

    for data in fr.readlines():
        if "](resources/" in data:
            data = data.replace("resources", "{{ site.baseurl }}{{ site.images }}/" + dir_path)
        fw.write(data)
    fr.close()
    fw.close()
    os.remove(from_path)


# 移动图片
def move_image(from_path, to_path):
    if not os.path.exists(to_path):
        os.mkdir(to_path)
    print "移动图片文件夹" + from_path + "\t" + to_path
    for dir_path in os.listdir(from_path):
        shutil.move(from_path + "/" + dir_path, to_path + "/" + dir_path)
    shutil.rmtree(from_path)


def solver(dir_path):
    print "*****************************************"
    print "移动文件夹" + dir_path
    tag_path = post_path + dir_path
    if not os.path.exists(tag_path):
        os.mkdir(tag_path)

    for file_path in os.listdir(temp_path + dir_path):

        if file_path == "resources":
            from_path = temp_path + dir_path + "/" + file_path
            to_path = image_path + dir_path
            move_image(from_path, to_path)
        elif ".md" in file_path:

            print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            from_path = temp_path + dir_path + "/" + file_path
            to_path = tag_path + "/" + time.strftime("%Y-%m-%d-", time.localtime()) + file_path
            move_md_file(from_path, to_path, dir_path)

    shutil.rmtree(temp_path + dir_path)


if __name__ == '__main__':
    print "start"

    for dir_path in os.listdir(temp_path):
        if os.path.isdir(temp_path + dir_path):
            print (dir_path + " is dir")
            solver(dir_path)

    print "end"
