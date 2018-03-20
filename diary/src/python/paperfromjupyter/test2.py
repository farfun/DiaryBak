#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/03/13 20:10
# @Author  : niuliangtao
# @Site    : 
# @File    : test2.py
# @Software: PyCharm
import datetime
import io
import re
import shutil

DIR_ROOT = "/Users/weidian/Documents/Diary/"


# Move the images under "/ipynb/<fname>_files" to "/assets/ipynb-images"
def move_image(from_dir, to_dir):
    print ("##################")
    print (from_dir + "\t" + to_dir)
    print ("##################")
    if not os.path.exists(from_dir):
        print "输入路径不存在"
        return
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)

    #
    for file_name in os.listdir(from_dir):
        from_file = os.path.join(from_dir, file_name)
        to_file = os.path.join(to_dir, file_name)
        # If it exists, then delete it and then conduct the movement
        if os.path.isfile(to_file):
            os.remove(to_file)
        shutil.move(from_file, to_file)

    shutil.rmtree(from_dir)


# Convert HTML table to markdown table
def transfertable(tablehtml):
    tablehtml = re.compile(r'<table>').sub('', tablehtml)
    tablehtml = re.compile(r'</tbody>[\n]</table>').sub('', tablehtml)

    # Table head
    tablehtml = re.compile(r'<tr><th>').sub(r'#', tablehtml)
    tablehead = re.compile(r'<thead>[\S\s]*?</thead>').findall(tablehtml)
    if tablehead:
        tablehead = tablehead[0]
        # Headline
        col_num = len(re.compile(r'</th>').findall(tablehead))
        tablehtml = re.compile(r'<tbody>').sub('|' + ' --- |' * col_num, tablehtml)

        headcontent = re.compile(r'(?<=>)[\S]*?(?=</th>)').findall(tablehead)
        newhead = '| ' + ' | '.join(headcontent) + ' |'
        tablehtml = re.compile(tablehead).sub(newhead, tablehtml)

    # First column
    firstcol = re.compile(r'(?<=\s)<tr>[\S\s]*?<td>').findall(tablehtml)
    for cell in firstcol:
        origincell = cell
        cell = re.compile(r'<tr><th[^>]*?>').sub('| **', cell)
        cell = re.compile(r'</th><td>').sub('** | ', cell)
        tablehtml = re.compile('\t' + origincell).sub(cell, tablehtml)

    # Table body
    tablehtml = re.compile(r'<tr><td>').sub('| ', tablehtml)
    tablehtml = re.compile(r'</td></tr>').sub(' |', tablehtml)
    tablehtml = re.compile(r'</th><td>').sub(' | ', tablehtml)
    tablehtml = re.compile(r'</td><td>').sub(' | ', tablehtml)

    # Final Check
    tablehtml = re.compile(r'<tbody>').sub("", tablehtml)

    return tablehtml


if __name__ == '__main__':
    yaml_csv_path = 'data2.csv'

    import os

    if os.path.isfile(yaml_csv_path):
        with io.open(yaml_csv_path, "r", encoding="utf8") as csvfile:
            # 这里不需要readlines
            for line in csvfile.readlines():
                print line

    today = datetime.datetime.today()
    today = '{}-{:0>2d}-{:0>2d}'.format(today.year, today.month, today.day)

    # Read head string from "_post_head.csv"

    with io.open(yaml_csv_path, "r", encoding="utf8") as csvfile:

        # data,from_file,to_path,to_file,img_path
        line_num = 0
        for line in csvfile.readlines():
            row = line.split(",")
            print row

            line_num += 1
            if line_num == 1:
                continue
            from_file = os.path.join(DIR_ROOT, row[1])
            to_path = os.path.join(DIR_ROOT, row[2])
            file_name = row[3]
            to_file = os.path.join(to_path, row[3]) + ".md"
            img_path = os.path.join(DIR_ROOT, row[4])

            if not os.path.isfile(from_file):
                print('\n\tWarning: "{}" doesn\'t exist.\n\n'.format(from_file))
                continue

            # ipynb_image_path = os.path.join(ipynb_path, r'{}_files'.format(fname))
            # destination_path = os.path.join(os.path.join(thepath, 'assets'), 'ipynb-images')
            # post_path = os.path.join(thepath, r'_posts/{}.md').format(date + '-' + fname)

            # Convert ipynb to markdown
            os.system('jupyter nbconvert --to markdown ' + from_file)
            # Move it to "/_posts" and renameit

            if os.path.isfile(to_file):
                os.remove(to_file)

            image_from = os.path.join(DIR_ROOT, os.path.dirname(from_file), file_name + "_files")
            image_to = os.path.join(DIR_ROOT, to_path, "resources")
            move_image(image_from, image_to)

            md_from_file = from_file.replace(".ipynb", ".md")
            md_to_file = to_file
            # shutil.move(from_file.replace(".ipynb", ".md"), to_file)

            content = ""
            with io.open(md_from_file, 'r', encoding='utf8') as f:
                content = f.read()
            content = re.compile(r'{}_files'.format(file_name)).sub(r'resources', content)
            #
            tables = re.compile(r'<table[\s\S]*?</table>').findall(content)
            if tables:
                for table in tables:
                    pass
                    # content = re.compile(table).sub(transfertable(table), content)

            # os.remove(post_path)
            content = re.sub(r"\n{5,}", "\n", content)
            with io.open(md_to_file, 'w', encoding='utf8') as f:
                f.write(content)
