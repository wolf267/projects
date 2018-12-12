'''
求1000以内能被3或5整出的数之和
'''
#sum = 0
#for i in range(1000):
#	if i%3==0 or i%5==0:
#		sum += i
#print(sum)

# way2
print(sum([i for i in range(1,1000) if i%3==0 or i%5==0]))
# way3
print(sum(i for i in range(1000) if i%3==0 or i%5==0))