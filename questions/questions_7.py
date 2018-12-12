'''
计算1-1000所有数字转化为英文后英文的总长度
'''
def count_num(num):
	num_word1 = {
		1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',\
		7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',\
		12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',\
		16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',\
		0:''
	}
	num_word2 = {
		2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',\
		7:'seventy',8:'eighty',9:'ninety',0:''
	}
	str = ''
	for i in range(1,num+1):
		if i <= 19:
			str += (num_word1[i])
		elif i < 100:
			str += (num_word2[i//10] + num_word1[i%10])
		elif i < 1000:
			str += (num_word1[i//100] + 'hundredand' + \
				num_word2[i//10%10] + num_word1[i%100])
		else:
			str += 'onethousand'
	return str

print(len(count_num(999)))