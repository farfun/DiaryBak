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
def moveallfiles(origindir, destinationdir, filename):
    if not os.path.exists(origindir):
        return
    # Delete all image files which contain "fname" in their filename
    for file in os.listdir(destinationdir):
        if file[:len(filename)] == filename:
            os.remove(os.path.join(destinationdir, file))
    for file in os.listdir(origindir):
        originfile = os.path.join(origindir, file)
        destinationfile = os.path.join(destinationdir, file)
        # If it exists, then delete it and then conduct the movement
        if os.path.isfile(destinationfile):
            os.remove(destinationfile)
        shutil.move(originfile, destinationfile)
        # Delete the origin image path
        # shutil.rmtree(ipynb_image_path)


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
            os.system('jupyter nbconvert --to markdown '.format(from_file))
            # Move it to "/_posts" and renameit

            shutil.move(from_file.replace(".ipynb", ".md"), to_file)
            if os.path.isfile(to_file):
                os.remove(to_file)
                # os.rename(os.path.join(thepath, r'_posts/{}.md').format(fname), post_path)

                # moveallfiles(ipynb_image_path, destination_path, fname)

                # with io.open(post_path, 'r', encoding='utf8') as f:
                #     fstr = f.read()
                #
                # # Replace the image link strings
                # fstr = re.compile(r'{}_files'.format(fname)).sub(r'https://wklchris.github.io/assets/ipynb-images', fstr)
                # fstr = headstr + fstr
                #
                # tablehtmllst = re.compile(r'<table>[\s\S]*?</table>').findall(fstr)
                # if tablehtmllst:
                #     for
                # table in tablehtmllst:
                # fstr = re.compile(table).sub(transfertable(table), fstr)
                #
                # os.remove(post_path)
                # fstr = re.sub(r"\n{5,}", "\n", fstr)
                # with io.open(post_path, 'w', encoding='utf8') as f:
                #     f.write(fstr)
