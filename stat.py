#!/usr/bin/env python3

import os
from re import sub
import string
import csv
from zhon.hanzi import punctuation # pip install zhon


def processText(text: str):
    text = sub("\(.*?\)", '', text)
    text = sub("（.*?）", '', text)
    return text.translate(str.maketrans('', '', string.punctuation + punctuation + '\n\r '))


stat={}
dirs = ('bx1', 'bx1sd', 'bx2', 'bx2sd', 'xb1',
        'xb1sd', 'xb2', 'xb2sd', 'xb3', 'xb3sd', 'kb')
for d in dirs:
    for f in os.listdir(d):
        fstr = open(os.path.join(d, f),
                    encoding="utf-8").read().replace(' ', '').replace('　', '')
        poem = processText(fstr.removeprefix(fstr.split('\n')[0]+'\n'+fstr.split('\n')[1]+'\n'))
        for c in poem:
            stat[c]=stat.get(c,0)+1
stat = sorted(stat.items(), key=lambda x: x[1])
print(dict(stat))
with open('stat.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(stat)
