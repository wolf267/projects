'''
给定2个字符串s1,s2,判定s2能否给s1做循环移位得到字符串的包含
s1='AABBCD', s2='CDAA'.
'''
s1='AABBCD'
s2='CDAA'
def problem5(s1, s2):
	s3 = s1 + s1
	return True if s2 in s3 else False


