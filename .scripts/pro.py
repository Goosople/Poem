import re
import os

file = input('FileName: ')
print('Processing ' + file + ' ...')

f = open(file, "r", encoding='utf-8')
s = f.read()

print('Contents waiting to be processed: ')
print(s)

c = re.findall("\<h1 style=\"font-size:20px; line-height:22px; height:22px; margin-bottom:10px;\"\>[\s\S]*?\</div\>",s)

str = ''
c = str.join(c)

c = re.sub('\<[\s\S]*?\>','',c)
c = re.sub('\n\n','\n',c)

print('Processed contents: ')
print(c)

f.close()
os.remove(file)

file = 'Processed_' + file
f = open(file, 'w+', encoding='utf-8')
f.write(c)
f.close()

f = open(file, "r", encoding='utf-8')
file2nd = f.readline()
f.close()
os.remove(file)

file = file2nd.replace(' / ','／')
file = file.replace('\n','') + '.txt'

f = open(file, 'w+', encoding='utf-8')
f.write(c)
f.close()
