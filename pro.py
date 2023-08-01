import os
import json
from re import sub


def splitText(text: str):
    chars = ('。', '！', '？', '……', '；')
    text = sub("\(.*?\)", '', text)
    text = sub("（.*?）", '', text)
    r = [text.replace('“', '').replace(
        '”', '').replace('‘', '').replace('’', '').replace('\n', '')]
    t = []
    for c in chars:
        for s in r:
            for i in s.split(c):
                if (i+c) in s:
                    t.append(i+c)
                else:
                    t.append(i)
        r = t
        t = []
    # for i in range(len(r)):
    #     if r[i][0]=='(':
    #         r[i-1]+=r[i][:r[i].find(')')+1]
    #         r[i]=r[i][r[i].find(')')+1:]
    r.pop()
    return r


ls=[]
dirs = ('bx1', 'bx1sd', 'bx2', 'bx2sd', 'xb1',
        'xb1sd', 'xb2', 'xb2sd', 'xb3', 'xb3sd', 'kb')
for d in dirs:
    dls=[]
    for f in os.listdir(d):
        fstr = open(os.path.join(d, f),
                    encoding="utf-8").read().replace(' ', '').replace('　', '')
        title = fstr.split('\n')[0]
        poet = fstr.split('\n')[1]
        poem = fstr.removeprefix(title+'\n'+poet+'\n')
#        print('\033[1m'+title+'\033[0m , '+poet, splitText(poem))
        dls.append({'title':title,'poet':poet,'poem':splitText(poem)})
    ls.append(dls)
#print(dic['bx1'])
jsn=json.dumps(ls)
print(ls) #,'\n========================================\n',jsn)
jsnf=open("poem.json",'w+')
jsnf.write(jsn)
jsnf.close()
