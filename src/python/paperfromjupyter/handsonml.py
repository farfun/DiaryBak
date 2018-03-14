#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/03/13 19:43
# @Author  : niuliangtao
# @Site    : 
# @File    : handsonml.py
# @Software: PyCharm

import subprocess

if __name__ == '__main__':
    subprocess.check_output("pwd", shell=True)

    print ("\n\n")
    # subprocess.check_output("cp {} {}".format("a", "b"), shell=True)
