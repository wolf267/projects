'''
从排序好的数组里面，删除重复的元素，重复的数字最多出现2次
nums = [1,1,1,2,2,3] => nums = [1,1,2,2,3]
'''
from collections import Counter

nums = [1,1,1,2,2,3]
c = Counter(nums)
for num, count in c.items():
	for i in range(2, count):
		nums.remove(num)
print(nums)