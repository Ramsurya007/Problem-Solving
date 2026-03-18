vowel = input("Enter")
count =0
for i in vowel:
    if i.upper() in 'AEIOU':
        count+=1
print(count)
