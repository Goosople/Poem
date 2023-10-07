#!/usr/bin/env python3

from fontTools.ttLib import TTFont
import os

f = TTFont("f.ttf")
uniMap = f['cmap'].tables[0].ttFont.getBestCmap()

s = ""
dirs = ('bx1', 'bx1sd', 'bx2', 'bx2sd', 'xb1',
        'xb1sd', 'xb2', 'xb2sd', 'xb3', 'xb3sd', 'kb')
for d in dirs:
    for f in os.listdir(d):
        fstr = open(os.path.join(d, f),
                    encoding="utf-8").read().replace(' ', '').replace('　', '')
        s += fstr.replace('\n','')

ldic = {}
for c in s:
    if not (ord(c) in uniMap.keys()):
        ldic[c] = ord(c)
print(ldic)
