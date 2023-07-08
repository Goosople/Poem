for i in ['报任安书\n', '礼运\n', '山居秋暝\n', '菩萨蛮\n', '苏幕遮\n', '菩萨蛮·书江西造口壁\n', '青玉案·元夕\n', '贺新郎\n', '长亭送别\n', '朝天子·咏喇叭\n']:
    f=open(i.strip('\n')+'.txt','w+',encoding='utf-8')
    f.write(i)
    f.close()