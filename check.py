#!/usr/bin/env python3

cpl=open("cpl.txt",encoding="utf-8").readlines()
pl=open("pl.txt",encoding="utf-8").readlines()
isin=[]
isnotin=[]
for i in cpl:
    for j in pl:
        if i.strip('\n') in j:
            isin.append(i)
for i in cpl:
    if not(i in isin):
        isnotin.append(i)
print("In: \033[1;32m",isin,"\033[0m")
print("Not in: \033[1;31m",isnotin,"\033[0m")
