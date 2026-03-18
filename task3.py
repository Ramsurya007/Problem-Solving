char = input("Enter a number ")
num = int(char)
rev = 0
for i in range(len(char)):
	temp = num % 10
	print(temp)
	rev = temp+rev*10
	print(rev)
	num = num//10
	print(num)
print(rev)
