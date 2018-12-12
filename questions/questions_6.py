'''
有一串长的字符串 
names = 'LI XIA ,ZHAO MING  ,LAO WANG >,LI MEI MEI,
CHANG JIANG,LI QIANG,ZHANG WU JI,ZHANG SAN FENG,DU 
GU QIU BAI, QIAO FENG'
1,过滤出所有的名字，去掉每个名字的左右的空格和乱码，每个名字的首字母大写。
2，统计出所有的名字里面名字最长的。
3，统计出同姓的人名单。
'''

names = 'LI XIA ,ZHAO MING  ,LAO WANG >,LI MEI MEI,\
CHANG JIANG,LI QIANG,ZHANG WU JI,ZHANG SAN FENG,DU \
GU QIU BAI, QIAO FENG'

names = {
	name.capitalize().strip(' >*'): len(name) \
	for name in names.split(',')
}
print(sorted(names.items(), key=lambda x: x[1], reverse=True)[0])
