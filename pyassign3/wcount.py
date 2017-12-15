#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Caoyuge "
__pkuid__  = "1700011740"
__email__  = "1700011740@pku.edu.cn"
"""

import sys

from urllib.request import urlopen


def wcount(lines, topn=10):
    l_lines = lines.lower()
    words_lines = ""
    count_lines = {}
    for i in l_lines:
        if not 96 < ord(i) < 123:
            words_lines = words_lines + " "
        else:
            words_lines = words_lines + i
    word_lines = words_lines.split()
    word1_lines = list(set(word_lines))
    for i in word1_lines:
        count_lines[i] = word_lines.count(i)
    zip_count_lines = zip(count_lines.values(), count_lines.keys())
    sorted_count_lines = sorted(zip_count_lines)
    sorted_count_lines.reverse()
    for i in range(topn):
        print(sorted_count_lines[i][1] + " " * (30 - len(str(sorted_count_lines[i][0]) + sorted_count_lines[i][1])) + str(sorted_count_lines[i][0]))
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)