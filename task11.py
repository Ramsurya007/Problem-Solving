num = int(input())
max1 = 0
while num!=0:
	temp =num%10
	if max1<temp:
		max1=temp
	num=num//10
print(max1)
