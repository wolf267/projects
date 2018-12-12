'''
给定一个字符串，寻找没有字符串重复的最长字符串
'''
s = 'abcabccbddskkcb'
l = list(s)
l = list(set(l))
s =''.join(l)
print(s, len(s))
