numbers = [int(x) for x in input("Enter a number:")]
number =[]
for i in range(0,len(numbers)):
    if numbers[i] in number:
        pass
    else:
        number.append(numbers[i])
print(number)
