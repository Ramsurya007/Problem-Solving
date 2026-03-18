word = input("Enter a word").replace(" ","")
dict={}
for i in word:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
